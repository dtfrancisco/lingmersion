from app import app
from flask import request, jsonify, Response, g
import psycopg2
from app.helpers.frontend_helpers import *
from app.helpers.database_helpers import *
from datetime import date
import requests
import os
from dotenv import load_dotenv

@app.before_request
def before_request():
    DB_HOST = 'localhost'
    DB_NAME = 'postgres'
    DB_USER = 'postgres'
    DB_PASS = 'admin'

    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    g.conn = conn

@app.after_request
def after_request(response):
    g.conn.close()
    return response

@app.route('/lists/')
def get_lists():
    properties = ('id', 'name', 'author', 'description', 'language', 'date_created', 'last_modified')
    rows = fetch_rows_as_dict('SELECT * FROM lists ORDER BY created ASC;', properties)
    return jsonify(rows)

@app.route('/addlist/', methods=['POST'])
def add_list():
    list = parse_list_info()

    if not list:
        return "Language provided does not exist", 404

    sql = """
          INSERT INTO Lists (name, author, description, language) VALUES(%s, %s, %s, %s)
          """
    data = (list['name'], list['author'], list['description'], list['language'])
    add_or_update_row(sql, data)

    return jsonify(list), 201

@app.route('/list/<int:id>/', methods=['GET', 'PUT'])
def handle_list(id):
    properties = ('id', 'name', 'author', 'description', 'language', 'date_created', 'last_modified')
    rows = fetch_rows_as_dict(f'SELECT * FROM lists WHERE id = {id};', properties)
    if not rows:
        return "List doesn't exist", 404 

    if request.method == 'PUT':
        list = parse_list_info()

        if not list:
            return "Language provided does not exist", 404

        sql = """UPDATE Lists
                 SET name = %s, author = %s, description = %s, language = %s, last_modified = Now()
                 WHERE id = %s
              """
        data = (list['name'], list['author'], list['description'], list['language'], id)
        add_or_update_row(sql, data)
        return '', 204

    # Just return data normally if request method is GET
    return jsonify(rows)

@app.route('/cards/list/<int:listId>/')
def get_cards_by_list(listId):
    properties = ('id', 'listid', 'term', 'author', 'description', 'language', 'date_created', 'last_modified', 'name', 'listauthor', 'listdescription')
    sql = f"""
          SELECT cards.*, name, lists.author AS listauthor, lists.description AS listdescription FROM cards 
          LEFT JOIN lists ON cards.listid = lists.id WHERE listid = {listId} ORDER BY created ASC;
          """
    rows = fetch_rows_as_dict(sql, properties)
    return jsonify(rows)

@app.route('/list/<int:listId>/card/<int:cardId>/', methods=['GET', 'PUT'])
def handle_card(listId, cardId):
    properties = ('id', 'listid', 'term', 'author', 'description', 'language', 'date_created', 'last_modified')
    row = fetch_rows_as_dict(f'SELECT * FROM cards WHERE listid = {listId} ORDER BY created ASC OFFSET {cardId - 1} LIMIT 1;', properties)
    if not row:
        return "Card doesn't exist", 404 

    if request.method == 'PUT':
        card = parse_card_info()

        # Check if a valid, existing language was provided
        if not card:
            return "Language provided does not exist", 404

        sql = """UPDATE Cards
                 SET author = %s, term = %s, description = %s, language = %s, last_modified = Now()
                 WHERE listid = %s AND id = %s
              """
        data = (card['author'], card['term'], card['description'], card['language'], listId, cardId)
        add_or_update_row(sql, data)
        return '', 204

    # Just return data normally if request method is GET
    return jsonify(row)

@app.route('/list/<int:listId>/addcard/', methods=['POST'])
def add_card(listId):
    # Check if listId provided exists
    list_resp = handle_list(listId)
    if list_resp == ("List doesn't exist", 404):
        return "List doesn't exist", 404

    card = parse_card_info()

    # Check if a valid, existing language was provided
    if not card:
        return "Language provided does not exist", 404

    audio_resp = get_audio(card["term"], card["language"])

    # Check to see if term exists in the language
    try:
        audio_resp.data
    except AttributeError:
        return f"Word doesn't exist in: {card['language']}", 404

    # check if list language matches term's language
    list_info = handle_list(listId)
    if card["language"].encode('utf-8') not in list_info.data:
        return "Language provided does not match list's language", 404

    sql = """
          INSERT INTO Cards (listId, term, author, description, language) VALUES(%s, %s, %s, %s, %s)
          """
    data = (listId, card['term'], card['author'], card['description'], card['language'])
    add_or_update_row(sql, data)

    return jsonify(card), 201

@app.route('/languages/')
def get_languages():
    languages = [
      { "name": "english", "lang_code": "en" },
      { "name": "spanish", "lang_code": "es" },
      { "name": "french", "lang_code": "fr" },
      { "name": "portuguese", "lang_code": "pt" },
    ]
    return jsonify(languages)

@app.route('/audio/<string:word>/<string:language>/')
def get_audio(word, language):
    language_codes = {
        "english": "en",
        "spanish": "es",
        "portuguese": "pt"
    }
    lang_code = language_codes[language]

    load_dotenv()
    api_key = os.environ.get('FORVO_API_KEY')
    print(f"Language {language} and word {word}")
    forvo_req_path = f"https://apifree.forvo.com/key/{api_key}/format/json/action/word-pronunciations/word/{word}/language/{lang_code}/order/rate-desc/limit/1"
    r = requests.get(forvo_req_path)
    try:
        audio_path = r.json()['items'][0]['pathmp3']
        return jsonify(audio_path)
    except IndexError:
        return f"Word doesn't exist in: {language}", 404

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

@app.route('/lists')
@app.route('/lists/')
def get_lists():
    properties = ('id', 'name', 'author', 'description', 'language', 'date_created', 'last_modified')
    rows = fetch_rows_as_dict('SELECT * FROM lists ORDER BY created ASC;', properties)
    print(rows)
    return jsonify(rows)

@app.route('/addlist', methods=['POST'])
@app.route('/addlist/', methods=['POST'])
def add_list():
    list = parse_list_info()
    sql = """
          INSERT INTO Lists (name, author, description, language) VALUES(%s, %s, %s, %s)
          """
    data = (list['name'], list['author'], list['description'], list['language'])
    add_or_update_row(sql, data)

    return jsonify(list, 201) # Add get location to newly created post

@app.route('/list/<int:id>', methods=['GET', 'PUT'])
@app.route('/list/<int:id>/', methods=['GET', 'PUT'])
def handle_list(id):
    if request.method == 'PUT':
        put_data = request.get_json()
        list = parse_list_info()
        sql = """UPDATE Lists
                 SET name = %s, author = %s, description = %s, language = %s, last_modified = Now()
                 WHERE id = %s
              """
        data = (list['name'], list['author'], list['description'], list['language'], id)
        add_or_update_row(sql, data)

        return jsonify({'data': put_data})

    # Just return data normally if request method is GET
    properties = ('id', 'name', 'author', 'description', 'language', 'date_created', 'last_modified')
    rows = fetch_rows_as_dict(f'SELECT * FROM lists WHERE id = {id};', properties)
    print(rows)
    return jsonify(rows)

@app.route('/cards/list/<int:listId>')
@app.route('/cards/list/<int:listId>/')
def get_cards_by_list(listId):
    properties = ('id', 'listid', 'term', 'author', 'description', 'language', 'date_created', 'last_modified', 'name', 'listauthor', 'listdescription')
    sql = f"""
          SELECT cards.*, name, lists.author AS listauthor, lists.description AS listdescription FROM cards 
          LEFT JOIN lists ON cards.listid = lists.id WHERE listid = {listId} ORDER BY created ASC;
          """
    rows = fetch_rows_as_dict(sql, properties)
    print(rows)
    return jsonify(rows)

@app.route('/list/<int:listId>/card/<int:cardId>', methods=['GET', 'PUT'])
@app.route('/list/<int:listId>/card/<int:cardId>/', methods=['GET', 'PUT'])
def handle_card(listId, cardId):
    if request.method == 'PUT':
        card = parse_card_info()
        sql = """UPDATE Cards
                 SET author = %s, term = %s, description = %s, language = %s, last_modified = Now()
                 WHERE listid = %s
              """
        data = (card['author'], card['term'], card['description'], card['language'], listId)
        add_or_update_row(sql, data)
        return jsonify({'data': data})

    # TODO- Just return data normally if request method is GET
    properties = ('id', 'listid', 'term', 'author', 'description', 'language', 'date_created', 'last_modified')
    rows = fetch_rows_as_dict(f'SELECT * FROM cards WHERE listid = {listId} ORDER BY created ASC OFFSET {cardId};', properties)
    print("Bondi", rows)
    return jsonify(rows)

@app.route('/list/<int:listId>/addcard', methods=['POST'])
@app.route('/list/<int:listId>/addcard/', methods=['POST'])
def add_card(listId):
    # TODO: 1. listId must match actual list
    card = parse_card_info()
    sql = """
          INSERT INTO Cards (listId, term, author, description, language) VALUES(%s, %s, %s, %s, %s)
          """
    data = (listId, card['term'], card['author'], card['description'], card['language'])
    add_or_update_row(sql, data)

    return jsonify(card, 201) # Add get location to newly created post

@app.route('/languages')
@app.route('/languages/')
def get_languages():
    languages = [
      { "name": "english", "id": 39 },
      { "name": "spanish", "id": 41 },
      { "name": "portuguese", "id": 133 },
    ]
    return jsonify(languages)

@app.route('/getaudio/<string:word>/<string:language>')
@app.route('/getaudio/<string:word>/<string:language>/')
def get_audio(word, language):
    languages = {
        "english": 39,
        "spanish": 41,
        "portuguese": 133
    }
    id = languages[language]

    load_dotenv()
    api_key = os.environ.get('FORVO_API_KEY')
    print(f"Language {language} and word {word}")
    forvo_req_path = f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/{word}/id_lang_speak/{id}/order/rate-desc/limit/1/key/{api_key}/" 
    r = requests.get(forvo_req_path)
    audio_path = r.json()['items'][0]['pathmp3']
    return(jsonify(audio_path))
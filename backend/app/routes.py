from app import app
from flask import request, jsonify, Response
from app.data import LISTS, CARDS
from app.helpers import get_number_of_cards_in_list
from datetime import date
import requests
import os
from dotenv import load_dotenv

@app.route('/lists')
@app.route('/lists/')
def get_lists():
    return jsonify(LISTS)

@app.route('/list/<int:id>')
@app.route('/list/<int:id>/')
def get_list(id):
    for list in LISTS:
        if list['id'] == id:
            return jsonify(list)
    return None

@app.route('/addlist', methods=['POST'])
@app.route('/addlist/', methods=['POST'])
def add_list():
    post_data = request.get_json()
    list = {
        'id': len(LISTS) + 1,
        'name': post_data.get('name'),
        'author': post_data.get('author'),
        'description':  post_data.get('description'),
        'language': post_data.get('language'),
        'created': date.today(),
        'modified': date.today()
    }
    LISTS.append(list)
    return jsonify(list, 201) # Add get location to newly created post

@app.route('/cards/list/<int:listId>')
@app.route('/cards/list/<int:listId>/')
def get_cards_by_list(listId):
    cardsInList = []
    for card in CARDS:
        if listId == card['listId']:
            cardsInList.append(card)

    return jsonify(cardsInList)

@app.route('/list/<int:listId>/card/<int:cardId>', methods=['GET', 'PUT'])
@app.route('/list/<int:listId>/card/<int:cardId>/', methods=['GET', 'PUT'])
def handle_card(listId, cardId):
    if request.method == 'PUT':
        for card in CARDS:
            if listId == card['listId']:
                if cardId == card['cardId']:
                    put_data = request.get_json()
                    CARDS.append(put_data)
                    CARDS.remove(card)
                    return jsonify({'data': put_data})
    else:
        for card in CARDS:
            if listId == card['listId']:
                if cardId == card['cardId']:
                    return jsonify(card)
        return None

@app.route('/list/<int:listId>/addcard', methods=['POST'])
@app.route('/list/<int:listId>/addcard/', methods=['POST'])
def add_card(listId):
    # TODO: Do input validation on card 1. listId must match actual list and names must match.
    # Is this necessary? 2. Verify created and modified dates
    num_cards_in_list = get_number_of_cards_in_list(listId)
    post_data = request.get_json()
    card = {
        'listId': listId,
        'cardId': num_cards_in_list + 1,
        'author': post_data.get('author'),
        'term': post_data.get('term'),
        'description':  post_data.get('description'),
        'language': post_data.get('language'),
        'created': date.today(),
        'modified': date.today()
    }
    CARDS.append(card)
    return jsonify(card, 201) # Add get location to newly created post

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

    forvo_req_path = f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/{word}/id_lang_speak/{id}/order/rate-desc/limit/1/key/{api_key}/" 
    r = requests.get(forvo_req_path)
    audio_path = r.json()['items'][0]['pathmp3']
    return(jsonify(audio_path))
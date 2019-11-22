from app import app
from flask import request, jsonify, Response
from app.data import LISTS, CARDS
from datetime import date
import requests
import os
from dotenv import load_dotenv

@app.route('/lists')
@app.route('/lists/')
def lists():
    return jsonify(LISTS)

@app.route('/cards')
@app.route('/cards/')
def cards():
    return jsonify(CARDS)

@app.route('/addcard', methods=['POST'])
@app.route('/addcard/', methods=['POST'])
def add_card():
    # TODO: Do input validation on card 1. listId must match actual list and names must match.
    # Is this necessary? 2. Verify created and modified dates
    post_data = request.get_json()
    card = {
        'listId': post_data.get('id'),
        'cardId': len(CARDS) + 1,
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
        "portuguese": 113
    }
    id = languages[language]

    load_dotenv()
    api_key = os.getenv('FORVO_API_KEY')

    forvo_req_path = f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/{word}/id_lang_speak/{id}/order/rate-desc/limit/1/key/{api_key}/" 
    r = requests.get(forvo_req_path)
    audio_path = r.json()['items'][0]['pathmp3']
    return(jsonify(audio_path))
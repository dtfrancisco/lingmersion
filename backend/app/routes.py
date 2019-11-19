from app import app
from flask import jsonify
from datetime import date

@app.route('/lists')
@app.route('/lists/')
def lists():
    item_1 = {
        'id': 1,
        'name': 'List One',
        'author': 'Jane Doe',
        'description': 'My first list',
        'created': date(2019, 4, 7),
        'modified': date(2019, 8, 13)
    }
    item_2 = {
        'id': 2,
        'name': 'List Two',
        'author': 'John Smith',
        'description': 'Spanish vocabulary',
        'created': date(2018, 2, 28),
        'modified': date(2018, 7, 17)
    }
    lists = [item_1, item_2]
    return jsonify(lists)

@app.route('/cards')
@app.route('/cards/')
def cards():
    item_1 = {
        'listId': 1,
        'cardId': 1,
        'author': 'Jane Doe',
        'term': 'coisa',
        'description': 'algo que existe',
        'language': 'portuguese',
        'created': date(2019, 4, 7),
        'modified': date(2019, 4, 9)
    }
    item_2 = {
        'listId': 1,
        'cardId': 2,
        'author': 'Jane Doe',
        'term': 'cachorro',
        'description': 'animal fofinho e o melhor amigo do homem',
        'language': 'portuguese',
        'created': date(2019, 8, 13),
        'modified': date(2019, 8, 13)
    }
    item_3 = {
        'listId': 2,
        'cardId': 3,
        'author': 'John Smith',
        'term': 'entender',
        'description': 'saber algo',
        'language': 'spanish',
        'created': date(2018, 2, 28),
        'modified': date(2018, 4, 17)
    }
    cards = [item_1, item_2, item_3]
    return jsonify(cards)

@app.route('addcard', methods=['POST'])
@app.route('addcard/', methods=['POST'])
def add_card():
    pass

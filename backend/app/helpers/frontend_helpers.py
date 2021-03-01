from flask import request

def parse_list_info():
    data = request.get_json()

    list = {
        'name': data.get('name'),
        'author': data.get('author'),
        'description':  data.get('description'),
        'language': data.get('language'),
    }
    return list

def parse_card_info():
    data = request.get_json()

    card = {
        'author': data.get('author'),
        'term': data.get('term'),
        'description':  data.get('description'),
        'language': data.get('language')
    }
    
    return card

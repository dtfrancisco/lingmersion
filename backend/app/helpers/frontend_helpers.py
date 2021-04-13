from flask import request

def parse_list_info():
    data = request.get_json()
    validated = validate_language(data.get('language'))
    if not validated:
        return None
    list = {
        'name': data.get('name'),
        'author': data.get('author'),
        'description':  data.get('description'),
        'language': data.get('language'),
    }
    return list

def parse_card_info():
    data = request.get_json()
    validated = validate_language(data.get('language'))
    if not validated:
        return None
    card = {
        'author': data.get('author'),
        'term': data.get('term'),
        'description':  data.get('description'),
        'language': data.get('language')
    }
    
    return card

def validate_language(language):

    language_codes = {
        "english": "en",
        "spanish": "es",
        "portuguese": "pt",
        "french": "fr"
    }

    for lang in language_codes.keys():
        if lang == language:
            return True
    return False

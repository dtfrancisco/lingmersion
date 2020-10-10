from datetime import date

LISTS = [
    {
        'id': 1,
        'name': 'List One',
        'author': 'Jane Doe',
        'description': 'My first list',
        'language': 'portuguese',
        'created': date(2019, 4, 7),
        'modified': date(2019, 8, 13)
    },
     {
        'id': 2,
        'name': 'List Two',
        'author': 'John Smith',
        'description': 'Spanish vocabulary',
        'language': 'spanish',
        'created': date(2018, 2, 28),
        'modified': date(2018, 7, 17)
    }
]

CARDS = [
    {
        'listId': 1,
        'cardId': 1,
        'author': 'Jane Doe',
        'term': 'coisa',
        'description': 'algo que existe',
        'language': 'portuguese',
        'created': date(2019, 4, 7),
        'modified': date(2019, 4, 9)
    },
    {
        'listId': 1,
        'cardId': 2,
        'author': 'Jane Doe',
        'term': 'cachorro',
        'description': 'animal fofinho e o melhor amigo do homem',
        'language': 'portuguese',
        'created': date(2019, 8, 13),
        'modified': date(2019, 8, 13)
    },
    {
        'listId': 2,
        'cardId': 1,
        'author': 'John Smith',
        'term': 'entender',
        'description': 'saber algo',
        'language': 'spanish',
        'created': date(2018, 2, 28),
        'modified': date(2018, 4, 17)
    }
]
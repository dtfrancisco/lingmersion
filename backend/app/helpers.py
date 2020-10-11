from app.data import LISTS, CARDS

def get_number_of_cards_in_list(listId):
    for list in LISTS:
        if list['id'] == listId:
            num_cards = 0
            for card in CARDS:
                if card['listId'] == listId:
                    num_cards += 1
            break

    return num_cards

# -*- coding: UTF-8 -*-
import random
import os
import codecs
def create_deck_54(new_deck):
    '推出一幅新牌'
    print('\n--debug:I made a new deck.')
    cardJokers = ('♞', '♘')
    cardMarks =('♣', '♦', '♥', '♠')

    cardNumbers=('2', '3', '4', '5', '6', '7', '8',
                    '9', '10', 'J', 'Q', 'K', 'A')
    for c in cardJokers:
        new_deck.append(c)

    # add 4x13 cards
    for cn in cardNumbers:
        for cm in cardMarks:
            # card = cm + cn
            card=cn + cm
            new_deck.append(card)

    return

def create_deck_52(new_deck):
    '推出一幅新牌'
    print('\n--debug:I made a new deck.')
    cardJokers = ('♞', '♘')
    cardMarks =('♣', '♦', '♥', '♠')

    cardNumbers=('2', '3', '4', '5', '6', '7', '8',
                    '9', '10', 'J', 'Q', 'K', 'A')
    #for c in cardJokers:
        #new_deck.append(c)

    # add 4x13 cards
    for cn in cardNumbers:
        for cm in cardMarks:
            # card = cm + cn
            card=cn + cm
            new_deck.append(card)

    return


def shuffled_deck(deck_to_be_shuffled):
    '洗牌'
    print('\n--debug:I shuffled a new deck.')
    random.shuffle(deck_to_be_shuffled)
    return

def record_deck(deck_to_be_record, filename):
    '记录一幅牌'
    print('\n--debug:I record a new deck.')
    out_path=os.getcwd() + '\\OutputDecks\\' + filename
    f=codecs.open(out_path, "w", "utf-8")
    for card in deck_to_be_record:
        f.write(card)
        f.write('\n')
    f.close
    return

def make_deck_by_type(game_type,new_deck):
    if game_type == 1:
        create_deck_54(new_deck)
        shuffled_deck(new_deck)
        record_deck(new_deck,'text1.txt')
    if game_type == 2:
        create_deck_52(new_deck)
        shuffled_deck(new_deck)
        record_deck(new_deck,'text2.txt')
    if game_type == 3:
        create_deck_54(new_deck)
        shuffled_deck(new_deck)
        record_deck(new_deck,'text3.txt')
    if game_type == 4: # 四人斗地主的牌
        # first deck
        deck_a = []
        create_deck_54(deck_a)
        new_deck.extend(deck_a)
        # second deck
        deck_b = []
        create_deck_54(deck_b)
        new_deck.extend(deck_b)
        # shuffled & record
        shuffled_deck(new_deck)
        record_deck(new_deck,'text4.txt')
    return

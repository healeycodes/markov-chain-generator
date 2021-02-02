import sys
from generate import get_source, build_model, generate_text


def test_possible_sentences():
    state_size = 2
    min_length = 1000
    source = 'An apple is very good. An orange is very bad.'
    fruit_talk = build_model(source, state_size)

    text = generate_text(fruit_talk, state_size, min_length)

    should_appear = [
        'An apple is very bad.',
        'An orange is very bad.',
        'An orange is very good.',
        'An apple is very good.'
    ]

    for sentence in should_appear:
        if sentence not in text:
            print('A sentence wasn\'t generated')
            sys.exit(1)


def test_minimum_length():
    state_size = 2
    min_length = 100
    source = get_source('poe')
    poe = build_model(source, state_size)
    text = generate_text(poe, state_size, min_length)
    if len(text) < min_length:
        print('Minimum length too short')
        sys.exit(1)


test_possible_sentences()
test_minimum_length()

import os
import json
import random


def get_source(dir):
    '''
    Look inside src/<dir>/ for text files and concatenate their contents.
    '''
    text = ""
    files = [
        # os.path.join to keep things cross-platform friendly
        os.path.join('src', dir, name) for name in os.listdir(os.path.join('src', dir))
    ]
    for name in files:
        with open(name, encoding="utf8") as f:
            text += "\n"
            text += f.read()
    return text


def build_model(source, state_size):
    '''
    Given some corpus and a state size, build a Markov chain model (as a dictionary).
    '''
    source = source.split()
    model = {}
    for i in range(state_size, len(source)):
        current_word = source[i]
        previous_words = ' '.join(source[i-state_size:i])
        if previous_words in model:
            model[previous_words].append(current_word)
        else:
            model[previous_words] = [current_word]

    return model


def generate_text(model, state_size, length):
    '''
    Consume a Markov chain model (make sure to specify the <state_size> used)
    to generate text that is at least <length> size long.
    '''
    possible_starters = random.sample(list(model.keys()), len(model.keys()))
    text = next(s.split(' ') for s in possible_starters if s[0].isupper())

    i = state_size
    while True:
        key = ' '.join(text[i-state_size:i])
        next_word = random.choice(model[key])
        text.append(next_word)
        i += 1
        if i > length and text[-1][-1] == '.':
            break
    return ' '.join(text)


if __name__ == "__main__":
    state_size = 2
    length = 100
    source = get_source('poe')
    poe = build_model(source, state_size)
    text = generate_text(poe, state_size, 100)
    print(text)

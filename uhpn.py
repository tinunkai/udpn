table = {
    'iu': 'Q',
    'ia': 'W',
    'ua': 'W',
    'uan': 'R',
    'ue': 'T',
    've': 'T',
    'ing': 'Y',
    'uai': 'Y',
    'sh': 'U',
    'ch': 'I',
    'uo': 'O',
    'un': 'P',
    'iong': 'S',
    'ong': 'S',
    'iang': 'D',
    'uang': 'D',
    'en': 'F',
    'eng': 'G',
    'ang': 'H',
    'an': 'J',
    'ao': 'K',
    'ai': 'L',
    'ei': 'Z',
    'ie': 'X',
    'iao': 'C',
    'zh': 'V',
    'ui': 'V',
    'ou': 'B',
    'in': 'N',
    'ian': 'M',
}

import random

while True:
    key = random.choice(list(table))
    print(key)
    input()
    print(table[key])
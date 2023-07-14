import random

locales_data = {
    'en': {
        'vowels': ('a', 'e', 'i', 'o', 'u', 'y'),
        'consonants': ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z',
                       'sh', 'zh', 'ch', 'kh', 'th')
    }
}

def generate_name(locale=None) -> str:
    data = locales_data['en']
    vowels = data['vowels']
    consonants = data['consonants']
    is_vowels_first = bool(random.randint(0, 1))
    result = ''.join(random.choice(vowels) if (is_vowels_first and i % 2 == 0) or (not is_vowels_first and i % 2 != 0) else random.choice(consonants) for i in range(random.randint(6, 9)))
    return result.title()
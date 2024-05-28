from unidecode import unidecode

def remove_accents(text: str) -> str:
    return unidecode(text)
from hazm import *

class Tokenizer: 
    def simple_toke(text: str, seperator: str):
        result = []
        word = text.split(sep=seperator)
        
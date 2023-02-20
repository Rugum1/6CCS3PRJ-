from spellchecker import SpellChecker
import json

class CSTermsSpellChecker():


    def load_file(self,file):
        with open(file , "r", encoding ="utf-8") as f:
            data = json.load(f)
        return(data)

    def process_data_from_file(self,file):
        processed_data = []
        data = self.load_file(file)
        for term in data:
            split_terms  = term.split()
            for term2 in split_terms:
                processed_data.append(term2)
        return processed_data


    def check_spelling(self,text):
        text = text.strip()
        spell = SpellChecker(distance = 2)
        spell.word_frequency.load_words(self.load_file("./data/computer_science_abreviations.json"))
        spell.word_frequency.load_words(self.process_data_from_file("./data/computer_science_glossary.json"))
        misspelled = text.split(' ')
        checked_words = []
        for word in misspelled:
            checked_words.append(spell.correction(word))

        return ' '.join(checked_words)

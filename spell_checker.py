from spellchecker import SpellChecker

class CSTermsSpellChecker():


    def check_spelling(text):
        spell = SpellChecker(distance = 2)
        misspelled = text.split(' ')
        checked_words = []
        for word in misspelled:
            checked_words.append(spell.correction(word))

        return ' '.join(checked_words)

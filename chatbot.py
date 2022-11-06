
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
# import nltk

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

#Create a new instance of a ChatBot

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'adapters.MyLogicAdapter',
        },
        # 'chatterbot.logic.MathematicalEvaluation',
        # 'chatterbot.logic.TimeLogicAdapter',
        # 'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)

# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.english")


print('Type something to begin...')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)
        print()

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

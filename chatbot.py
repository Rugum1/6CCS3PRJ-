
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
# import nltk



#Create a new instance of a ChatBot

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'adapters.CSTermsAdapter',
        },
        

    ],
    database_uri='sqlite:///database.sqlite3'
)


print('Type something to begin...')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()
        bot_response = bot.get_response(user_input)


        print(bot_response)
        print()

    # Press ctrl-c or ctrl-d on the keyboard to exit
    # except Exception as e:
    #        bot_response = "I do not understand what you mean"
    #        print(e)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

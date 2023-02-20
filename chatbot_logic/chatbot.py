from chatterbot import ChatBot
from chatterbot.conversation import Statement
import spacy




class ChatBotStudentAid(): 

    def __init__(self): 
        "create class"
        self.bot  = self.create_bot() 

    #Create a new instance of a ChatBot
    def create_bot(self): 

        bot = ChatBot(
                    'Chatbot',
                    storage_adapter='chatterbot.storage.SQLStorageAdapter',
                    logic_adapters=[
            
                        {
                            'import_path': 'adapters.CSTermsAdapter',
                        },
                        

                    ],
                    database_uri='sqlite:///database.sqlite3'
        )

        return bot 
    

    #Get an answer to user query 
    def get_answer(self,user_query): 

        try:

            bot_response = self.bot.get_response(user_query)

        except AttributeError: 

            bot_response = Statement(text = "I am sorry!I cannot answer your question.")

        return bot_response

    

from chatbot import bot
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english",
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

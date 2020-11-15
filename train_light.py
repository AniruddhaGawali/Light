from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot=ChatBot('light')
trainers= ChatterBotCorpusTrainer(chatbot)

trainers.train('./data/app data/think data/conversation.yml')
trainers.train('chatterbot.corpus.english')

from chatterbot.trainers import ListTrainers
from chatterbot import ChatBot
import csv

bot = ChatBot('test')

client = []
manager = []
convo = []
with open('test_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
        
    for line in csv_reader:
        convo.append(line[3])
        
convo.pop(0)      
print(convo)


bot.set_trainer(List_Trainer)
bot.train(convo)

while True:
    request = input('You: ')
    response = bot.get_response(request)
    
    print('bot: ', response)
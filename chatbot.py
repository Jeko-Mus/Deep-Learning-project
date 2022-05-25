import random
import json
import torch

from model import NeuralNet
from functions import bag_of_words, tokenize

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "trained.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

bot_name = "assistant"
print("Hi there! How can I help you today? (remember to type 'done' when you want to exit this chat)")

while True:
    sentence = input("You: ")
    if sentence == "done":
        print("Thanks for the chat! bye for now")
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    
    if prob.item() > 0.80:
        for intent in intents['intents']:
            if tag == intent['tag']:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: I do not understand. Try to be more specific")


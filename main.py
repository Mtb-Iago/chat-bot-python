from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

def treinamento():
    train = []
    data = json.loads(open('treinamento.json', 'r').read())

    for row in data:
        train.append(row['perguntas'])
        train.append(row['respostas'])
    return train
    # Create a new chat bot named Charlie

def menu():
    menuOpcoes = json.loads(open('menu.json', 'r').read())
    for apresentacao in menuOpcoes:
        print(f'[*] - {apresentacao["item"]}')

def chat():
    chatbot = ChatBot('Enzo')
    trainer = ListTrainer(chatbot)
    train = treinamento()
    trainer.train(train)
    
    return chatbot

if __name__ == "__main__":
    chatbot = chat()
    print('\n')
    print('Olá eu sou o Enzo um robô de atendimento, escolha um item para te ajudar: ')
    while True:
        print('\n')
        print('----------------Menu de Opções----------------')
        menu()
        print('\n')
        perguntas = input('Você: ')
        if perguntas == "s":
            print('Obrigado Volte Sempre, foi um prazer te atender :D')
            break
        resposta = chatbot.get_response(perguntas)
        if resposta.confidence >0.6:
            print('Enzo: ', resposta.text)
        else:
            print('Enzo: Ainda não sei responder essa pergunta :(')
        print('////////////////////////////')
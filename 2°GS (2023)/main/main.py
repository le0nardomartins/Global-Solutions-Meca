import speech_recognition as sr
import datetime
import pygame
from datetime import datetime
import telebot

##### INICIALIZANDO
pygame.mixer.init()
print(sr.Microphone.list_microphone_names())
definirMic = 1
i = 0

pre = int  # Nível de pressão ideal
b = str  # Nível de pressão alta
bat = int  # BATIMENTOS
a = int  # FCM
sint = str
nome = str
API = "6820946733:AAH3w-rMU3EodSlzTfmq2HgcDcfla8FqR7c"
bot = telebot.TeleBot(API)

@bot.message_handler(commands=["/Diagnóstico Rápido"])
def diagnosticorapido(msg):
    bot.send_message(msg.chat.id, "Ótimo, vamos começar!")
    pass

@bot.message_handler(commands=["/Chamar Ambulância"])
def chamarambulancia(msg):
    bot.send_message(msg.chat.id, "")
    pass

@bot.message_handler(commands=["/Doencas mais recorrentes"])
def doencasrecorrentes(msg):
    bot.send_message(msg.chat.id, "")
    pass

@bot.message_handler(commands=["/Bons hábitos de saúde"])
def bonshabitos(msg):
    bot.send_message(msg.chat.id, "")
    pass

@bot.message_handler(commands=["/Estou bem, obrigado(a)!"])
def estoubem(msg):
    bot.send_message(msg.chat.id, "Tudp bem então! Até mais!")
    pass

##### MONITORAMENTO DO MICROFONE PARA RECEBER O COMANDO
def monitoraMic():
    entrada = device_index = definirMic
    mic = sr.Recognizer()
    with sr.Microphone(entrada) as source:
        print("Ouvindo...")
        mic.pause_threshold = 0.5
        audio = mic.listen(source)
    try:
        trigger = mic.recognize_google(audio, language='pt-br')
        print(str(nome) + ": " + trigger)

    except sr.UnknownValueError:
        print('Comando inválido')
        return ' '
    return trigger

##### FUNÇÂO PARA RESPONDER USANDO O PYGAME
def resposta(arquivo):
    pygame.mixer.music.load('audio/' + arquivo + '.mp3')  # WINDONS
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


##### MONITORAMENTO DE TEMPERATURA
def temp():
    temp = int(input("Temperatura atual do usuário: "))

    if (temp >= 38):
        resposta('tempalta')  # ALERTAR O USUÁRIO SOBRE A TEMPERATURA

def agendar():
    o = str(input('Deseja agendar uma consulta? (S ou N) ').lower())
    if (o == 's'):
        print('Diga seus sintomas para já deixarmos o médico preparado para recebe-lo: ')
        sint = str(input(' '))
        with open('txt/consulta.txt', 'a', encoding='UTF-8') as consul:
            consul.write(f"----------------- CONSULTA - {nome} -----------------\n")
            consul.write(f"DATA: {datetime.now()}\n"
                    f"NOME: {nome}\n"
                    f"SINTOMAS: {sint}\n")
        print('Consulta agendada')
        resposta('fim_consulta')

    elif (o == 'n'):
        print('Tudo bem!')

    else:
        print('Resposta inválida')

##### FORMULÁRIO
def form():
    resposta('forms')  # INICIAR O FORMS

    ### PRESSÃO
    pres = input('Você tem problemas de pressão? (S ou N) ').lower()
    if (pres == 's'):
        c = input('Normalmente sua pressão é muito alta ou muito baixa? ').lower()
        pres = str('Sim')

        if (c == 'alta'):
            b = int(input('Qual é seu nível de pressão considerado alta? '))
            c = str('Hipertensão')
            pre = int(input('Qual é seu nível de pressão considerado ideal? '))

            if (pre >= b):
                resposta('pressao')  # ALERTAR O USUÁRIO SOBRE A PRESSÃO

        elif (c == 'baixa'):
            b = int(input('Qual é seu nível de pressão considerado alta? '))
            c = str('Hipotensão')
            pre = int(input('Qual é seu nível de pressão considerado ideal? '))

            if (pre >= b):
                resposta('pressao')  # ALERTAR O USUÁRIO SOBRE A PRESSÃO
    elif (pres == 'n'):
        pres = str('Não')
        c = str('tudo normal')
        pre = str('120/80')
        b = int(input('Qual é seu nível de pressão considerado alta? '))


    ##### BATIMENTOS
    bat = int(input('Qual o batimento cardiaco do usuário? '))
    idade = int(input('Qual a idade do usuario? '))
    a = 220 - idade  # Calcular os batimentos
    if (bat < a):
        print(f'O batimento ideal para o usuário não deve ultrapassar {a}BPM')
        print(f'O batimento do usário está em {bat}BPM.')
    else:
        print(f'O batimento ideal para o usuário não deveria ultrapassar {a}BPM.')
        print(f'O batimento do usário está em {bat}BPM.')
        resposta('bat')
        atv = input('Digite S ou N: ').lower()
        if (atv == 's'):
            resposta('bat_normal')

        elif (atv == 'n'):
            resposta('causas_btm')
            print('LIGUE PARA 190 EM CASO ME EMERGÊNCIA')
            print('LIGUE PARA 192 EM CASO DE MAL-ESTAR')

    ##### MONITORAMENTO DE CAMINHADA
    passos = int(input("Quantos passos o usuário deu: "))
    tempo = float(input('Tempo de caminhada (em horas): '))
    comprimentoP = 0.762  # em metros
    dist = passos * comprimentoP
    velocidadeM = (dist / tempo) * 3.6
    print(f"Distância percorrida: {dist:.2f} metros")
    print(f"Velocidade média: {velocidadeM:.2f}m/s")

    ##### FORMS
    with open('txt/formulario.txt', 'a', encoding='UTF-8') as f:
        f.write(f"----------------- FORMULARIO - {nome} -----------------\n")
        f.write(f"DATA E HORA: {datetime.now()}\n"
                f"NOME: {nome}\n"
                f"IDADE: {idade} anos\n"
                f"-------------------------------\n"
                f"BATIMENTOS: {bat} BPM\n"
                f"FCM: {a} BPM\n"
                f"-------------------------------\n"
                f"PROBLEMAS DE PESSÃO: {pres}, {c}.\n"
                f"PRESSÃO CONSIDERADA ALTA: {b} mmHg\n"
                f"PRESSÃO CONSIDERADA IDEAL: {pre} mmHg\n"
                f"-------------------------------\n"
                f"DISTÂNCIA PERCORRIDA: {dist:.2f} metros\n"
                f"VELOCIDADE ESTIMADA: {velocidadeM:.2f}m/s\n")
        f.write("--------------------------------------------------\n")
    resposta('forms_fim')  # RESPONDER SOBRE FINALIZAR FORMS




#### INICIA O PROGRAMA
if __name__ == '__main__':
    resposta("olá")
    resposta("seunome")
    nome = str(input('Digite seu nome: '))
    print(f'Olá, {nome}!')
    resposta('ouvindo')

    while (1 or 1):
        trigger = monitoraMic().lower()

        if 'ai' in trigger or 'machu' in trigger or 'dor' in trigger:
            resposta('ajuda')
            print(' 1 - Consulta\n',
                  '2 - Preencher Formulário\n',
                  '3 - Desligar\n')

            esco = input('Escolha umas opções acima: ')

            if (esco == '1'):
                print('Escolhido: Consulta')
                resposta('consulta')
                agendar()

            elif (esco == '2'):
                print('Escolhido: Formulário')
                form()

            elif (esco == '3'):
                print('Escolhido: Desligar')
                resposta('despedida')  # DESPEDINDO
                print('Vou continuar monitorando você!')
                temp()
                break

            else:
                print('Não entendi')


import cv2
import numpy as np
import tensorflow as tf
from imutils.video import VideoStream
import time
import imutils
import pygame
from gtts import gTTS

# Carregar o modelo TensorFlow Lite
interpreter = tf.lite.Interpreter(model_path="vww_96_grayscale_quantized.tflite")
interpreter.allocate_tensors()

# Obter detalhes dos tensores de entrada e saída
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


##### FUNÇÂO PARA RESPONDER USANDO O PYGAME
def resposta(arquivo):
    pygame.mixer.music.load('audio/' + arquivo + '.mp3')  # WINDONS
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

##### CRIA AUDIO
def criaAudio(trigger):
    tts = gTTS(trigger, lang='pt-br')
    tts.save('audio/mensagem.mp3')


##### VERIFICAR AS LABELS
def verifica():
    if predicted_class == "Corte Superficial":
        resposta('corte')
        resposta('corte2')

    elif predicted_class == "Pápula":
        resposta('')

    elif predicted_class == "Acne":
        resposta('')

    elif predicted_class == "Mácula":
        resposta('')

    elif predicted_class == "Placa":
        resposta('')

    elif predicted_class == "Nodulo":
        resposta('')

    elif predicted_class == "Saudável":
        resposta('')

    elif predicted_class == "Não tem ninguem":
        resposta('')


# Carregar rótulos
with open("txt\labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

# Iniciar a câmera
cap = cv2.VideoCapture(0)  # O argumento 0 indica que a câmera padrão será usada

# inicializar vídeo
vs = VideoStream(src=0).start()
time.sleep(1.0)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=800)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Pré-processar a imagem de acordo com os requisitos do modelo
    input_shape = input_details[0]['shape'][1:1]
    #frame_resized = cv2.resize(frame, (input_shape[0], input_shape[0]))
    frame_resized = frame

    # Adicionar uma dimensão extra para atender às expectativas do modelo
    input_data = np.expand_dims(frame_resized, axis=0)
    input_data = input_data.astype(np.float32) / 255.0  # Normalizar os pixels para o intervalo [0, 1]

    # Definir os dados de entrada no modelo
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # Realizar a inferência
    interpreter.invoke()

    # Obter os resultados da saída
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Processar os resultados
    predicted_class_index = np.argmax(output_data)
    predicted_class = labels[predicted_class_index]

    # Exibir o quadro na janela
    cv2.imshow('', frame)

    # Tomar ação com base na saída do modelo
    verifica()

    # Sair quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()

##### INICIALIZANDO
pygame.mixer.init()







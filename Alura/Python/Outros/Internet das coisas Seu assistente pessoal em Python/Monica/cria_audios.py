from gtts import gTTS #Importando  Google Text-to-Speech
# from subprocess import call #Importando para poder chamar o áudio Mac/Linux
from playsound import playsound #Importando para poder chamar o audio no windwos
import os

def cria_audio(mensagem, nome=None):
    tts = gTTS(mensagem, lang= 'pt-br') # Cria um audio a partir do texto passado
    if nome == None: #Se o nome for nulo, quer dizer que a assistente esta só lendo uma informação momentanea
        tts.save('Monica/audios/mensagem.mp3')# Salva o aquivo de audio (Lembre-se de acessar a função e alterar o método de salvar de "wb" para "w")
        
        # call(['afplay', 'Pedrinho/audios/hello.mp3']) #Chamada para MAC
        # call(['aplay', 'Pedrinho/audios/hello.mp3']) #Chamada para Linux
        playsound('Monica/audios/mensagem.mp3') #Chamada para WIndows
        os.remove('Monica/audios/mensagem.mp3') # Apaga o arquivo mp3 para poder ser criado e executado dps
        
    else: #senão, quer dizer que será salva uma mensagem fixa para ser usada dps
        tts.save(f'Monica/audios/{nome}.mp3')
        playsound(f'Monica/audios/{nome}.mp3')

cria_audio('Oi, Maricy tudo bom??', 'ola_maricy')

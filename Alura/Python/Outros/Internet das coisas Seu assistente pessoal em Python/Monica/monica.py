 # Exemplo retirado da biblioteca do git: https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
 # É preciso instalar o "pyaudio" (só disponivel na versão 3.6 do Python) 

import speech_recognition as sr
from playsound import playsound
from comandos import *

##### CONFIGURAÇÕES #####
# Lembre-se de atualziar o setuptool "pip3 install --upgrade setuptools", instalar "pip intall wheel" e "pip install oauth2client"
# Necessario instlar as bibliotecas "gcloud" e "google-api-python-client" (nesse ultimo use pip3).

# Acessamos o Google Cloud e seguimos os passo:
#   -Criamos um projeto
#   -Vamos no painel de API e procuramos a API do Cloud Speech
#   -Ativamos ela e genciamos
#   -No gerenciamento, colocamos o nome, declaramos ela como proprietario e a chave como jason
#   -Após isso baixamos o arquivo com a chave json e colocamos dentro da pagina da nossa aplicação

hotword = 'mônica' # Nome da nossa Assistente
with open('Alura\Python\Outros\Internet das coisas Seu assistente pessoal em Python\Monica\python-assistente-276711-89dd570a509f.json') as credenciais_google: #Abrimos o arquivo chave
    credenciais_google = credenciais_google.read() #salvamos o arquivo chave json

def responde(arquivo): # È criada uma função para respostas em voz da assitente, nela é passada o nome do arquivo a ser executado
    print(arquivo)
    playsound(f'Monica/audios/{arquivo}.mp3') # Executar aqruivo de áudio

def executa_comandos(trigger):
    if 'notícias' in trigger:
        ultimas_noticias()
    elif 'maricy' in trigger and 'oi' in trigger:
        responde('ola_maricy')
    elif ('toca' in trigger or 'tocar' in trigger or 'toque' in trigger) and 'curtidas' in trigger:
        playlist('curtidas')
    else:
        responde('comando_invalido')


def monitora_audio():
    # Obtendo o audio do microfone
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True: #Realiza um loop para sempre monitorar o áudio
            print("Aguardadndo comando...")
            audio = microfone.listen(source) #Captura o áudio

            # recognize speech using Google Speech Recognition (Usado só para Teste)
            try:
                trigger = microfone.recognize_google(audio, language= 'pt-BR')
                trigger = trigger.lower()
                if hotword in trigger:
                    print(trigger.strip(hotword)) # É retirado do trigger somente a string da hotword
                    responde('feedback')
                    executa_comandos(trigger)
                    break
                
            except sr.UnknownValueError:
                print("Google Speech Recognition não conseguiu entender")
            except sr.RequestError as e:
                print("Não foi possivel adiquirir os dados do serviço do Google Speech Recognition; {0}".format(e))


        #--------- COM GOOGLE CLOUD ----------
        # recognize speech using Google Cloud Speech
            # try:
            #     trigger = microfone.recognize_google_cloud(audio, credentials_json= credenciais_google, language= 'pt-BR') # Converte o áudio capturado em texto
            #     trigger = trigger.lower() # Colocar tudo em minuscula
            #     if hotword in trigger: # Se o nome da assistente for chamado ele entrar na execução do comando
            #         print('Comando: ', trigger)
            #         responde('feedback')
            #         break

            # except sr.UnknownValueError:
            #     print("Audio não pode ser compreendido")
            # except sr.RequestError as e:
            #     print("Erro ao adquirir informações com servidor; {0}".format(e))
    return trigger

while True:
    monitora_audio()
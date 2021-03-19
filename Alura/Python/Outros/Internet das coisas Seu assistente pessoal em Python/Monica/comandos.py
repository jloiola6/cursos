from requests import get # Para fazer request de informações do site
from bs4 import BeautifulSoup # Para fazer o tratamento desses dados
from cria_audios import * # Importando função de criação de audios
import webbrowser as wb


def ultimas_noticias():
    site = get('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419') # Nós passamso um link em XML das noticias do google e salvamos na variavel site
    noticias = BeautifulSoup(site.text, 'html.parser') # Tratamso as informações do xml de acordo com tags html
    c = 1
    for i in noticias.findAll('item')[:5]: # Damos um for dos 5 primeiros dados de noticias da tag "item"
        mensagem = i.title.text # A mensagem recebe o titulo em forma de texto
        print(f'Noticia {c}: {mensagem}') # Printamos a noticia
        cria_audio(mensagem)
        c += 1

def playlist(album):
    if album == 'curtidas':
        wb.open('https://music.youtube.com/watch?v=KhZSUsz7Hkg&feature=share')

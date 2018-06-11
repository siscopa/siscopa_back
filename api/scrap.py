import requests
from bs4 import BeautifulSoup


class ScrapTimeCopa:

    def __init__(self):
        self.url = "https://sportv.globo.com/site/programas/copa-2018/noticia/confira-as-listas-dos-convocados-para-a-copa-do-mundo-2018.ghtml"
        self.response = requests.get(self.url)
        self.pagina = self.response.text
        self.soup = BeautifulSoup(self.pagina,"html.parser")
        self.tag_times = self.soup.find_all('blockquote')
        self.jogadores = self.soup.find_all("ul",class_="content-unordered-list")

    def get_goleiros(self):
        for i in range(0,len(self.tag_times)):
            print(self.tag_times[i].string)
            print(self.jogadores[i].li)

    def get_nome_time(self):
        for i in self.tag_times:
            return i.string

    def get_nome_jogadores(self):
        for i in self.jogadores:

            print(i)

    def principal(self):
        for i in range(0,len(self.tag_times)):
            print(self.tag_times[i].string)
            print(self.jogadores[i])

if __name__ == '__main__':
    objeto = ScrapTimeCopa()
    #objeto.get_nome_jogadores()
    #objeto.principal()
    objeto.get_goleiros()

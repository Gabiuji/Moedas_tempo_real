from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")


class MeuApp(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar R${self.pegarCotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R${self.pegarCotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.pegarCotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R${self.pegarCotacao('ETH')}"
        #return super().on_start()
    
    def pegarCotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        print(requisicao.json())
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao
    
MeuApp().run()
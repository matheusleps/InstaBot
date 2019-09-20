from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        self.cont = 0
        self.stopCont = 10
        self.numeroSeguidores = '0'
        self.codigoLocal = ''

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def encontrarFotos(self, tag):
        bot = self.bot
        time.sleep(2)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            foto = bot.find_elements_by_tag_name('a')
            links = [elem.get_attribute('href') for elem in foto]
        for i in range(13,30):
            bot.get(links[i])
            try:
                time.sleep(2)
                if ed.verificarLike() == False:
                    bot.find_element_by_class_name('fr66n').click() #curtir
                    time.sleep(2)
                if tag == seguirTag:
                    ed.verificarSeguindo()
                    time.sleep(2)
            except Exception as ex:
                time.sleep(6)
    
    def seguirSeguidores(self):
        bot = self.bot
        bot.get('https://www.instagram.com/'+self.username)
        time.sleep(2)
        elemento = bot.find_elements_by_tag_name('a')
        links = [elem.get_attribute('href') for elem in elemento]
        for i in range(len(links)):
            if links[i]=='https://www.instagram.com/'+ self.username +'/followers/':
                elemento[i].click()
                break
        time.sleep(4)
        bot2 = self.bot
        seguidores = bot2.find_elements_by_class_name('wo9IH')
        listaSeguidores = [seguidores.find_element_by_class_name('uu6c_') for seguidores in seguidores]
        listaBotaoSeguir = [listaSeguidores.find_element_by_class_name('Pkbci') for listaSeguidores in listaSeguidores]
        for listaBotaoSeguir in listaBotaoSeguir:
            if listaBotaoSeguir.find_element_by_tag_name('button').text == 'Seguir':
                listaBotaoSeguir.find_element_by_tag_name('button').click()
                time.sleep(1)

    def calcularSeguidores(self):
        bot = self.bot
        numeroSeguidores = bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
        if self.numeroSeguidores != numeroSeguidores:
            self.numeroSeguidores = numeroSeguidores
            print('--------------------------\nNúmero atual de seguidores: '+numeroSeguidores)

    def seguirIdeal(self):
        bot = self.bot
        bot.get('https://www.instagram.com/lpeventos08')
        time.sleep(2)
        elemento = bot.find_elements_by_tag_name('a')
        links = [elem.get_attribute('href') for elem in elemento]
        for i in range(len(links)):
            if links[i]=='https://www.instagram.com/lpeventos08/following/':
                elemento[i].click()
                
    def verificarLike(self):
        bot = self.bot
        botao = bot.find_element_by_class_name('fr66n')
        botao2 = botao.find_element_by_tag_name('button')
        botaoFinal = botao2.find_element_by_tag_name('span')
        if botaoFinal.get_attribute('class') == 'glyphsSpriteHeart__filled__24__red_5 u-__7':
            return True
        return False
    
    def buscarTag(self, tag):
        bot = self.bot
        bot.get('https://www.instagram.com/'+self.username)
        time.sleep(2)
        ed.calcularSeguidores()
        bot.get('https://www.instagram.com/explore/tags/'+tag)
        time.sleep(2)
        ed.encontrarFotos(tag)
    
    def verificarSeguindo(self):
        bot = self.bot
        if ed.cont<10:
            ed.cont = ed.cont+1
            bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[2]/button').click()
        else:
            ed.zerarCont()
    
    def zerarCont(self):
        self.stopCont = self.stopCont - 1
        if self.stopCont == 0:
            self.cont = 0
            self.stopCont = 10
    
    def getCodigoCidade(self, cidade):
        codigoCidades = ['213106903','405027146','248738611','112047398814697','213665608','221337983','8226756']
        return codigoCidades[cidade]


    def verificaCidade(self, tag):
        cidades = ['curitiba', 'riodejaneiro', 'parana', 'saopaulo','londrina','assis', 'maringa']
        for i in range(len(cidades)):
            if tag == cidades[i]:
                self.codigoLocal = ed.getCodigoCidade(i)
                return True
        return False

    def buscarLocalizacao(self, tag):
        bot = self.bot
        bot.get('https://www.instagram.com/'+self.username)
        time.sleep(2)
        ed.calcularSeguidores()
        bot.get('https://www.instagram.com/explore/locations/'+self.codigoLocal)
        time.sleep(2)
        ed.encontrarFotos(tag)



usuario = ''
senha = ''
print('Usuário:')
#usuario = input(usuario)
print('Senha:')
#senha = input(senha)
tags = [] 
tag = ''
print('PARA INICIAR A APLICAÇÃO DIGITE: start')
while True:
    print('Insira uma tag:')
    tag = ''
    tag = input(tag)    
    if tag == 'start':
        break
    tags.append(tag)  
seguirTag = 'nao seguir'
ed = InstagramBot(usuario,senha)
ed.login()
time.sleep(2)
while True:
    i=0
    for i in range(len(tags)):
        try:
            if ed.verificaCidade(tags[i]):
                ed.buscarLocalizacao(tags[i])
            else:
                ed.buscarTag(tags[i])
        except Exception as ex:
            ed.bot.get('https://www.instagram.com/'+usuario)
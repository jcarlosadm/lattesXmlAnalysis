# -*- coding: UTF-8 -*-
import Pesquisadores # recebe arquivo fonte Pesquisadores.py
import Relatorios # recebe arquivo fonte Relatorios.py

#=============================================================
#    *    Classe Analise_Xml
#-------------------------------------------------------------
#    Classe principal, recebe todas as outras classes
#
#    Objetos:
#    pesquisadores    :    lista todos os pesquisadores
#    relatorios        :    lista todos os relatorios
#
#    Métodos:
#    executar        :    executa o programa principal
#=============================================================

class Analise_Xmls(object):

    #---------------------------------------------------------
    #    Inicialização
    #---------------------------------------------------------
    
    def __init__(self):
        self.ano_inicial = 0
        self.ano_final = 0
        self.configurar_ano()
        self.pesquisadores = Pesquisadores.Pesquisadores()
        self.relatorios = Relatorios.Relatorios(self.ano_inicial,self.ano_final)
    
    #---------------------------------------------------------
    #    configura ano inicial e final
    #---------------------------------------------------------
    
    def configurar_ano(self):
        # abre arquivo de configuração
        arquivo = open('init.txt','r')
        # faz busca das configurações no arquivo aberto
        linha = arquivo.readline()
        while(linha!=''):
            # se a linha for referente ao ano inicial das publicações, atribui à constante relacionada
            if('ano inicial das publicacoes' in linha):
                self.ano_inicial = int(linha.split(' : ')[1])
            # se a linha for referente ao ano final das publicações, atribui à constante relacionada
            elif('ano final das publicacoes' in linha):
                self.ano_final = int(linha.split(' : ')[1])
            linha = arquivo.readline()
        # fecha arquivo de configuração
        arquivo.close()
    
    #---------------------------------------------------------
    #    Executa o programa principal
    #---------------------------------------------------------
    
    def update(self):
        self.pesquisadores.update(self.ano_inicial,self.ano_final,self.relatorios)
        self.relatorios.update(self.ano_inicial,self.ano_final,self.pesquisadores)

#=============================================================
#    Execução principal
#=============================================================

programa = Analise_Xmls();
programa.update();

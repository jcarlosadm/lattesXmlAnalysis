# -*- coding: UTF-8 -*-
from xml.dom import minidom # para explorar arquivos xml
import os # para explorar os sistemas de arquivos e pastas
import operator # para ordenar listas de objetos de acordo com o atributo dos mesmos
import Pesquisador

#=============================================================
#	*	Classe Pesquisadores
#-------------------------------------------------------------
#	Classe que gerencia todos os professores
#
#	Propriedades:
#	pesquisadores	:	array de objetos da classe Pesquisador
#=============================================================

class Pesquisadores(object):
	
	#---------------------------------------------------------
	#	Inicialização
	#---------------------------------------------------------
	
	def __init__(self):
		self.pesquisadores = []
		
		self.terminaContagem = False
		self.contarCurriculos = 0
		self.arquivoXml = ""
	
	#---------------------------------------------------------
	#	Atualização
	#---------------------------------------------------------
	
	def update(self,ano_inicial,ano_final,relatorios):
		
		# analisa pasta padrão em busca de curriculos
		self.analisa_pasta(ano_inicial,ano_final,relatorios)
	
	#---------------------------------------------------------
	#		Analisa pasta padrão em busca de curriculos em
	#	formato xml na ordem numérica
	#---------------------------------------------------------
	
	def analisa_pasta(self,ano_inicial,ano_final,relatorios):
	
		# verifica próximo curriculo
		self.verifica_proximo_curriculo()
		
		while(not(self.terminaContagem)):
			# pega o nome do curriculo do arquivo xml aberto
			nomeDoArquivo = self.arquivoXml.getElementsByTagName('DADOS-GERAIS')
			nomeDoArquivo = nomeDoArquivo[0].attributes['NOME-COMPLETO'].value
			
			# controla se usa lattes para um novo pesquisador
			usarLattes = True
			
			# verifica se ja existe algum pesquisador com o mesmo nome
			# se existir, nao usa esse lattes aberto
			if(self.pesquisador_ja_existe(nomeDoArquivo)):
				usarLattes = False
			
			# se o lattes aberto puder ser usado...
			if(usarLattes):
				# adiciona ao relatorio de lista de curriculos
				relatorios.adicionar_lista_curriculos(nomeDoArquivo,self.contarCurriculos,False)
				
				# adiciona pesquisador
				self.adiciona_pesquisador(nomeDoArquivo,relatorios,ano_inicial,ano_final)
				
			else:
				# adiciona ao relatório de lista de curriculos e informa repetição
				relatorios.adicionar_lista_curriculos(nomeDoArquivo,self.contarCurriculos,True)
			
			# verifica próximo curriculo
			self.verifica_proximo_curriculo()
		
		# ordena lista de pesquisadores de acordo com os seus nomes
		self.pesquisadores.sort(key=operator.attrgetter('nome'))
	
	#---------------------------------------------------------
	#	Verifica a existência do próximo curriculo
	#---------------------------------------------------------
	
	def verifica_proximo_curriculo(self):
		# Se o curriculo existir, abre
		if(os.path.exists('curriculos/curriculo ('+str(self.contarCurriculos+1)+").xml")):
			self.contarCurriculos += 1
			self.arquivoXml = minidom.parse('curriculos/curriculo ('+str(self.contarCurriculos)+').xml')
			self.terminaContagem = False
		# caso contrario, nem inicializa
		else:
			self.terminaContagem = True
	
	#---------------------------------------------------------
	#	Adiciona pesquisador
	#---------------------------------------------------------
	
	def adiciona_pesquisador(self,nomeDoArquivo,relatorios,ano_inicial,ano_final):
		self.pesquisadores.append(Pesquisador.Pesquisador(nomeDoArquivo,self.arquivoXml,self.pesquisadores,relatorios,
									ano_inicial,ano_final))
	
	#---------------------------------------------------------
	#	Verifica se o pesquisador já existe
	#---------------------------------------------------------
	
	def pesquisador_ja_existe(self,nomeDoArquivo):
		# verifica se ja existe algum pesquisador com o mesmo nome
		for pesquisador in self.pesquisadores:
			# se existir retorna True
			if(pesquisador.nome == nomeDoArquivo):
				return True
		# Caso não exista, retorna False
		return False


# -*- coding: UTF-8 -*-

class Relatorios(object):
	def __init__(self, ano_inicial, ano_final):
		self.lista_curriculos_por_nome = []
		self.lista_curriculos_por_curriculo = []
		self.contagem = {
        "Artigos_completos_publicados_em_periodicos":{},
        "Livros_e_capitulos_de_livros_publicados":{},
        "Textos_em_jornais_e_noticias_revistas":{},
        "Trabalhos_completos_publicados_em_anais_de_congresso":{},
        'Apresentacoes_de_trabalhos':{},
        'Resumos_publicados_em_anais_de_congresso':{},
        'Acessorias_consultorias_e_outros_trabalhos_tecnicos':{},
        'Outras_producoes_bibliograficas':{}
		}
		self.inicializar_contagem(ano_inicial,ano_final)
	
	def inicializar_contagem(self,ano_inicial,ano_final):
		for ano in range(ano_inicial,ano_final+1):
			# fazer um for key in self.contagem
			self.contagem['Artigos_completos_publicados_em_periodicos'][ano]=0
			self.contagem["Livros_e_capitulos_de_livros_publicados"][ano]=0
			self.contagem["Textos_em_jornais_e_noticias_revistas"][ano]=0
			self.contagem["Trabalhos_completos_publicados_em_anais_de_congresso"][ano]=0
			self.contagem['Apresentacoes_de_trabalhos'][ano]=0
			self.contagem['Resumos_publicados_em_anais_de_congresso'][ano]=0
			self.contagem['Acessorias_consultorias_e_outros_trabalhos_tecnicos'][ano]=0
			self.contagem['Outras_producoes_bibliograficas'][ano]=0
	
	def adicionar_lista_curriculos(self,nomePesquisador,sequencia,repetido=False):
		frase_repetido = ""
		if(repetido):
			frase_repetido = " repetido!!"
		
		self.lista_curriculos_por_nome.append(nomePesquisador+" = curriculo ("+str(sequencia)+").xml"+frase_repetido)
		self.lista_curriculos_por_curriculo.append("curriculo ("+str(sequencia)+").xml = "+nomePesquisador+frase_repetido)
		
	def update(self,ano_inicial,ano_final,pesquisadores):
		self.escrever_lista_curriculos()
		self.escrever_contagem_geral(ano_inicial,ano_final)
		self.escrever_relatorio_detalhado(ano_inicial,ano_final,pesquisadores)
	
	def escrever_lista_curriculos(self):
		# abre arquivo de texto que relaciona arquivos xml e os nomes dos pesquisadores
		listagem_xml = open("relatorios/_lista_curriculos_xml.txt","w")
		# ordena a lista
		self.lista_curriculos_por_nome.sort()
		self.lista_curriculos_por_curriculo.sort()
		# escreve cada um no arquivo aberto
		listagem_xml.write("Ordenados pelos arquivos xml:\n")
		for item in self.lista_curriculos_por_curriculo:
			listagem_xml.write("  "+item.encode('iso8859-1')+"\n")
		listagem_xml.write("\nOrdenados pelos nomes dos pesquisadores:\n")
		for item in self.lista_curriculos_por_nome:
			listagem_xml.write("  "+item.encode('iso8859-1')+"\n")
		#fecha arquivo
		listagem_xml.close()
	
	def escrever_contagem_geral(self,ano_inicial,ano_final):
		# abre o arquivo contagem
		contagem = open("relatorios/contagens.txt","w")

		# escreve Artigos completo publicados em periodicos
		self.escrever_trecho_contagem('Artigos_completos_publicados_em_periodicos',
										'Artigos completos publicados em periodicos',contagem,ano_inicial,ano_final)
		# escreve livros e capítulos de livros publicados
		self.escrever_trecho_contagem('Livros_e_capitulos_de_livros_publicados',
										'Livros e Capitulos de livros publicados',contagem,ano_inicial,ano_final)
		# escreve textos em jornais e revistas
		self.escrever_trecho_contagem('Textos_em_jornais_e_noticias_revistas',
										"Textos em jornais e revistas publicados",contagem,ano_inicial,ano_final)
		# escreve trabalhos completos publicados em anais de congresso
		self.escrever_trecho_contagem('Trabalhos_completos_publicados_em_anais_de_congresso',
										'Trabalhos completos publicados em anais de congresso',contagem,ano_inicial,ano_final)
		# escreve apresentações de trabalhos em congressos
		self.escrever_trecho_contagem('Apresentacoes_de_trabalhos',
										'Apresentações de Trabalhos',contagem,ano_inicial,ano_final)
		# escreve resumos publicados em anais de congresso
		self.escrever_trecho_contagem('Resumos_publicados_em_anais_de_congresso',
										"Resumos publicados em anais de congresso",contagem,ano_inicial,ano_final)
		# escreve acessorias, consultorias e demais tipos de trabalhos técnicos
		self.escrever_trecho_contagem('Acessorias_consultorias_e_outros_trabalhos_tecnicos',
										'Acessorias, consultorias e demais tipos de trabalhos técnicos',contagem,ano_inicial,ano_final)
		# escreve outras produções bibliográficas
		self.escrever_trecho_contagem('Outras_producoes_bibliograficas',
										'Outras produções bibliográficas',contagem,ano_inicial,ano_final)
    
		# fecha o arquivo contagem
		contagem.close()
		
	def escrever_trecho_contagem(self,tipo_producao,titulo,arq_contagem,ano_inicial,ano_final):
		arq_contagem.write('\n'+titulo+'\n')
		for ano in range(ano_inicial,ano_final+1):
			arq_contagem.write(str(ano)+": "+str(self.contagem[tipo_producao][ano])+"\n")
	
	def escrever_relatorio_detalhado(self,ano_inicial,ano_final,pesquisadores):
		# abre relatorio
		relatorio = open("relatorios/relatorio_detalhado.txt","w")

		# escreve artigos completos publicados em periodicos
		self.escrever_trecho_relatorio(relatorio,pesquisadores,'Artigos_completos_publicados_em_periodicos',
											'Artigos completos publicados em periodicos',ano_inicial,ano_final)
		# livros e capítulos de livros publicados
		self.escrever_trecho_relatorio(relatorio,pesquisadores,'Livros_e_capitulos_de_livros_publicados',
											'Livros e Capitulos de livros publicados',ano_inicial,ano_final)
		# textos em jornais e revistas
		self.escrever_trecho_relatorio(relatorio,pesquisadores,'Textos_em_jornais_e_noticias_revistas',
											"Textos em jornais e revistas publicados",ano_inicial,ano_final)
		# trabalhos completos publicados em anais de congresso
		self.escrever_trecho_relatorio(relatorio,pesquisadores,"Trabalhos_completos_publicados_em_anais_de_congresso",
											"Trabalhos completos publicados em anais de congresso",ano_inicial,ano_final)
		# apresentação de trabalhos
		self.escrever_trecho_relatorio(relatorio,pesquisadores,'Apresentacoes_de_trabalhos',
											'Apresentações de Trabalhos',ano_inicial,ano_final)
		# resumos publicados em anais de congresso
		self.escrever_trecho_relatorio(relatorio,pesquisadores,"Resumos_publicados_em_anais_de_congresso",
											'Resumos publicados em anais de congresso',ano_inicial,ano_final)
		# Acessorias, consultorias e demais trabalhos técnicos
		self.escrever_trecho_relatorio(relatorio,pesquisadores,"Acessorias_consultorias_e_outros_trabalhos_tecnicos",
											"Acessorias, consultorias e demais trabalhos técnicos",ano_inicial,ano_final)
		# Outras produções bibliográficas
		self.escrever_trecho_relatorio(relatorio,pesquisadores,"Outras_producoes_bibliograficas",
											"Outras produções bibliográficas",ano_inicial,ano_final)

		# fecha relatorio
		relatorio.close()
		 
	def escrever_trecho_relatorio(self,relatorio,pesquisadores,tipo_producao,titulo,ano_inicial,ano_final):
		relatorio.write("\n========================================================================")
		relatorio.write('\n'+titulo+':\n')
		for pesquisador in pesquisadores.pesquisadores:
			escrever_nome=True
			for ano in range(ano_inicial,ano_final+1):
				if(len(pesquisador.publicacoes[tipo_producao][ano])>0):
					if(escrever_nome):
						relatorio.write("\n  "+pesquisador.nome.encode('iso8859-1')+"\n")
						escrever_nome=False
					relatorio.write("    "+str(ano)+"\n")
				for producao in pesquisador.publicacoes[tipo_producao][ano]:
					relatorio.write("       "+str(producao.encode('iso8859-1'))+"\n")

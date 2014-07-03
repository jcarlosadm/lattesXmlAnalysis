# -*- coding: UTF-8 -*-

#=============================================================
#    *    Classe Pesquisador
#-------------------------------------------------------------
#    Classe que armazena dados dos pesquisadores
#
#    Propriedades:
#=============================================================

class Pesquisador(object):
    def __init__(self,nome,arquivoXML,pesquisadores,relatorios,ano_inicial,ano_final):
        self.nome = nome
        self.publicacoes = {"Artigos_completos_publicados_em_periodicos":{},"Livros_e_capitulos_de_livros_publicados":{},"Textos_em_jornais_e_noticias_revistas":{},'Trabalhos_completos_publicados_em_anais_de_congresso':{},'Apresentacoes_de_trabalhos':{},'Resumos_publicados_em_anais_de_congresso':{},'Acessorias_consultorias_e_outros_trabalhos_tecnicos':{},'Outras_producoes_bibliograficas':{}}
        
        self.inicializar_publicacoes(ano_inicial,ano_final)
        
        # artigos completos publicados em periodicos do pesquisador
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DO-ARTIGO','NATUREZA','COMPLETO',
                                    'ANO-DO-ARTIGO','TITULO-DO-ARTIGO','Artigos_completos_publicados_em_periodicos')
        # livros e capitulos de livros publicados
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DO-LIVRO','TIPO','LIVRO-PUBLICADO',
                                    'ANO','TITULO-DO-LIVRO','Livros_e_capitulos_de_livros_publicados')
        # capítulos de livros publicados
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DO-CAPITULO','TIPO','Capítulo de livro publicado',
                                    'ANO','TITULO-DO-CAPITULO-DO-LIVRO','Livros_e_capitulos_de_livros_publicados')
        # textos em revistas
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DO-TEXTO','NATUREZA','REVISTA_MAGAZINE',
                                    'ANO-DO-TEXTO','TITULO-DO-TEXTO','Textos_em_jornais_e_noticias_revistas')
        # textos em jornais
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DO-TEXTO','NATUREZA','JORNAL_DE_NOTICIAS',
                                    'ANO-DO-TEXTO','TITULO-DO-TEXTO','Textos_em_jornais_e_noticias_revistas')
        # trabalhos completos publicados em congresso
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DO-TRABALHO',"NATUREZA",'COMPLETO',
                                    'ANO-DO-TRABALHO','TITULO-DO-TRABALHO','Trabalhos_completos_publicados_em_anais_de_congresso')
        # apresentações de trabalho em congressos
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DA-APRESENTACAO-DE-TRABALHO',"","",
                                    'ANO','TITULO','Apresentacoes_de_trabalhos')
        # resumos expandidos publicados em anais de congressos
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DO-TRABALHO','NATUREZA','RESUMO_EXPANDIDO',
                                    'ANO-DO-TRABALHO','TITULO-DO-TRABALHO','Resumos_publicados_em_anais_de_congresso')
        # resumos publicados em anais de congresso
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DO-TRABALHO','NATUREZA','RESUMO',
                                    'ANO-DO-TRABALHO','TITULO-DO-TRABALHO','Resumos_publicados_em_anais_de_congresso')
        # resumos publicados em anais de congresso (artigos)
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DO-ARTIGO','NATUREZA','RESUMO',
                                    'ANO-DO-ARTIGO','TITULO-DO-ARTIGO','Resumos_publicados_em_anais_de_congresso')
        # Acessorias, consultorias e trabalhos técnicos
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DO-TRABALHO-TECNICO','','','ANO','TITULO-DO-TRABALHO-TECNICO'
                                    ,'Acessorias_consultorias_e_outros_trabalhos_tecnicos')
        # Cursos de curta duração ministrados
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DE-CURSOS-CURTA-DURACAO-MINISTRADO','','',
                                    'ANO','TITULO','Acessorias_consultorias_e_outros_trabalhos_tecnicos')
        # Outras produções técnicas
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DE-OUTRA-PRODUCAO-TECNICA','','',
                                    'ANO','TITULO','Acessorias_consultorias_e_outros_trabalhos_tecnicos')
        # Demais trabalhos
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DE-DEMAIS-TRABALHOS','','',
                                    'ANO','TITULO','Acessorias_consultorias_e_outros_trabalhos_tecnicos')
        # Outras produções bibliográficas
        self.processar_producao(ano_inicial,ano_final,arquivoXML,pesquisadores,relatorios,
                                    'DADOS-BASICOS-DE-OUTRA-PRODUCAO','','','ANO','TITULO','Outras_producoes_bibliograficas')
        
    def inicializar_publicacoes(self,ano_inicial,ano_final):
        for ano in range(ano_inicial,ano_final+1):
            # usar for key in self.publicações
            self.publicacoes['Artigos_completos_publicados_em_periodicos'][ano] = []
            self.publicacoes['Livros_e_capitulos_de_livros_publicados'][ano]=[]
            self.publicacoes["Textos_em_jornais_e_noticias_revistas"][ano]=[]
            self.publicacoes["Trabalhos_completos_publicados_em_anais_de_congresso"][ano]=[]
            self.publicacoes['Apresentacoes_de_trabalhos'][ano]=[]
            self.publicacoes['Resumos_publicados_em_anais_de_congresso'][ano]=[]
            self.publicacoes['Acessorias_consultorias_e_outros_trabalhos_tecnicos'][ano]=[]
            self.publicacoes['Outras_producoes_bibliograficas'][ano]=[]
        
    def processar_producao(self,ano_inicial,ano_final,arquivoXml,pesquisadores,relatorios,nome_tag,
                            atributo_filtro_item,valor_atributo_item,atributo_ano_item,atributo_titulo_item,
                            tipo_producao,filtro_adicional=False,tipo_filtro_adiconal=''):

        itens = arquivoXml.getElementsByTagName(nome_tag)
        for ano in range(ano_inicial,ano_final+1):
            for item in itens:

                if(filtro_adicional):
                    item = item.getElementsByTagName(tipo_filtro_adiconal)[0]

                if(atributo_filtro_item==''):
                    atributo = True
                else:
                    atributo = (item.attributes[atributo_filtro_item].value.encode('iso8859-1')==valor_atributo_item)

                if(atributo and item.attributes[atributo_ano_item].value==str(ano)):
                    if(self.producao_exclusiva(item.attributes[atributo_titulo_item].value,tipo_producao,ano,pesquisadores)):
                        relatorios.contagem[tipo_producao][ano]+=1
                    self.publicacoes[tipo_producao][ano].append(item.attributes[atributo_titulo_item].value)

            self.publicacoes[tipo_producao][ano].sort()
            
    def producao_exclusiva(self,titulo,tipo_producao,ano,pesquisadores):
        for pesquisador in pesquisadores:
            for publicacao in (pesquisador.publicacoes[tipo_producao][ano]):
                if(titulo == publicacao):
                    return False # nao e exlusiva
        return True # é exclusiva

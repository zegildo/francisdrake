#coding: utf-8
"""
Author: ZéGildo (zegildo@gmail.com)
---------------
This crawler get all information (siape, name, departament, photo and
personal link) about special professors in
https://sigaa.ufersa.edu.br/sigaa/public/docente/busca_docentes.jsf

"""
import grequests
from lxml import html
import sys

def get_clean_name(name):
    '''Normalize strings and remove initinal and final spaces

    Returns:
        A printable name
    '''
    return name.encode('utf-8').decode().strip()

def get_reitoria_siapes():
    '''
    Dean, Vice Dean and other professors linked to the actual 
    manangement are not listed on departament's page

    https://reitoria.ufersa.edu.br/equipe/
        # Jose De Arimatea De Matos - 336632
        # Jose Domingues Fontenele Neto - 1181653
        # Felipe De Azevedo Silva Ribeiro - 1670609
    '''
    siapes_reitoria = [336632, 1181653, 1670609]
    return siapes_reitoria

def get_pro_reitores_siapes():
    '''
    Deans of undergradate studies, and other professors linked 
    to the actual manangement are not listed on departament's page

    #Pro-Reitorias

    #https://ufersa.edu.br/proreitorias/

    #https://proae.ufersa.edu.br/equipe/
        # Vânia Christina Nascimento Porto - 1714179

    #https://proec.ufersa.edu.br/equipe-da-proec
        # Rodrigo Sergio Ferreira De Moura - 1545235
        # Almir Mariano De Sousa Junior - 2079536
    
    #https://progepe.ufersa.edu.br/
        # Alexandre Jose De Oliveira - 1677881

    #https://prograd.ufersa.edu.br/equipe/
        # Rodrigo Nogueira De Codes - 1806868
        # Jose Erimar Dos Santos - 1243118

    #https://proppg.ufersa.edu.br/equipe/
        # Jean Berg Alves Da Silva - 2359110
        # Vander Mendonca - 1547955

    #https://proplan.ufersa.edu.br/
        # Alvaro Fabiano Pereira De Macedo - 1500639
        # Moacir Franco De Oliveira - 2206331

    #There are not professors in PROAD
    #https://proad.ufersa.edu.br/equipe-proad/
    '''
    pro_reitores = [
    1714179, 1545235, 2079536, 1677881, 1806868, 
    1243118, 2359110, 1547955, 1500639, 2206331] 
    return pro_reitores


def get_diretores_siapes():
    '''
    # https://sigaa.ufersa.edu.br/sigaa/public/academico/busca_responsavel.jsf

    # CENTRO DE CIÊNCIAS BIOLÓGICAS E DA SAÚDE    
        #RODRIGO SILVA DA COSTA - 1574667

    #CENTRO DE CIÊNCIAS EXATAS E NATURAIS    
        #RAFAEL CASTELO GUEDES MARTINS - 2752035

    #CENTRO DE CIÊNCIAS SOCIAIS APLICADAS E HUMANAS  
        #LUDIMILLA CARVALHO SERAFIM DE OLIVEIRA - 1781560

    #CENTRO DE ENGENHARIAS   
        #ALAN MARTINS DE OLIVEIRA - 1802972

    #CAMPUS ANGICOS  
        #ARAKEN DE MEDEIROS SANTOS - 1631848

    #CAMPUS CARAUBAS 
        #DANIEL FREITAS FREIRE MARTINS - 1813593

    #CAMPUS PAU DOS FERROS
        #RICARDO PAULO FONSECA MELO - 1991824
    '''
    diretores = [
    1574667, 2752035, 1781560, 1802972, 
    1631848, 1813593, 1991824]
    return diretores

def get_special_professors_siapes():
    '''
    Get the siapes of the special professors who aren't listed
    on the departament's list.
    '''
    special_siapes = []

    special_siapes.extend(get_reitoria_siapes())
    special_siapes.extend(get_pro_reitores_siapes())
    special_siapes.extend(get_diretores_siapes())
    return special_siapes

def print_list_special_professors():
    '''Print the information (siape, name, depart., photo_link, personal_page)
    about all SPECIAL professors in UFERSA
    '''
    URL = 'https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape='
    URL_BASE = "https://sigaa.ufersa.edu.br"


    siapes = get_special_professors_siapes()
    urls = [URL+str(siape) for siape in siapes ]
    rs = (grequests.get(u) for u in urls)
    responses = grequests.map(rs)
    
    i = 0
    for r in responses:
        pg_prof = html.fromstring(r.text)
        nome = pg_prof.xpath('//div[@class="barra_professor"]/h3/text()')[0]
        nome = get_clean_name(nome)
        dep = pg_prof.xpath('//h3[@class="departamento"]/text()')[0]
        dep = get_clean_name(dep)
        ft = pg_prof.xpath('//div[@class="foto_professor"]/img/@src')[0]
        ft = URL_BASE+ft
        siape = siapes[i]
        pg = urls[i]
        print(f'{siape}, "{nome}", "{dep}", "{ft}", "{pg}"')
        i = i+1

print_list_special_professors()

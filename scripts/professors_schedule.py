#coding: utf-8
"""
Author: ZéGildo (zegildo@gmail.com)
---------------

Catching the professors schedule at UFERSA is an annoying task.
We should to stalk more than 700 personal links, copy and paste
each detail over many semesters.

To solve this I developed this web crawler that collect the class
schedule historical for each UFERSA Professor during all his
professor carrer.

"""
import sys
import requests
from lxml import html

def print_schedule_class(nivel):
    """Get the schedule class present in nivel.

    Args:
        nivel: A lxml Element containing the information
        view (https://lxml.de/api/lxml.etree._Element-class.html).

    Returns:
        A line with part of the schedule class historical. For example:
        -------
        111111,turmas-graduacao,2018.1,PAC0864,ESPAÇO E FORMA,60h,6M2345
    """
    nivel_id = nivel.get('id')
    ano_periodo = ''
    codigo_disciplina = ''
    nome_disciplina = ''
    carga_horaria = ''
    horario = ''
    for element in nivel.iter():
        if element.tag == 'td':
            classe = element.get('class')
            if classe == 'anoPeriodo':
                ano_periodo = clean_string(element.text)
            elif classe == 'codigo':
                codigo_disciplina = clean_string(element.text)
            elif classe == 'ch':
                carga_horaria = clean_string(element.text)
            elif classe == 'horario':
                horario = clean_string(element.text)
                print '{0},"{1}","{2}","{3}","{4}","{5}","{6}"'.format(SIAPE,
                                                                       nivel_id,
                                                                       ano_periodo,
                                                                       codigo_disciplina,
                                                                       nome_disciplina,
                                                                       carga_horaria,
                                                                       horario)
        elif element.tag == 'a':
            nome_disciplina = clean_string(element.text)

def clean_string(string):
    """Get a clean version of a string

    Args:
        A string that should be cleaned
    Returns:
        A clean version of a string
    """
    new_string = string.encode('utf-8').strip()
    return new_string

def buil_schedule_professors(url):
    """Get the schedule class from the personal link
    of a UFERSA's professor

    Args:
        url: A personal link to a professor's schedule.

    Returns:
        Multiple lines with the class schedule historical
        of a professor: For example:

        url = 'https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1111111'

        output:
        -------
        111111,turmas-graduacao,2018.1,PAC0864,ESPAÇO E FORMA,60h,6M2345
        111111,turmas-graduacao,2018.1,PSH1601,GEOMETRIA DESCRITIVA,60h,4T2345
        111111,turmas-graduacao,2018.1,PSH1600,OFICINA DE PLÁSTICA I,60h,6M2345
        111111,turmas-graduacao,2018.1,PAC0861,PLANEJAMENTO DA PAISAGEM I,60h,6N1234
    """
    response = requests.get(url)
    hrs = html.fromstring(response.text)
    niveis = hrs.xpath('//div[@class="aba"]')
    for nivel in niveis:
        print_schedule_class(nivel)
#This code should be execute in terminal like:
#cat siapes | time parallel -j+0 --progress python professors_schedule.py {} > horarios.csv
if __name__ == "__main__":

    SIAPE = sys.argv[1]
    URL = 'https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape='
    try:
        buil_schedule_professors(URL+SIAPE)
    except:
        print(SIAPE)
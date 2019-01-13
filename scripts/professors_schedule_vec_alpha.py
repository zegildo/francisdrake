#coding: utf-8
"""
Author: ZéGildo (zegildo@gmail.com)
---------------

Catching the professors schedule at UFERSA is a annoying task.
We should to stalk more than 700 personal links, copy and paste
each detail over many semesters.

To solve this I developed this web crawler that collect the class
schedule historical for each UFERSA Professor during all his
professor carrer.

"""
import sys
import requests
from lxml import html

def buil_schedule_class_professor(url):
    """Get the schedule class from the personal link
    of a UFERSA's professor

    Args:
        url: A personal link to a professor's schedule.

    Returns:
        Multiple lines with the class schedule historical
        of a professor: For example:

        url = 'https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3049977'

        output:
        -------
        3049977,turmas-graduacao,2018.1,PAC0864,ESPAÇO E FORMA,60h,6M2345
        3049977,turmas-graduacao,2018.1,PSH1601,GEOMETRIA DESCRITIVA,60h,4T2345
        3049977,turmas-graduacao,2018.1,PSH1600,OFICINA DE PLÁSTICA I,60h,6M2345
        3049977,turmas-graduacao,2018.1,PAC0861,PLANEJAMENTO DA PAISAGEM I,60h,6N1234

    Raises:
        #TODO this method

    """

    response = requests.get(url)
    hrs = html.fromstring(response.text)
    niveis = hrs.xpath('//div[@class="aba"]/@id | //td/text() | //td/a/text()')
    niveis = [e.strip() for e in niveis if e.strip()]
    limit = 0
    periodo = ''
    turma = ''
    while limit < (len(niveis)):
        horario = []
        if 'turmas-' in niveis[limit]:
            turma = niveis[limit]
            limit = limit + 1
        elif '.' in niveis[limit]:
            periodo = niveis[limit]
            horario.append(turma)
            horario.extend(niveis[limit:limit+CONST_PASSO+1])
            print ','.join(horario).encode('utf-8').strip()
            horario = []
            limit = limit + CONST_PASSO + 1
        else:
            horario.append(turma)
            horario.append(periodo)
            horario.extend(niveis[limit:limit+CONST_PASSO])
            print ','.join(horario).encode('utf-8').strip()
            horario = []
            limit = limit + CONST_PASSO

#This code should be execute in terminal like:
#cat Desktop/siapes | time parallel -j+0 --progress python professors_schedule.py {} > horarios.csv_file
if __name__ == "__main__":

    SIAPE = sys.argv[1:][0]
    CONST_PASSO = 4
    URL = 'https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape='
    buil_schedule_class_professor(URL+SIAPE)

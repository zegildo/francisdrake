#coding: utf-8
"""

cat Desktop/siapes |
time parallel -j+0 
--progress python Desktop/professors_schedule.py {} > Desktop/horarios.csv_file
"""
import requests
from lxml import html
import sys

def buil_schedule_ufersa_professors(URL):

    r = requests.get(URL)
    hrs = html.fromstring(r.text)
    niveis = hrs.xpath('//div[@class="aba"]/@id | //td/text() | //td/a/text()')
    niveis = [e.strip() for e in niveis if e.strip()]
    
    PASSO = 4
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
            horario.extend(niveis[limit:limit+PASSO+1])
            print ','.join(horario).encode('utf-8').strip()
            horario = []
            limit = limit + PASSO + 1
        else:
            horario.append(turma)
            horario.append(periodo)
            horario.extend(niveis[limit:limit+PASSO])
            print ','.join(horario).encode('utf-8').strip()
            horario = []
            limit = limit + PASSO
            
if __name__ == "__main__":

    siape = sys.argv[1:][0]
    URL = 'https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape='
    buil_schedule_ufersa_professors(URL+siape)
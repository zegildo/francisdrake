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
    '''    
    r = requests.get(URL)
    r.raw.chunked = True
    hrs = html.fromstring(r.text)
    niveis = hrs.xpath('//div[@class="aba"]')
    
    for nv in niveis:
        nivel = nv.get('id')
        ano_periodo = ''
        codigo_disciplina = ''
        nome_disciplina=''
        carga_horaria = ''
        horario = ''

        for el in nv.iter():
            if el.tag == 'td':
                classe = el.get('class') 
                if classe == 'anoPeriodo':
                    ano_periodo = el.text.strip()
                elif classe == 'codigo':
                    codigo_disciplina = el.text.strip()
                elif classe == 'ch':
                    carga_horaria = el.text.strip()
                elif classe == 'horario':
                    horario = el.text.strip()
                    print (siape,nivel,ano_periodo,
                            codigo_disciplina,nome_disciplina,
                            carga_horaria,horario)
            elif el.tag == 'a':
                     nome_disciplina = el.text.strip()
    '''
if __name__ == "__main__":

    siape = sys.argv[1:][0]
    URL = 'https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape='
    buil_schedule_ufersa_professors(URL+siape)
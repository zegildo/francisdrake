#coding: utf-8
"""
Author: ZéGildo (zegildo@gmail.com)
---------------
This crawler get all information (siape, name, departament, photo and
personal link) about professors in
https://sigaa.ufersa.edu.br/sigaa/public/docente/busca_docentes.jsf

"""

import sys

def update_siapes(siapes_coletados):

    with open('inputs/siapes') as siapes:
        set_siapes_atuais = set([linha.strip() for linha in siapes])
    set_siapes_coletados = set([s.strip() for s in siapes_coletados])
    set_novos_siapes = set_siapes_coletados - set_siapes_atuais
    print("Novos siapes:")
    for i in set_novos_siapes:
        print(i)
    merge_siapes = set_siapes_atuais.union(set_siapes_coletados)
    with open('inputs/siapes', 'w') as siapes:
        siapes.write('\n'.join(merge_siapes))

if __name__ == "__main__":
    data = sys.stdin.readlines()
    update_siapes(data)
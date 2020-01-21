#coding: utf-8
"""
Author: ZéGildo (zegildo@gmail.com)
---------------
This crawler get all information (siape, name, departament, photo and
personal link) about professors in
https://sigaa.ufersa.edu.br/sigaa/public/docente/busca_docentes.jsf

"""
import sys
import grequests
from lxml import html

def get_session():
    '''Get a request's session

    Returns:
        A session (grequests API) with all information
        session inside the object
    '''
    session = grequests.Session()
    return session

def get_view_state(session):
    '''Extract the view state information inside the page.
    This information is necessary to autenticate the request
    in the server.

    Returns:
        The view state information that will be pass on the
        post request.
    '''
    response = session.get(URL)
    body = html.fromstring(response.text)
    view_state = body.xpath('//input[@id="javax.faces.ViewState"]/@value')[0]
    return view_state

def get_ufersa_departament_page(departament):
    '''Send a post request

    Returns:
        A response to the post request
    '''
    session = get_session() #it is necessary for jsession on server.
    view_state = get_view_state(session)
    params = {'form': 'form',
              'form:nome':'',
              'form:departamento':departament,
              'form:buscar':'Buscar',
              'javax.faces.ViewState':view_state}
    response = session.post(URL, data=params)
    return response

def get_siape_professors(link_pages):
    '''Extract siape number inside the link_pages

    Returns:
        An array with siapes numbers
    '''
    position = 1
    siapes = [int(link.split('=')[position]) for link in link_pages]
    return siapes

def agg_info_url_base(url_base, incomplete_links):
    '''Aggregate a fixed url with additional information

    Returns:
        An array with personal urls
    '''
    complet_links = [url_base+i for i in incomplete_links]
    return complet_links

def get_clean_names(names):
    '''Normalize strings and remove initinal and final spaces

    Returns:
        An array with printable names
    '''
    clean_names = [name.encode('utf-8').decode().strip() for name in names]
    return clean_names

def print_list_ufersa_professors(departament):
    '''Print the information (siape, name, depart., photo_link, personal_page)
    about all professors in UFERSA
    '''
    response = get_ufersa_departament_page(departament)
    departament_page = html.fromstring(response.text)
    nomes = departament_page.xpath('//span[@class="nome"]/text()')
    nomes = get_clean_names(nomes)
    departamentos = departament_page.xpath('//span[@class="departamento"]/text()')
    departamentos = get_clean_names(departamentos)
    fotos = departament_page.xpath('//td[@class="foto"]/img/@src')
    fotos = agg_info_url_base(URL_BASE, fotos)
    paginas = departament_page.xpath('//span[@class="pagina"]/a/@href')
    paginas = agg_info_url_base(URL_BASE, paginas)
    siapes = get_siape_professors(paginas)
    for siape, nome, dep, ft, pg in zip(siapes, nomes, departamentos, fotos, paginas):
        print(f'{siape}, "{nome}", "{dep}", "{ft}", "{pg}"')

#This code should be execute in terminal like:
#cat siapes | time parallel -j+0 --progress python professors_information.py {} > professors_information.csv
if __name__ == "__main__":

    URL = "https://sigaa.ufersa.edu.br/sigaa/public/docente/busca_docentes.jsf"
    URL_BASE = "https://sigaa.ufersa.edu.br"
    DEPART = sys.argv[1:][0]
    print_list_ufersa_professors(DEPART)

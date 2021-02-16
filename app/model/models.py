from app import app
from app import db

'''
Arquivo contendo as tabelas de pessoa e sala para a criação do banco de 
dados.
'''

class Pessoa(db.Model):
    '''Tabela Pessoa

    Cria a tabela Pessoa no banco de dados e salva os dados.

    Atributes
    ---------
    id : int
        id auto-incrementado

    nome : str
        nome da pessoa
    
    Methods
    -------
    def create(pessoa=None):
        Cria uma nova Pessoa no banco
    
    def save():
        Salva as novas informações da Pessoa no banco de dados
    '''

class Sala(db.Model):
    '''Tabela Sala

    Cria a tabela Pessoa no banco de dados e salva os dados.

    Atributes
    ---------
    nome : str
        nome da sala
    
    lotacao : str
        capacidade de pessoas na sala

    Methods
    -------
    def create(sala=None):
        Cria uma nova pessoa no banco

    def save():
        Salva as novas informações da Sala no banco de dados
    '''
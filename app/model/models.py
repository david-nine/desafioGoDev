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
        id da pessoa auto-incrementado

    nome : str
        nome da pessoa
    
    salas : list
        salas relacionadas a Pessoa

    etapa1 : str
        sala da etapa 1

    etapa2 : str
        sala da etapa 2

    cafe1 : str
        sala pro café da etapa 1

    cafe2 : str
        sala pro café da etapa 2

    Methods
    -------
    def create(pessoa=None):
        Cria uma nova Pessoa no banco
    
    def save():
        Salva as novas informações da Pessoa no banco de dados
    '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    etapa1 = db.Column(db.String(200), nullable=True)
    etapa2 = db.Column(db.String(200), nullable=True)
    cafe1 = db.Column(db.String(200), nullable=True)
    cafe2 = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"EmpresaModel('{self.id}', '{self.nome}', '{self.sobrenome}',\
                              '{self.etapa1}', '{self.etapa2}', '{self.cafe1}',\
                              '{self.cafe3}')"  

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
    nome = db.Column(db.String(200), primary_key=True)
    lotacao = db.Column(db.Integer, nullable=True)
    
    def __repr__(self):
        return f"EmpresaModel('{self.nome}', '{self.lotacao}')"
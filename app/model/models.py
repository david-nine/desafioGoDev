from app import app
from app import db

'''
Arquivo contendo as tabelas de pessoa e sala para a criação do banco de 
dados.
'''

pessoas1 = db.Table('pessoas1',
    db.Column('pessoa_id', db.Integer, db.ForeignKey('pessoa.id'), primary_key=True),
    db.Column('etapa1_nome', db.String(200), db.ForeignKey('sala.nome'), primary_key=True),
)
pessoas2 = db.Table('pessoas2',
    db.Column('pessoa_id', db.Integer, db.ForeignKey('pessoa.id'), primary_key=True),
    db.Column('etapa2_nome', db.String(200), db.ForeignKey('sala.nome'), primary_key=True),
)

class Pessoa(db.Model):
    '''Tabela Pessoa

    Cria a tabela Pessoa no banco de dados e salva os dados.

    Atributes
    ---------
    id : int
        id da pessoa auto-incrementado

    nome : str
        nome da pessoa
    
    sobrenome : str
        sobrenome da pessoa

    Methods
    -------
    def save():
        Salva as novas informações da Pessoa no banco de dados
    '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200), nullable=False)
    sobrenome = db.Column(db.String(200), nullable=False)
    
    
    def __repr__(self):
        return f"Pessoa('{self.id}', '{self.nome}', '{self.sobrenome}')"

class Sala(db.Model):
    '''Tabela Sala

    Cria a tabela Sala no banco de dados e salva os dados.

    Atributes
    ---------
    nome : str
        nome da sala
    
    lotacao : str
        capacidade de pessoas na sala

    pessoas1 : list
        lista de pessoas na sala durante a primeira etapa
    
    pessoas2 : list
        lista de pessoas na sala durante a segunda etapa
    
    Methods
    -------
    def save():
        Salva as novas informações da Sala no banco de dados
    '''
    nome = db.Column(db.String(200), primary_key=True)
    lotacao = db.Column(db.Integer, nullable=True)
    pessoas1 = db.relationship('Pessoa', secondary=pessoas1, lazy='subquery', 
                             backref=db.backref('pessoas1', lazy=True))
    pessoas2 = db.relationship('Pessoa', secondary=pessoas2, lazy='subquery', 
                             backref=db.backref('pessoas2', lazy=True))           

    def __repr__(self):
        return f"Sala('{self.nome}', '{self.lotacao}')"

    def save(self):
        '''Salva as novas informações da Sala no banco de dados
        '''
        db.session.merge(self)
        db.session.commit()
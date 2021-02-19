from app import app
from app import db

'''
Arquivo contendo as tabelas de pessoa e sala para a criação do banco de 
dados.
'''

pessoas = db.Table('pessoas',
    db.Column('pessoa_id', db.Integer, db.ForeignKey('pessoa.id'), primary_key=True),
    db.Column('sala_nome', db.String(200), db.ForeignKey('sala.nome'), primary_key=True),
)
pessoas2 = db.Table('pessoas2',
    db.Column('pessoa_id', db.Integer, db.ForeignKey('pessoa.id'), primary_key=True),
    db.Column('sala_nome', db.String(200), db.ForeignKey('sala.nome'), primary_key=True),
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
    def create(pessoa=None):
        Cria uma nova Pessoa no banco
    
    def save():
        Salva as novas informações da Pessoa no banco de dados
    '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200), nullable=False)
    sobrenome = db.Column(db.String(200), nullable=False)
    
    
    def __repr__(self):
        return f"Pessoa('{self.id}', '{self.nome}', '{self.sobrenome}')"

    def save(self):
        db.session.merge(self)
        db.sessin.commit()
    
    def create(self, pessoa):
        db.session.add(pessoa)
        db.session.commit()


class Sala(db.Model):
    '''Tabela Sala

    Cria a tabela Sala no banco de dados e salva os dados.

    Atributes
    ---------
    nome : str
        nome da sala
    
    lotacao : str
        capacidade de pessoas na sala

    etapa1 : list
        lista de pessoas na sala durante a primeira etapa
    
    etapa2 : list
        lista de pessoas na sala durante a segunda etapa
    
    Methods
    -------
    def create(sala=None):
        Cria uma nova pessoa no banco

    def save():
        Salva as novas informações da Sala no banco de dados
    '''
    nome = db.Column(db.String(200), primary_key=True)
    lotacao = db.Column(db.Integer, nullable=True)
    etapa1 = db.relationship('Pessoa', secondary=pessoas, lazy='subquery', 
                             backref=db.backref('salas1', lazy=True))
    etapa2 = db.relationship('Pessoa', secondary=pessoas2, lazy='subquery', 
                             backref=db.backref('salas2', lazy=True))           

    def __repr__(self):
        return f"Sala('{self.nome}', '{self.lotacao}')"

    def save(self):
        db.session.merge(self)
        db.session.commit()
    
    def create(self, sala):
        db.session.add(sala)
        db.session.commit()




# class SalaCafe(db.Model):
#     '''Tabela SalaCafe

#     Cria a tabela Sala no banco de dados e salva os dados.

#     Atributes
#     ---------
#     nome : str
#         nome da sala
    
#     Methods
#     -------
#     def create(salacafe=None):
#         Cria uma nova SalaCafe no banco

#     def save():
#         Salva as novas informações da SalaCafe no banco de dados
#     '''
#     nome = db.Column(db.String(200), primary_key=True)
#     # pessoas1 = db.relationship('Pessoa', backref='pessoacafe1', lazy=True)
#     # pessoas2 = db.relationship('Pessoa', backref='pessoacafe2', lazy=True)
#     # etapa1 = db.Column(db.Integer, db.ForeignKey('pessoa.id'),
#     #                    nullable=True)
#     etapa2 = db.Column(db.Integer, db.ForeignKey('pessoa.id'),
#                        nullable=True)

#     def __repr__(self):
#         return f"SalaCafe('{self.nome}','{self.etapa1}', '{self.etapa2}')"

#     def save(self):
#         db.session.merge(self)
#         db.sessin.commit()
    
#     def create(self, salacafe):
#         db.session.add(salacafe)
#         db.session.commit()
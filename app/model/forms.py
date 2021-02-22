from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, ValidationError
from app import db
from app.model.models import Sala, Pessoa

'''
Arquivo contendo os formulários
'''

class FormPessoa(FlaskForm):
    '''Formulário para cadastro de Pessoa
    
    Atributes
    ---------
    nome : str
        nome da pessoa

    sobrenome : str
        sobrenome da pessoa
    '''
    nome = StringField("Nome", validators=[InputRequired("Informe o\
                                                          nome da pessoa")])
    sobrenome = StringField("Sobrenome", 
                            validators=[InputRequired("Informe o sobrenome\
                                                       da pessoa")])
    submit = SubmitField("Confirmar")

    def validate_nome(self, nome):
        if not Sala.query.all():
            raise ValidationError('Não existem salas')
        if len(Sala.query.all()) < 2:
            raise ValidationError('Não há salas suficientes para o\
                                    cadastro de pessoas')
    

class FormSala(FlaskForm):
    '''Formulário para cadastro de Sala

    nome : str
        nome da sala

    lotacao : int
        capacidade de lotação da sala

    Methods
    -------
    def validate_nome(nome=None):
        verifica se ja existe uma sala com esse nome
    '''
    nomesala = StringField("Nome", validators=[InputRequired("Informe um\
                                                          nome para a sala")])

    lotacao = IntegerField("Lotação",
                           validators=[InputRequired('Informe a lotação\
                                                      máxima da sala')])
    submit = SubmitField("Confirmar")

    def validate_nomesala(self, nomesala):
        if Sala.query.filter_by(nome=nomesala.data).first():
            raise ValidationError('Já existe uma sala com este nome')

class FormCafe(FlaskForm):
    '''Formulário para cadastro de Sala de café

    nome : str
        nome da sala
    
    Methods
    -------
    def validate_nome(nome=None):
        verifica se já existe uma sala com esse nome
    '''
    nomecafe = StringField("Nome", validators=[InputRequired("Informe um \
                                                          nome para a sala")])
    submit = SubmitField("Confirmar")
    def validate_nomecafe(self, nomecafe):
        if Sala.query.filter_by(nome=nomecafe.data).first():
            raise ValidationError('Já existe uma sala com este nome')

class FormPesquisa(FlaskForm):
    '''Formulário para Pesquisa de Sala

    nome : str
        nome da sala
    
    Methods
    -------
    def validate_nome(nome=None):
        Verifica se essa sala existe
    '''
    nomepesquisa = StringField(validators=[InputRequired("Informe o nome da sala")])
    buscar = SubmitField("Buscar Sala")

    def validate_nomepesquisa(self, nomepesquisa):
        if not Sala.query.filter_by(nome=nomepesquisa.data).first():
            raise ValidationError('Esta sala não existe')
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, ValidationError
from app import db
from app.model.models import Sala

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
    nome = StringField("Nome", validators=[InputRequired("Informe um \
                                                          nome para a sala")])

    lotacao = IntegerField("Lotação",
                           validators=[InputRequired('Informe a lotação\
                                                      máxima da sala')])
    def validate_nome(self):
        if Sala.query.filter_by(nome=nome).first():
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
    nome = StringField("Nome", validators=[InputRequired("Informe um \
                                                          nome para a sala")])

    def validate_nome(self):
        if Sala.query.filter_by(nome=nome).first():
            raise ValidationError('Já existe uma sala com este nome')
from app import app
from app.model.models import Pessoa, Sala
from app.model.forms import FormSala, FormPessoa, FormCafe

'''
Comunicação entra as rotas e os models
'''
class DAO():
    '''Data Access Object
    
    A classe DAO faz o tratamento de dados vindo do routes.py e envia
    parra o models.py.

    Methods
    -------
    def cadastrar_pessoa(form=None):
        Cadastra uma nova pessoa.

    def cadastrar_sala(form):
        Cadastra uma nova sala.

    def cadastra_cafe(form):
        Cadastra uma nova sala de café.
    
    def pesquisa_sala(form):
        Pesquisa a sala desejada no banco.
    
    def pesquisa_aluno(id):
        Pesquisa o aluno desejado no banco.

    def organizar_pessoas():
        Faz a divisão das pessoas nas salas para as duas etapas e salva
        no banco
    '''
    def cadastrar_pessoa(self, form):
        nova_pessoa = Pessoa(nome=form.nome.data,
                             sobrenome=form.nome.data)
        Pessoa.create(nova_pessoa)
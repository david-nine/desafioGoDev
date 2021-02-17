from app import app
from app.model.models import Pessoa, Sala
from app.model.forms import FormSala, FormPessoa, FormCafe, FormPesquisa

'''
Comunicação entra as rotas e os models
'''
class DAO:
    '''Data Access Object
    
    A classe DAO faz o tratamento de dados vindo do routes.py e envia
    parra o models.py.

    Methods
    -------
    def cadastrar_pessoa(form=None):
        Cadastra uma nova pessoa.

    def cadastrar_sala(form):
        Cadastra uma nova sala.
    
    def pesquisa_sala(form):
        Pesquisa a sala desejada no banco.
    
    def pesquisa_pessoa(id):
        Pesquisa o aluno desejado no banco.

    def organizar_pessoas():
        Faz a divisão das pessoas nas salas para as duas etapas e salva
        no banco
    '''

    def cadastrar_pessoa(self, form):
        '''Cadastra uma Pessoa nova no banco a partir dos dados passados
        pelo form
        
        Parameters
        ----------
        form : FlaskForm
            formulário FormPessoa com os dados da pessoa que vai ser 
            cadastrada
        '''
        print(form.nome.data)
        nova_pessoa = Pessoa(nome=form.nome.data,
                             sobrenome=form.nome.data)
        Pessoa.create(nova_pessoa)

    def cadastrar_sala(self, form):
        '''Cadastra uma Sala nova no banco a partir dos dados passados
        pelo form

        Parameters
        ----------
        form : FlaskForm
            formulário FormSala ou FormCafe com os dados da Sala que vai ser 
            cadastrada
        '''
        if type(form.lotacao.data) == int:
            nova_sala = Sala(nome=form.nome.data,
                             lotacao=form.lotacao.data)
        else:
            nova_sala = Sala(nome=form.nome.data)
        Sala.create(nova_sala)

    def pesquisa_sala(self, form):
        '''Pesquisa a Sala com o nome passado pelo form

        Parameters
        ----------
        form : FlaskForm
            formulário FormCafe com o nome da sala procurada
        '''
        sala = Sala.query.filter_by(nome=form.nome.data).first()
        return sala

    def pesquisa_pessoa(self, id):
        '''Pesquisa a Pessoa a partir do id

        Parameters
        ----------
        id : int
            id da pessoa procurada
        '''
        pessoa = Pessoa.query.get(id)
        return pessoa

    def organizar_pessoas(self):
        '''Faz a divisão das pessoas nas salas

        Faz uma lista com todos as pessoas e vai adicionando uma por vez
        em uma das salas de forma que as salas fiquem com o mesmo número
        de pessoas ou no máximo uma a mais. 
        '''
        pessoas = Pessoa.query.all()
        salas = Sala.query.all()
        for i in range(0, len(quant_pessoas), 3):
            for count in range(len(salas)):
                pessoa = pessoas[i+count]
                pessoa.nome = salas[count].nome
                pessoa.save()
    
    def getPessoasSala(self, sala):
        '''Pega todas as pessoas da sala desejada e separa em duas listas,
        uma da primeira etapa e outra da segunda.

        Parameters
        ----------
        sala : str
            nome da sala
        '''
        pessoas = Pessoa.query.all()
        etapa1 = []
        etapa2 = []
        for pessoa in pessoas:
            if pessoa.etapa1 == sala:
                etapa1.append(pessoa)
            elif pessoa.etapa2 == sala:
                etapa2.append(pessoa)
        return (etapa1, etapa2)
                 
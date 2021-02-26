from app import app
from app import db
from app.model.models import Pessoa, Sala
from app.model.forms import FormSala, FormPessoa, FormPesquisa

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

    def cadastrar_sala(form=None):
        Cadastra uma nova sala.

    def cadastrar_salacafe(form=None):
        Cadastra um novo espaço para café
    
    def pesquisa_sala(form=None):
        Pesquisa a sala desejada no banco.
    
    def pesquisa_pessoa(id=None):
        Pesquisa o aluno desejado no banco.

    def organizar_pessoas():
        Faz a divisão das pessoas nas salas para as duas etapas e salva
        no banco

    def busca_pessoas():
        busca todas as pessoas do banco

    def create(objeto=None):
        Cria uma nova linha no banco na tabela do objeto passado
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
        nova_pessoa = Pessoa(nome=form.nome.data,
                             sobrenome=form.sobrenome.data)
        self.create(nova_pessoa)
        

    def cadastrar_sala(self, form):
        '''Cadastra uma Sala nova no banco a partir dos dados passados
        pelo form

        Parameters
        ----------
        form : FlaskForm
            formulário FormSala ou FormCafe com os dados da Sala que vai ser 
            cadastrada
        '''
        nova_sala = Sala(nome=form.nomesala.data, lotacao=form.lotacao.data)
        self.create(nova_sala)
        

    def cadastrar_salacafe(self, form):
        '''Cadastra uma SalaCafe nova no banco a partir dos dados passados
        pelo form

        Parameters
        ----------
        form : FlaskForm
            formulário FormCafe com os dados da SalaCafe que vai ser 
            cadastrada
        '''
        nova_sala = Sala(nome=form.nomecafe.data)
        self.create(nova_sala)

    def pesquisa_sala(self, nome):
        '''Pesquisa a Sala pelo nome

        Parameters
        ----------
        nome : str
            nome da sala pesquisada
        '''
        sala = Sala.query.filter_by(nome=nome).first()
        return sala

    def pesquisa_pessoa(self, id):
        '''Pesquisa a uma Pessoa a partir do id

        Parameters
        ----------
        id : int
            id da pessoa procurada
        '''
        pessoa = Pessoa.query.filter_by(id=id).first()
        return pessoa

    def busca_pessoas(self):
        '''Busca e retorna todas as pessoas cadastradas no banco
        '''
        return Pessoa.query.all()

    def create(self, objeto):
        '''Cria uma nova linha na tabela do objeto desejado apartir dos 
        dados passados pelo objeto.

        Parameters
        ----------
        objeto : Object
            objeto do tipo Pessoa ou Sala 
        '''
        db.session.add(objeto)
        db.session.commit()

    def organizar_pessoas(self):
        '''Faz a divisão das pessoas nas salas

        Faz uma lista com todos as pessoas e vai adicionando uma por vez
        em uma das salas de forma que as salas fiquem com o mesmo número
        de pessoas ou no máximo uma a mais. 
        '''
        pessoas = self.busca_pessoas()
        if pessoas:
            salascafe = Sala.query.filter_by(lotacao=None).all()
            salas = Sala.query.all()
            salas_certo = []
            for sala in salas:
                if sala.lotacao != None:
                    salas_certo.append(sala)  
            
            for sala in salas_certo:
                sala.pessoas1 = []
                sala.pessoas2 = []
                sala.save()
            
            for sala in salascafe:
                sala.pessoas1 = []
                sala.pessoas2 = []
                sala.save()

            i = 0
            for pessoa in pessoas:
                if i == (len(salas_certo)):
                    i = 0
                if salas_certo[i].lotacao == len(salas_certo[i].pessoas1):
                    i +=1
                    if i == len(salas_certo):
                        i = 0
                salas_certo[i].pessoas1.append(pessoa)
                salas_certo[i].save()
                i += 1
            
            i = 0
            for pessoa in pessoas:
                if i == (len(salascafe)):
                    i = 0
                if salascafe[i].lotacao == len(salascafe[i].pessoas1):
                    i +=1
                    if i == len(salascafe):
                        i = 0
                salascafe[i].pessoas1.append(pessoa)
                salascafe[i].save()
                i += 1

            count = 0
            i = 0 
            for pessoa in pessoas:
                if i == (len(salas_certo)):
                    i = 0
                if salas_certo[i].lotacao == len(salas_certo[i].pessoas2):
                    i +=1
                    if i == len(salas_certo):
                        i = 0 
                if count >= len(pessoas)//2:
                    if count == len(pessoas)//2:
                        i += 1
                    if i == (len(salas_certo)):
                        i = 0                   
                    salas_certo[i].pessoas2.append(pessoa)
                else:
                    salas_certo[i].pessoas2.append(pessoa)
                salas_certo[i].save()
                count += 1
                i += 1
            
            
            i = 1
            for pessoa in pessoas:
                if i == (len(salascafe)):
                    i = 0
                if salascafe[i].lotacao == len(salascafe[i].pessoas2):
                    i +=1
                    if i == len(salascafe):
                        i = 0
                salascafe[i].pessoas2.append(pessoa)
                salascafe[i].save()
                i += 1
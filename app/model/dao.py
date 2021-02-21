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
        nova_sala = Sala(nome=form.nome.data, lotacao=form.lotacao.data)
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
        nova_sala = Sala(nome=form.nome.data)
        self.create(nova_sala)

    def pesquisa_sala(self, nome):
        '''Pesquisa a Sala com o nome passado pelo form

        Parameters
        ----------
        form : FlaskForm
            formulário FormCafe com o nome da sala procurada
        '''
        sala = Sala.query.filter_by(nome=nome).first()
        return sala

    def pesquisa_pessoa(self, id):
        '''Pesquisa a Pessoa a partir do id

        Parameters
        ----------
        id : int
            id da pessoa procurada
        '''
        pessoa = Pessoa.query.filter_by(id=id).first()
        return pessoa

    def busca_salas_da_pessoa(self, pessoa):
        salas = Sala.query.with_parent(pessoa)
        return salas

    def busca_pessoas(self):
        return Pessoa.query.all()

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()

    def organizar_pessoas(self):
        '''Faz a divisão das pessoas nas salas

        Faz uma lista com todos as pessoas e vai adicionando uma por vez
        em uma das salas de forma que as salas fiquem com o mesmo número
        de pessoas ou no máximo uma a mais. 
        '''
        pessoas = Pessoa.query.all()
        if pessoas:
            salascafe = Sala.query.filter_by(lotacao=None).all()
            salas = Sala.query.all()
            salas_certo = []
            for sala in salas:
                if sala.lotacao != None:
                    salas_certo.append(sala)  

            # for sala in salas_certo:
            #     sala.etapa1 = []
            #     sala.etapa2 = []
            #     sala.save()
            
            # for sala in salascafe:
            #     sala.etapa1 = []
            #     sala.etapa2 = []
            #     sala.save()

            i = 0
            for pessoa in pessoas:
                if i == (len(salas_certo)):
                    i = 0
                salas_certo[i].etapa1.append(pessoa)
                salas_certo[i].save()
                i += 1

            i = 1
            count = 0
            for pessoa in pessoas:
                i2 = i - 1
                if i == 0:
                    i2 = len(salas_certo)
                if i == (len(salas_certo)):
                    i = 0
                if count == 1:
                    salas_certo[i].etapa2.append(pessoa)
                    salas_certo[i].save()
                else:
                    salas_certo[i2].etapa2.append(pessoa)
                    salas_certo[i2].save()
                i += 1
                if count == 0:
                    count = 1
                else:
                    count = 0
            
            i = 0
            for pessoa in pessoas:
                if i == (len(salascafe)):
                    i = 0
                salascafe[i].etapa1.append(pessoa)
                salascafe[i].save()
                i += 1

            i = 1
            count = 0
            for pessoa in pessoas:
                i2 = i - 1
                if i == 0:
                    i2 = len(salascafe)
                if i == (len(salascafe)):
                    i = 0
                if count == 1:
                    salascafe[i].etapa2.append(pessoa)
                    salascafe[i].save()
                else:
                    salascafe[i2].etapa2.append(pessoa)
                    salascafe[i2].save()
                i += 1
                if count == 0:
                    count = 1
                else:
                    count = 0

            print(salas_certo[1].etapa1)
            print(salascafe[1].etapa1) 
            print(salas_certo[1].etapa2)
            print(salascafe[1].etapa2)
            
            print("----------------------")
            # i = 0
            # count = 0
            # for pessoa in pessoas:
            #     print("i = ", i)
            #     print("i2 = ", i2)
            #     i2 = i+1
            #     print("alooooooooooo", len(salas_certo))
            #     if i == (len(salas_certo)-1):
            #         i2 = 0
            #     if count == 0:
            #         salas_certo[i2].etapa1.append(pessoa)
            #         salas_certo[i2].save()
            #         salas_certo[i].etapa2.append(pessoa)
            #         salas_certo[i].save()
            #         salascafe[i].etapa2.append(pessoa)
            #         salascafe[i].save()
            #         salascafe[i2].etapa1.append(pessoa)
            #         salascafe[i2].save()
            #         i += 1
            #         if i2 == 0:
            #             i = 0
            #     if count == 0:
            #         count = 1
            #     else:
            #         count = 0
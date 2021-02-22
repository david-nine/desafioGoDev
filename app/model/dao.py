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
            
            i = 0
            for pessoa in pessoas:
                if i == (len(salascafe)):
                    i = 0
                salascafe[i].etapa1.append(pessoa)
                salascafe[i].save()
                i += 1

            count = 0
            i = 0 
            for pessoa in pessoas:
                if i == (len(salascafe)):
                    i = 0
                if count > len(pessoas)/2:
                    if count == len(pessoas):
                        i += 1
                        if i == (len(salascafe)):
                            i = 0
                        salascafe[i].etapa2.append(pessoa)
                else:
                    salascafe[i].etapa2.append(pessoa)
                salascafe[i].save()
                count += 1
                i += 1

            count = 0
            i = 0 
            for pessoa in pessoas:
                if i == (len(salas_certo)):
                    i = 0
                if count > len(pessoas)/2:
                    if count == len(pessoas):
                        i += 1
                        if i == (len(salas_certo)):
                            i = 0
                        salas_certo[i].etapa2.append(pessoa)
                else:
                    salas_certo[i].etapa2.append(pessoa)
                salas_certo[i].save()
                count += 1
                i += 1
            # salas_cafe_troca = []
            # salas_cafe_fica = []
            # quant = len(salascafe) // 2
            # for i in range(quant):
            #     salas_cafe_troca.append(salascafe[i])
            # quant = len(salascafe) - quant
            # for i in range(quant, quant*2): 
            #     salas_cafe_fica.append(salascafe[i])
           
            # quant = len(pessoas) // 2
            # i = 0
            # count = 0
            # while count < quant:
            #     if i == (len(salas_cafe_troca)):
            #         i = 0
            #     print(len(salas_cafe_troca))
            #     salas_cafe_troca[i].etapa2.append(pessoas[count])
            #     salas_cafe_troca[i].save()
            #     count += 1
            #     i += 1

            # i = 1
            # quant = len(pessoas) - quant
            # while count < quant:
            #     if i == (len(salas_cafe_fica)):
            #         i = 0
            #     salas_cafe_fica[i].etapa2.append(pessoas[count])
            #     salas_cafe_fica[i].save()
            #     count += 1
            #     i += 1

            # salas_troca = []
            # salas_troca = []
            # quant = len(salas_certo) // 2
            # for i in range(quant):
            #     salas_troca.append(salas_certo[i])
            # quant = len(salas_certo) - quant
            # for i in range(quant, quant*2): 
            #     salas_troca.append(salas_certo[i])
           
            # quant = len(pessoas) // 2
            # i = 0
            # count = 0
            # while count < quant:
            #     if i == (len(salas_troca)):
            #         i = 0
            #     salas_troca[i].etapa2.append(pessoas[count])
            #     salas_troca[i].save()
            #     count += 1
            #     i += 1

            # i = 1
            # quant = len(pessoas) - quant
            # while count < quant:
            #     if i == (len(salas_troca)):
            #         i = 0
            #     salas_troca[i].etapa2.append(pessoas[count])
            #     salas_troca[i].save()
            #     count += 1
            #     i += 1
from app import app
from app.model.models import Pessoa, Sala, SalaCafe
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
        nova_pessoa = Pessoa(nome=form.nome.data,
                             sobrenome=form.sobrenome.data)
        nova_pessoa.create(nova_pessoa)
        

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
        nova_sala.create(nova_sala)
        

    def cadastrar_salacafe(self, form):
        '''Cadastra uma SalaCafe nova no banco a partir dos dados passados
        pelo form

        Parameters
        ----------
        form : FlaskForm
            formulário FormCafe com os dados da SalaCafe que vai ser 
            cadastrada
        '''
        nova_sala = SalaCafe(nome=form.nome.data)
        nova_sala.create(nova_sala)

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
        pessoa = Pessoa.query.get(id)
        salas = [Sala.query.with_parent(pessoa1)]
        salas.append(Sala.query.with_parent(some_pessoa2))
        salascafe = [SalaCafe.query.with_parent(some_pessoa3)] 
        salascafe.append([SalaCafe.query.with_parent(some_pessoa4)])
        return (pessoa, salas, salascafe)

    def busca_pessoas(self):
        return Pessoa.query.all()

    def organizar_pessoas(self, tipo):
        '''Faz a divisão das pessoas nas salas

        Faz uma lista com todos as pessoas e vai adicionando uma por vez
        em uma das salas de forma que as salas fiquem com o mesmo número
        de pessoas ou no máximo uma a mais. 
        '''
        lista_pessoas = Pessoa.query.all()

        if tipo == 'sala':
            lista_salas = Sala.query.all()    
        elif tipo == 'cafe':
            lista_salas = SalaCafe.query.all()
            
        quant_salas = len(lista_salas)
        quant_pessoas = len(lista_pessoas)
        val_for = quant_pessoas // quant_salas
        resto = quant_pessoas % quant_salas
        for sala in lista_salas:
            sala.pessoa1 = []
            sala.save()
        for count in range(0, val_for, quant_salas):
            for i in range(len(lista_salas)):
                sala = lista_salas[i]
                pessoa = lista_pessoas[i+count]
                sala.pessoas1.append(pessoa)
        
             
        
        
                    
        
        # for i in range(0, (len(lista_pessoas)//2), len(lista_salas)):
        #     for count in range(len(lista_salas)):
        #         lista_salas[count].etapa1.append(lista_pessoas[i+count])
        # for i in range(0, (len(pessoas)//2), len(lista_salascafe)):
        #     for count in range(len(lista_salascafe)):
        #         lista_salas[count].etapa1.append(lista_pessoas[i+count])
        # for i in range(0, (len(pessoas)//2), len(lista_salas)):
        #     for count in range(len(lista_salas)):
        #         lista_salas[count].etapa2.append(lista_pessoas[i+count])
        # for i in range(0, (len(pessoas)//2), len(lista_salascafe)):
        #     for count in range(len(lista_salascafe)):
        #         lista_salas[count].etapa2.append(lista_pessoas[i+count])
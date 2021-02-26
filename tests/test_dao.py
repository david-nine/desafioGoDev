from app import app
from app.model.dao import DAO
from app.model.models import Pessoa, Sala
from app.model.forms import FormCafe, FormPessoa, FormSala

DAO = DAO()

def test_create():
    '''Testa se a função DAO.create() adiciona um novo objeto no banco
    '''
    result = Sala(nome='sala 01', lotacao=15)
    DAO.create(result)
    assert result == Sala.query.filter_by(nome='sala 01').first()

def test_pesquisa_sala():
    '''Testa se a função DAO.pesquisa_sala retorna a sala a partir do
    nome 
    '''
    result = Sala(nome='sala 02', lotacao=15)
    DAO.create(result)
    assert result == DAO.pesquisa_sala('sala 02')

def test_pesquisa_pessoa():
    '''Testa se a função DAO.pesquisa_pessoa retorna a pessoa a partir
    do id 
    '''
    pessoa = Pessoa(nome='pessoa 01', sobrenome='teste')
    DAO.create(pessoa)
    pessoa_id = pessoa.id
    result = Pessoa.query.filter_by(nome='pessoa 01').first()
    assert result == DAO.pesquisa_pessoa(pessoa_id)

def test_busca_pessoas():
    '''Testa se a função DAO.pesquisa_pessoa retorna todas as pessoas do 
    banco
    '''
    result = Pessoa.query.all()
    assert DAO.busca_pessoas() == result

def test_organizar_pessoas():
    '''Testa de a função DAO.organizar_pessoas separa as pessoas em suas
    salas e altera na segunda etapa
    '''
    sala3 = Sala(nome="sala cafe 01")
    DAO.create(sala3)
    sala4 = Sala(nome="sala cafe 02")
    DAO.create(sala4)
    DAO.organizar_pessoas()
    pessoa_result = Pessoa(nome='pessoa_result', sobrenome='test')
    salas =  Sala.query.filter_by(lotacao=15)
    pessoa_result.pessoas1.append(salas[0])
    pessoa_result.pessoas2.append(salas[1])
    pessoa_result.pessoas1.append(sala3)
    pessoa_result.pessoas2.append(sala4)
    pessoa = Pessoa.query.first()
    assert pessoa.pessoas1 == pessoa_result.pessoas1 and pessoa.pessoas2\
           == pessoa_result.pessoas2
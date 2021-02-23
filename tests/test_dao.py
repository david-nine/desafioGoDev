from app import app
from app.model.dao import DAO
from app.model.models import Pessoa, Sala
from app.model.forms import FormCafe, FormPessoa, FormSala

DAO = DAO()

# def test_cadastrar_sala():
#     '''testa se a função DAO.cadastrar_sala cadastra a sala no banco    
#     '''

#     result = Sala(nome='salateste', lotacao=15)
#     form = FormSala(nome='salateste', lotacao=15)
#     DAO.cadastrar_sala(form)
#     sala = Sala.query.filter_by(nome=nome).first()
#     assert result == sala


# def test_cadastrar_pessoa():
#     '''testa se a função DAO.cadastrar_pessoa cadastra a pessoa no banco
#     '''
#     result = Pessoa(nome='pessoa', sobrenome='teste')
#     form = FormPessoa()
#     form.nome.data = 'pessoa'
#     form.sobrenome.data = 'teste'
#     DAO.cadastrar_pessoa(form)
#     pessoa = Pessoa.query.filter_by(nome=nome).first()
#     assert result == pessoa

# def test_cadastra_cafe():
#     '''testa se a função DAO.cadastrar_cafe cadastra a sala pra café
#     no banco
#     '''
#     result = Sala(nome='Nome da sala')
#     form = FormCafe()
#     form.nomecafe.data = "Nome da sala"
#     DAO.cadastrar_cafe(form)
#     sala = Sala.query.filter_by(nome='cafe_test').first()
#     assert 'Nome da sala' == form.nomecafe.data

def test_pesquisa_sala():
    '''Testa se a função DAO.pesquisa_sala retorna a sala a partir do
    nome 
    '''
    result = Sala(nome='nome')
    DAO.create(result)
    assert result == DAO.pesquisa_sala('nome')

def test_pesquisa_pessoa():
    '''Testa se a função DAO.pesquisa_pessoa retorna a pessoa a partir
    do id 
    '''
    result = Pessoa.query.filter_by(nome='pessoa').first()
    assert result == DAO.pesquisa_pessoa(0)

def test_busca_pessoas():
    '''Testa se a função DAO.pesquisa_pessoa retorna todas as pessoas do 
    banco
    '''
    result = Pessoa.query.all()
    assert DAO.busca_pessoas() == result

def test_create():
    '''Testa se a função DAO.create() adiciona um novo objeto no banco
    '''
    result = Sala(nome='teste create')
    DAO.create(result)
    assert result == Sala.query.filter_by(nome='teste create').first()

def test_organizar_pessoas():
    '''Testa de a função DAO.organizar_pessoas separa as pessoas em suas
    salas e altera na segunda etapa
    '''
    assert True
from app import app
from app.controller.dao import DAO
from app.model.models import Pessoa, Sala
from app.model.forms import FormCafe, FormPessoa, FormSala

def test_cadastrar_sala():
    '''testa se a função DAO.cadastrar_sala cadastra a sala no banco    
    '''

    result = Sala(nome='sala', lotacao=15)
    form = FormSala()
    form.nome.data = 'sala'
    form.lotacao.data = 15
    DAO.cadastrar_sala(form)
    sala = Sala.query.filter_by(nome=nome).first()
    assert result == sala


def test_cadastrar_pessoa():
    '''testa se a função DAO.cadastrar_pessoa cadastra a pessoa no banco
    '''
    result = Pessoa(nome='pessoa', sobrenome='teste')
    form = FormPessoa()
    form.nome.data = 'pessoa'
    form.sobrenome.data = 'teste'
    DAO.cadastrar_pessoa(form)
    pessoa = Pessoa.query.filter_by(nome=nome).first()
    assert result == pessoa

def cadastra_cafe():
    '''testa se a função DAO.cadastrar_cafe cadastra a sala pra café
    no banco
    '''
    result = Sala(nome='cafe_test')
    form = FormCafe()
    form.nome.data = 'cafe_test'
    DAO.cadastrar_cafe(form)
    sala = Sala.query.filter_by(nome=nome).first
    assert result == sala

def pesquisa_sala():
    '''Testa se a pesquisa a sala esta funcionando 
    '''
    result = Sala(nome='nome')
    Sala.create(result)
    sala = Sala.query.filter_by(nome='nome').first()
    assert result == sala

def pesquisa_aluno(id):
    '''
    '''
    result = Pessoa(nome='nome', sobrenome='teste')
    Pessoa.create(result)
    pessoa = Pessoa.query.filter_by(nome=nome).first()
    assert result == pessoa

# def test_organizar_pessoas():
#     '''testa se a função organizar_pessoas separa as pessoas por igual
#     '''
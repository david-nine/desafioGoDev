from app import app
from app.model.models import Sala, Pessoa

SALA = Sala(nome='test2')
PESSOA = Pessoa(nome='pessoa1', sobrenome='teste')

def test_create_sala():
    '''Verifica se a função Sala.create(sala) está criando uma nova 
    Sala no banco de dados.
    '''
    result = SALA
    Sala.create(SALA)
    busca = Sala.query.filter_by(nome=result.nome).first()
    assert result == busca

def test_save_sala():
    '''Verifica se a função Sala.save() está as novas informações da 
    Sala no banco de dados.
    '''
    result = 'nome_alterado'
    SALA.nome = result
    SALA.save()
    sala_alterada = Sala.query.filter_by(nome=result).first()
    assert result == sala_alterada.nome

def test_create_pessoa():
    '''Verifica se a função Pessoa.create(pessoa) está criando uma nova 
    Pessoa no banco de dados.
    '''
    result = PESSOA
    Pessoa.create(PESSOA)
    busca = Pessoa.query.filter_by(nome=result.nome).first()
    assert result == busca

def test_save_pessoa():
    '''Verifica se a função Pessoa.save() está as novas informações da 
    Pessoa no banco de dados.
    '''
    result = 'nome_alterado'
    PESSOA.nome = result
    PESSOA.save()
    pessoa_alterada = Pessoa.query.filter_by(nome=result).first()
    assert result == pessoa_alterada.nome
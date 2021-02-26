from app import app
from app.model.models import Sala, Pessoa

SALA = Sala(nome='test2')
PESSOA = Pessoa(nome='pessoa1', sobrenome='teste')

def test_save_sala():
    '''Verifica se a função Sala.save() está as novas informações da 
    Sala no banco de dados.
    '''
    result = 'nome_alterado'
    SALA.nome = result
    SALA.save()
    sala_alterada = Sala.query.filter_by(nome=result).first()
    assert result == sala_alterada.nome
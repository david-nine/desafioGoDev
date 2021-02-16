from app import db
from app.model.models import Sala
from app.model.forms import FormCafe

def test_validate_nome():
    result = ValidationError('Sala com esse nome já existente')
    sala = Sala(nome='teste1')
    Sala.create(sala)
    test = FormCafe.validate_nome('teste1')
    assert result == test
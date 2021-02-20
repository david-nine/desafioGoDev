from app import app
from flask import render_template, redirect
from app.model.forms import FormCafe, FormPessoa, FormSala, FormPesquisa
from app.model.dao import DAO
from app.model.models import Pessoa, Sala

DAO =  DAO()

@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    '''Home page

    Página inicial contendo a lista de todas as pessoas, botão para 
    cadastro de pessoas, botão para cadastro de salas, formulário para
    pesquisar salas e uma lista com todas as pessoas, com um botão para
    visualizar a pessoa, ao lado. 
    '''

    form = FormPesquisa()
    if form.validate_on_submit():
        return redirect('verSala/'+form.nome.data)
        
    pessoa1 = Pessoa(nome='david', sobrenome='hildebrandt')
    DAO.create(pessoa1)
    pessoa2 = Pessoa(nome='jorge', sobrenome='sobrenome')
    DAO.create(pessoa2)
    pessoa3 = Pessoa(nome='alisson', sobrenome='flores')
    DAO.create(pessoa3)

    sala1 = Sala(nome='sala 01', lotacao=15)
    DAO.create(sala1)
    sala2 = Sala(nome='sala 02', lotacao=20)
    DAO.create(sala2)
    sala3 = Sala(nome='sala cafe 01')
    DAO.create(sala3)
    sala4 = Sala(nome='sala cafe 02')
    DAO.create(sala4)
    sala1.etapa1.append(pessoa1)
    sala1.etapa1.append(pessoa2)
    sala1.etapa1.append(pessoa3)
    sala1.save()
    sala1.etapa2.append(pessoa2)
    sala1.etapa2.append(pessoa3)
    sala1.etapa2.append(pessoa1)
    sala1.save()
    sala2.etapa1.append(pessoa1)
    sala2.etapa1.append(pessoa2)
    sala2.etapa1.append(pessoa3)
    sala2.save()
    sala2.etapa2.append(pessoa2)
    sala2.etapa2.append(pessoa3)
    sala2.etapa2.append(pessoa1)
    sala2.save()
    sala3.etapa1.append(pessoa1)
    sala3.etapa1.append(pessoa2)
    sala3.etapa1.append(pessoa3)
    sala3.save()
    sala3.etapa2.append(pessoa2)
    sala3.etapa2.append(pessoa3)
    sala3.etapa2.append(pessoa1)
    sala3.save()    
    sala4.etapa1.append(pessoa1)
    sala4.etapa1.append(pessoa2)
    sala4.etapa1.append(pessoa3)
    sala4.save()
    sala4.etapa2.append(pessoa2)
    sala4.etapa2.append(pessoa3)
    sala4.etapa2.append(pessoa1)
    sala4.save()
    # pessoas = DAO.busca_pessoas()


    # DAO.organizar_pessoas()
    pessoas = DAO.busca_pessoas()
    
    return render_template('index.html', form=form, pessoas=pessoas)

@app.route('/cadastroPessoa', methods=['get', 'post'])
def cadastro_pessoa():
    '''Tela de cadastro de pessoas
    
    Página com o formulário para cadstro de pessoas.
    '''
    form = FormPessoa()
    if form.validate_on_submit():
        DAO.cadastrar_pessoa(form)
        return redirect('/')

    return render_template('cadastroPessoa.html', form=form)

@app.route('/cadastroSala', methods=['get', 'post'])
def cadastro_sala():
    '''Tela de cadastro de salas

    Página com o formulário para cadastro de salas.
    '''
    form = FormSala()
    if form.validate_on_submit():
        DAO.cadastrar_sala(form)
        return redirect('/index')
    return render_template('cadastroSala.html', form=form)


@app.route('/verSala/<sala>', methods=['get', 'post'])
def ver_sala(sala):
    '''Tela com as informações da sala

    Página contendo duas tabelas, uma para cada etapa, com as pessoas 
    que estarão na sala em cada uma das etapas.

    Parameters
    ----------
    sala : str
        nome da sala 
    '''
    sala = DAO.pesquisa_sala(sala)
    etapa1 = sala.etapa1
    etapa2 = sala.etapa2

    return render_template('sala.html', sala=sala, etapa1=etapa1, etapa2=etapa2)

@app.route('/cadastroCafe', methods=['get', 'post'])
def cadastro_cafe():
    '''Tela de cadastro de salas de café

    Página com o formulário para cadastro de salas de café.
    '''
    form = FormCafe()
    if form.validate_on_submit():
        DAO.cadastrar_salacafe(form)
        return redirect('/index')
    return render_template('cadastroCafe.html', form=form)

@app.route('/verPessoa/<id>', methods=['get', 'post'])
def ver_pessoa(id):
    pessoa = DAO.pesquisa_pessoa(id)
    salas = Sala.query.with_parent(pessoa)
    sala1 = salas[0]
    sala2 = salas[1]
    sala3 = salas[2]
    sala4 = salas[3]
    # sala4 = salas[2]
    print("------------------------")
    print(sala2)
    print("------------------------")
    print(sala2)
    print("------------------------")
    print(sala3)
    print("------------------------")
    print(sala4)

    return render_template('pessoa.html', pessoa=pessoa, sala1=sala1,
                           sala2=sala2, sala3=sala3, sala4=sala4)
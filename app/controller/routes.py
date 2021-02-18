from app import app
from flask import render_template, redirect
from app.model.forms import FormCafe, FormPessoa, FormSala, FormPesquisa
from app.model.dao import DAO

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
    # DAO.organizar_pessoas()
    pessoas = DAO.busca_pessoas()
    form = FormPesquisa()
    if form.validate_on_submit():
        return redirect('verSala/'+form.nome.data)
    
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
    salas = pessoa[1]
    salascafe = pessoa[2]
    pessoa = pessoa[0]
    return render_template('pessoa.html', pessoa=pessoa, salascafe=salascafe,\
                           salas=salas)
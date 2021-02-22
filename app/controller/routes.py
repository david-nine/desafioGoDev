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
    pesquisa = FormPesquisa()
    if pesquisa.validate_on_submit():
        return redirect('verSala/'+pesquisa.nomepesquisa.data)
    DAO.organizar_pessoas()
    pessoas = DAO.busca_pessoas()
    return render_template('index.html', pesquisa=pesquisa, pessoas=pessoas)

@app.route('/cadastroPessoa', methods=['get', 'post'])
def cadastro_pessoa():
    '''Tela de cadastro de pessoas
    
    Página com o formulário para cadstro de pessoas.
    '''
    pesquisa = FormPesquisa()
    form = FormPessoa()
    if form.validate_on_submit():
        DAO.cadastrar_pessoa(form)
        return redirect('/')

    return render_template('cadastroPessoa.html', form=form, pesquisa=pesquisa)

@app.route('/cadastroSala', methods=['get', 'post'])
def cadastro_sala():
    '''Tela de cadastro de salas

    Página com o formulário para cadastro de salas.
    '''
    pesquisa = FormPesquisa()
    form = FormSala()
    if form.validate_on_submit():
        DAO.cadastrar_sala(form)
        return redirect('/index')
    return render_template('cadastroSala.html', form=form, pesquisa=pesquisa)


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
    pesquisa = FormPesquisa()
    sala = DAO.pesquisa_sala(sala)
    pessoas1 = sala.pessoas1
    pessoas2 = sala.pessoas2
    return render_template('sala.html', sala=sala, pessoas1=pessoas1, 
                           pessoas2=pessoas2, pesquisa=pesquisa)

@app.route('/cadastroCafe', methods=['get', 'post'])
def cadastro_cafe():
    '''Tela de cadastro de salas de café

    Página com o formulário para cadastro de salas de café.
    '''
    pesquisa = FormPesquisa()
    form = FormCafe()
    if form.validate_on_submit():
        DAO.cadastrar_salacafe(form)
        return redirect('/index')
    return render_template('cadastroCafe.html', form=form, pesquisa=pesquisa)

@app.route('/verPessoa/<id>', methods=['get', 'post'])
def ver_pessoa(id):
    '''Tela que mostra as informações da pessoa

    Carrega as salas que a pessoa vai ficar na etapa 1 e na etapa 2 

    Parrameters
    -----------
    id : int
        número do id da pessoa
    '''
    pessoa = DAO.pesquisa_pessoa(id)
    pesquisa = FormPesquisa()

    return render_template('pessoa.html', pessoa=pessoa, pesquisa=pesquisa)
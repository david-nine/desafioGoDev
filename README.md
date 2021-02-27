# Sistema para cadastro de pessoas e salas

Este sistema realiza o cadastro de pessoas a partir do nome e sobrenome,
de salas a partir do nome e lotação e de espaços para café a partir do 
nome. Realizando então a divisão por igual das pessoas entre as salas 
com no maximo uma pessoa de diferença entre elas.

É possivel pesquisar pessoas cadastradas, e visuaisar a sala que ela vai
ficar em cada uma das etapas e a sala de café de cada intervalo.

Também se pode pesquisar uma sala ou espaço de café, retornando a lista
de pessoas que vão estar neste espaço em cada etapa.

Para poder cadastrar pessoas é necessário ter no mínimo duas salas e dois
espaços de café para poder fazer a divisão das pessoas entra as salas.

## Instalação

- Baixar [Python 3](https://www.python.org/downloads/)
- Clonar o repositório
- De o comando:

    ```python -m pip install --upgrade pip```
- instalar o arquivo **requirements.txt**

    ```python -m pip install -r requirements.txt```
- Executar o arquivo **start_bd.py**
- Executar o arquivo **inicializador.py**

## Como usar

Páginas e conteúdo de cada uma delas

### Home Page

- Navbar com os botões **Home**, **cadastrar sala**, **Cadastrar Pessoa**, **Cadastrar Espaço de café**
- Lista com todas as pessoas cadastradas com um botão ao lado para visualizar
o seu perfil.
- Campo para pesquisar a sala pelo nome

### Perfil da pessoa

Esta tela contém o nome da pessoa e duas tabelas, uma de cada etapa,
com a sala que a pessoa vai ficar e o espaço de café.

### Sala

Esta tela contém duas tabelas uma para cada etapa com a lista de pessoas
que vai ficar nesta sala em cada uma das etapas.

## Tests

Para rodar os testes, execute o arquivo start_bd.py

Execute os seguintes comandos no terminal:
   
    ```pip install -U pytest```

    ```python -m pytest```
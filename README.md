
<h1 align="center"> Projeto ReddFlow </h1>

<div align="center">

<img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/pedro-hnrq/Proj_ReddFlow" />
<img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/pedro-hnrq/Proj_ReddFlow" />
<img alt="" src="https://img.shields.io/github/repo-size/pedro-hnrq/Proj_ReddFlow" />
<img alt="Github License" src="https://img.shields.io/github/license/pedro-hnrq/Proj_ReddFlow" />

</div>

<h2 align="center">📷 Prévia <h2>

![topi_view](https://github.com/pedro-hnrq/Proj_ReddFlow/assets/74242717/6466d014-6675-4fe4-9498-fe24307a6127)


<h3>🎯 Objetivo</h3>

<h5 align="justify">O ReddFlow é um projeto desenvolvido como parte de um teste, com o propósito de criar uma plataforma interativa de fórum. Ele permite o gerenciamento de postagens e comentários, onde apenas usuários autenticados têm permissão para criar novas postagens e fazer comentários. Usuários anônimos têm acesso somente à visualização do conteúdo. Além disso, os usuários autenticados podem gerenciar sua própria conta.</h5>


<h4> 🚀 Como executar </h4>

#### 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Python 
- Django 
- GIT 
- PostgreSQL
- Docker
- Docker Compose


#### 🛠️ Instalação

Faça o clone do projeto:

```
git@github.com:pedro-hnrq/Proj_ReddFlow.git
```  
Após clonar o repositório acesse o diretório
```
cd Proj_ReddFlow
``` 

Crie uma maquina virtual  para rodar o projeto.

```python
python -m venv .venv
```
Uma vez criado seu ambiente virtual, você deve ativá-lo.

No Unix ou no MacOS, executa:

```bash
source .venv/bin/activate
```

No Windows, execute:

```bash
.venv\Scripts\activate.bat
```

Com o ambiente virtual ativo instale as dependências

```python
pip install -r requirements.txt
```

execute os comandos abaixo para criar arquivo de variáveis de ambiente a partir de exemplos. (Lembre-se de modificá-los)

```bash
mv env .env
```
#### Execução na máquina

Na primeira vez é necessário executar esse comando para aplicar as migrações do banco de dados
```python
python manage.py migrate
```

Criando super usuário para acessar o painel administrativo
```python
python manage.py createsuperuser
```

Executando a aplicação
```python
python manage.py runserver
```

#### 🐋 Execução com DOCKER


Antes de tudo, construa e execute o contêiner Docker:

```bash
docker compose up --build
```

Após iniciar o contêiner, aplique as migrações no banco de dados PostgreSQL:
```bash
docker compose exec app python manage.py migrate
```

__Acessando o PGAdmin__

Acesse o PGAdmin em [localhost:5051](http://localhost:5051) no seu navegador usando a senha padrão admin. Em seguida, configure a conexão com o banco de dados:
 
 - General/name: _DB_
 - Connection/Host name: _DB_
 - Connection/Port: 5432 (default)
 - Connection/Database: _forum_
 - Connection/Username: _Dev_
 - Connection/Password: _Dev@pg_

Os emails enviados podem ser visualizados no link [localhost:8000](http://localhost:8000)

**Acesso ao Site e Painel Administrativo**

Para acessar no site e no painel administrativo, crie um superusuário com o seguinte comando:
```bash
docker compose exec app python manage.py createsuperuser
```
```bash
docker compose exec app python manage.py runserver
```

Para poder parar a aplicação no docker basta executar
```bash
docker compose down
```


## Licença
[MIT License](LICENSE)

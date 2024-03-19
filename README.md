
<h1 align="center"> Projeto ReddFlow </h1>

<!-- badges -->

<h2 align="center">📷 Prévia <h2>

<h3>🎯 Objetivo</h3>

<h5 align="justify">O ReddFlow é um projeto desenvolvido como parte de um teste, com o propósito de criar uma plataforma interativa de fórum. Ele permite o gerenciamento de postagens e comentários, onde apenas usuários autenticados têm permissão para criar novas postagens e fazer comentários. Usuários anônimos têm acesso somente à visualização do conteúdo. Além disso, os usuários autenticados podem gerenciar sua própria conta.</h5>


<h4> 🚀 Como executar </h4>

#### 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Python 
- Django 
- GIT 
- PostgreSQL


#### 🛠️ Instalação

Faça o clone do projeto:

```
git@github.com:pedro-hnrq/Proj_ReddFlow
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

#### Realizar Teste

```python
python manage.py test
```

## Licença
[MIT License](LICENSE)
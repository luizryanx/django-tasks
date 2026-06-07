requirements.txt
asgiref==3.11.1
Django==6.0.4
sqlparse==0.5.5
tzdata==2026.2


Django Tasks

Sistema de Gerenciamento de Tarefas

Descrição

O Django Tasks é um sistema web desenvolvido com Django para auxiliar no gerenciamento de tarefas.

A aplicação permite que usuários autenticados criem, visualizem, editem e removam tarefas, facilitando a organização das atividades do dia a dia.

⸻

Problema que o sistema busca resolver

O sistema foi desenvolvido para ajudar no controle e organização de tarefas, permitindo que o usuário acompanhe suas atividades em um único local de forma simples e prática.

⸻

Tipo de Usuário

Usuário Autenticado

O sistema possui acesso restrito a usuários autenticados.

Para acessar a aplicação pela primeira vez, é necessário criar um usuário através do comando:
(obs:. Ou então usar o meu login. Usuário:Luizryanx, Senha: Letycia15)

python manage.py createsuperuser

Após a criação do usuário, será possível realizar login e utilizar todas as funcionalidades do sistema.

⸻

Funcionalidades

* Login no sistema;
* Logout;
* Cadastro de tarefas;
* Listagem de tarefas;
* Edição de tarefas;
* Exclusão de tarefas;
* Alteração de senha;
* Controle e gerenciamento das tarefas cadastradas.

⸻

Tecnologias Utilizadas

* Python
* Django
* SQLite
* HTML
* CSS
* Bootstrap

⸻

Instalação e Execução

1. Clonar o repositório

git clone https://github.com/luizryanx/django-tasks.git

1. Entrar na pasta do projeto

cd django-tasks

1. Criar um ambiente virtual

python -m venv venv

1. Ativar o ambiente virtual

Windows

venv\Scripts\activate

Linux/macOS

source venv/bin/activate

1. Instalar as dependências

pip install -r requirements.txt

1. Aplicar as migrações

python manage.py migrate

1. Criar um usuário para acesso

python manage.py createsuperuser

1. Executar o servidor

python manage.py runserver

1. Acessar o sistema

Abra o navegador e acesse:

http://127.0.0.1:8000/

⸻

Como Utilizar

1. Execute o projeto seguindo os passos de instalação.
2. Crie um usuário utilizando o comando createsuperuser.
3. Faça login no sistema.
4. Cadastre novas tarefas.
5. Edite ou exclua tarefas quando necessário.
6. Utilize a funcionalidade de alteração de senha quando desejar.

⸻

Dados Iniciais para Testes

O sistema não possui dados obrigatórios para funcionamento.

Para iniciar os testes:

1. Execute as migrações.
2. Crie um usuário com o comando:

python manage.py createsuperuser

1. Faça login no sistema.
2. Cadastre tarefas para testar as funcionalidades.

⸻

Autor

Projeto desenvolvido por Luiz Ryan Araújo da Silva como atividade final do curso de Desenvolvimento Web com Django.

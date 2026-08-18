# 🏥 Agenda Médica

Sistema web de gerenciamento de consultas médicas desenvolvido com **Python**, **Flask** e **SQLite**.

O projeto está sendo desenvolvido como parte da minha jornada de aprendizado em **desenvolvimento Back-end com Python**, aplicando na prática conceitos de desenvolvimento web, banco de dados, autenticação, APIs, CRUD e integração entre Front-end e Back-end.

## 🚀 Tecnologias utilizadas

* 🐍 Python 3
* 🌐 Flask
* 🗄️ SQLite
* 📄 HTML5
* 🎨 CSS3
* 🔧 Jinja2
* 📊 Tabulator
* 🌐 Requests
* 🌱 Git e GitHub

## 📚 Funcionalidades

Atualmente, o projeto possui:

* 🔐 Sistema de login
* 👤 Autenticação de usuários
* 🔒 Controle de sessão
* 📊 Dashboard
* 🗄️ Integração com banco de dados SQLite
* 🧑‍🤝‍🧑 Cadastro e utilização de dados de pacientes
* 👨‍⚕️ Dados de médicos
* 📅 Consultas médicas
* 🔌 API de consultas
* 🌐 Consumo de APIs externas
* 📡 Requisições HTTP com Requests
* ⚠️ Tratamento de erros de API
* 📊 Tabela dinâmica com Tabulator
* 🔎 Filtros por paciente, médico, data e hora
* ↕️ Ordenação dos dados
* 📜 Rolagem vertical para visualização das consultas
* ⚙️ Coluna de ações na tabela
* 🗑️ Exclusão de consultas pela interface
* 🔌 Exclusão de consultas através de API REST
* 🗄️ Exclusão dos registros diretamente no SQLite
* 🔄 Atualização da tabela após exclusão

## 🔌 API de consultas

O sistema possui uma API própria para gerenciamento das consultas.

### Listar consultas

```text
GET /api/consultas
```

Retorna as consultas cadastradas em formato JSON.

### Excluir consulta

```text
DELETE /api/consultas/<id>
```

Exemplo:

```text
DELETE /api/consultas/10
```

A requisição é processada pelo Flask e o registro correspondente é excluído do banco de dados SQLite.

Após a exclusão, a linha também é removida da tabela do Tabulator sem a necessidade de recarregar a página.

## 📁 Estrutura do projeto

```text
agenda-medica/
│
├── app.py
├── banco.py
├── criar_tabela.py
├── seed.py
├── api_externa.py
├── requirements.txt
├── agenda.db
│
├── templates/
│   ├── login.html
│   └── dashboard.html
│
└── README.md
```

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/wander671/sistema-agenda-medica.git
```

### 2. Entre na pasta do projeto

```bash
cd sistema-agenda-medica
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Crie as tabelas do banco de dados

```bash
python criar_tabela.py
```

### 7. Insira os dados de teste

```bash
python seed.py
```

### 8. Execute a aplicação

```bash
python app.py
```

Depois, acesse no navegador:

```text
http://127.0.0.1:5000
```

## 💻 Conceitos praticados

Durante o desenvolvimento deste projeto, estou praticando:

* Desenvolvimento Back-end com Python
* Framework Flask
* Rotas e requisições HTTP
* Métodos HTTP GET e DELETE
* Templates HTML com Jinja2
* Banco de dados SQLite
* SQL
* CRUD
* Autenticação de usuários
* Sessões
* APIs REST
* Consumo de APIs externas
* Biblioteca Requests
* JSON
* Tratamento de erros HTTP
* Tabulator
* JavaScript
* Fetch API
* Integração entre Front-end e Back-end
* Integração entre Flask e SQLite
* Organização de projetos
* Git e GitHub

## 🎯 Próximos passos

O projeto continuará evoluindo com novas funcionalidades, incluindo:

* ✏️ Edição de consultas
* 👨‍⚕️ Cadastro de médicos pela interface
* 🧑‍🤝‍🧑 Cadastro de pacientes pela interface
* 📅 Agendamento de consultas pela interface
* 🔎 Sistema de busca de consultas
* 🔐 Melhorias na segurança da autenticação
* 📱 Interface responsiva
* 🚀 Melhorias na experiência do usuário

## 📈 Status do projeto

🚧 **Em desenvolvimento**

Este projeto faz parte do meu processo de aprendizado e evolução na área de **desenvolvimento Back-end com Python**.

## 👨‍💻 Autor

**Wander Farias**

🔗 **GitHub:**
https://github.com/wander671

🔗 **LinkedIn:**
https://www.linkedin.com/in/wander-farias-396066363/

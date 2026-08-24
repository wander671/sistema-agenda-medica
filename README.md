# 🏥 Agenda Médica

Sistema web para gerenciamento de consultas médicas, desenvolvido com **Python e Flask**, com banco de dados **SQLite**, API REST, autenticação de usuários e execução em **Docker**.

O projeto foi desenvolvido com foco em aprendizado prático de **Back-end com Python**, aplicando conceitos de desenvolvimento web, banco de dados, APIs, tratamento de erros, integração Front-end/Back-end, containerização e versionamento com Git.

---

## 📌 Sobre o projeto

A **Agenda Médica** é uma aplicação web desenvolvida para organizar e gerenciar consultas médicas.

O sistema permite autenticação de usuários, visualização de consultas, pesquisa por pacientes ou médicos, exclusão de consultas e comunicação com uma API própria.

A aplicação também foi preparada para execução utilizando **Docker e Docker Compose**, garantindo um ambiente padronizado para execução do projeto.

---

## 🚀 Funcionalidades

### 🔐 Autenticação

- Login de usuários
- Controle de sessão
- Logout
- Validação de acesso
- Interface de login responsiva
- Mostrar/ocultar senha

### 📊 Dashboard

- Visualização das consultas cadastradas
- Interface moderna e responsiva
- Tabela dinâmica com Tabulator
- Ordenação dos dados
- Rolagem vertical
- Coluna de ações
- Exclusão de consultas

### 🔎 Busca

- Busca por paciente
- Busca por médico
- Busca geral
- Busca diretamente pela API
- Retorno de resultados em JSON
- Tratamento de busca sem resultados

### 🗄️ Banco de dados

- SQLite
- Relacionamento entre tabelas
- Pacientes
- Médicos
- Consultas
- Operações CRUD
- Tratamento de erros no banco
- Utilização de `rollback()` em operações com falha

### 🔌 API REST

- Listagem de consultas
- Busca de consultas
- Exclusão de consultas
- Retorno de dados em JSON
- Parâmetros de busca
- Integração com o Front-end

### 🌐 API externa

- Consumo de API externa utilizando Requests
- Tratamento de `Timeout`
- Tratamento de `ConnectionError`
- Tratamento de `HTTPError`
- Tratamento de `RequestException`
- Validação de respostas HTTP
- Validação de respostas JSON

### ⚠️ Tratamento de erros

- Página personalizada para erro `404`
- Página personalizada para erro `500`
- Tratamento de exceções SQLite
- Tratamento de erros em APIs externas
- Utilização de `try/except/finally`

### 🐳 Docker

- Dockerfile
- Docker Image
- Docker Container
- Docker Compose
- WSL 2
- Mapeamento de portas
- Persistência do SQLite através de volume
- Execução da aplicação Flask em container

---

# 🛠️ Tecnologias

| Tecnologia | Utilização |
|---|---|
| 🐍 Python 3.14 | Linguagem principal |
| 🌐 Flask | Framework Web |
| 🗄️ SQLite | Banco de dados |
| 📊 Tabulator | Tabela dinâmica |
| 🌐 Requests | Consumo de APIs |
| 📄 HTML5 | Estrutura das páginas |
| 🎨 CSS3 | Interface e responsividade |
| 🔧 Jinja2 | Templates |
| 💻 JavaScript | Interações da interface |
| 🐳 Docker | Containerização |
| 🐳 Docker Compose | Orquestração do container |
| 🐧 WSL 2 | Ambiente Linux no Windows |
| 🌱 Git | Controle de versão |
| 🐙 GitHub | Hospedagem do código |

---

# 📁 Estrutura do projeto

```text
agenda-medica/
│
├── app/
│
├── static/
│   └── style.css
│
├── templates/
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── agenda.db
├── api_externa.py
├── app.py
├── banco.py
├── criar_tabela.py
├── seed.py
├── requirements.txt
└── README.md


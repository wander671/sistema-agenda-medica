# 🏥 Agenda Médica em Python + Flask

Projeto desenvolvido para praticar desenvolvimento web com **Python**, **Flask** e **SQLite**, simulando um sistema simples de agendamento de consultas médicas.

## 🚀 Tecnologias utilizadas

* Python 3
* Flask
* SQLite
* HTML5
* CSS3
* Jinja2

## 📚 Objetivo

O objetivo deste projeto é consolidar conhecimentos em:

* Estrutura de projetos Flask
* Criação de banco de dados SQLite
* CRUD básico
* Login de usuários
* Sessões (Session)
* Templates HTML
* Integração entre Flask e Banco de Dados

## 📁 Estrutura do projeto

```text
agenda-medica/
│
├── app.py
├── banco.py
├── criar_tabela.py
├── seed.py
├── agenda.db
├── templates/
│   ├── login.html
│   └── index.html
└── README.md
```

## ⚙️ Como executar

### Clone o projeto

```bash
git clone https://github.com/SEU-USUARIO/agenda-medica.git
```

### Entre na pasta

```bash
cd agenda-medica
```

### Crie um ambiente virtual

```bash
python -m venv .venv
```

### Ative o ambiente virtual

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

### Instale as dependências

```bash
pip install flask
```

### Crie as tabelas

```bash
python criar_tabela.py
```

### Insira dados de teste

```bash
python seed.py
```

### Execute o projeto

```bash
python app.py
```

Depois abra:

```
http://127.0.0.1:5000
```

## 💻 Aprendizados

Durante este projeto foram praticados:

* Organização de projetos Flask
* Banco de dados SQLite
* SQL (CREATE, INSERT e SELECT)
* Templates HTML
* Sistema de Login
* Sessões de usuário
* Estrutura MVC

## 🎯 Próximas melhorias

* Cadastro de pacientes
* Cadastro de médicos
* Agendamento de consultas pela interface
* Edição de consultas
* Exclusão de consultas
* Interface responsiva
* Autenticação mais segura

## 👨‍💻 Autor

**Wander Farias**

GitHub: https://github.com/wander671

LinkedIn: https://www.linkedin.com/in/wander-farias-396066363

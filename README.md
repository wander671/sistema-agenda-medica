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
* 💻 JavaScript
* 🌱 Git e GitHub

## 📚 Funcionalidades

Atualmente, o projeto possui:

* 🔐 Sistema de login
* 👤 Autenticação de usuários
* 🔒 Controle de sessão
* 🎨 Interface de login com visual profissional
* 👁️ Mostrar e ocultar senha
* 📊 Dashboard
* 🎨 Dashboard com interface moderna e responsiva
* 🗄️ Integração com banco de dados SQLite
* 🧑‍🤝‍🧑 Cadastro e utilização de dados de pacientes
* 👨‍⚕️ Dados de médicos
* 📅 Consultas médicas
* 🔌 API de consultas
* 🌐 Consumo de APIs externas
* 📡 Requisições HTTP com Requests
* ⚠️ Tratamento de erros de API
* 📊 Tabela dinâmica com Tabulator
* 🔎 Busca de consultas por paciente
* 👨‍⚕️ Busca de consultas por médico
* 🔎 Busca geral por paciente ou médico
* ↕️ Ordenação dos dados
* 📜 Rolagem vertical para visualização das consultas
* ⚙️ Coluna de ações na tabela
* 🗑️ Exclusão de consultas pela interface
* 🔌 Exclusão de consultas através de API REST
* 🗄️ Exclusão dos registros diretamente no SQLite
* 🔄 Atualização da tabela após exclusão

## 🎨 Melhorias de interface

O projeto recebeu melhorias visuais para proporcionar uma experiência mais próxima de um sistema profissional.

### Tela de Login

* 🏥 Identidade visual da Agenda Médica
* 🔐 Card centralizado para autenticação
* 👤 Campos de usuário e senha estilizados
* 👁️ Botão para mostrar e ocultar senha
* 🔵 Botão de login moderno
* ✨ Efeitos de interação
* 📱 Layout responsivo

### Dashboard

* 🏥 Cabeçalho com identidade visual
* 👋 Área de boas-vindas ao usuário
* 🚪 Botão de logout estilizado
* 🔎 Campo de pesquisa moderno
* 📋 Área de consultas organizada em painel
* 🗑️ Botão de exclusão estilizado
* 📱 Responsividade para diferentes tamanhos de tela

## 🔌 API de consultas

O sistema possui uma API própria para gerenciamento das consultas.

### Listar consultas

```text
GET /api/consultas
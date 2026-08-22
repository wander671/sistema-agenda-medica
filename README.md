# 🏥 Agenda Médica

Sistema web de gerenciamento de consultas médicas desenvolvido com **Python**, **Flask** e **SQLite**.

O projeto está sendo desenvolvido como parte da minha jornada de aprendizado em **desenvolvimento Back-end com Python**, aplicando na prática conceitos de desenvolvimento web, banco de dados, autenticação, APIs, CRUD, SQL e integração entre Front-end e Back-end.

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

## 🔎 Busca de consultas — Aula 10

A **Aula 10** teve como objetivo implementar e finalizar a busca de consultas no Back-end.

A API permite pesquisar consultas utilizando o nome do paciente ou do médico.

### Conceitos aplicados

* 🔀 Estruturas condicionais `if/else`
* 🔎 Parâmetros recebidos pela URL
* 🗄️ SQL com `WHERE`
* 🔍 SQL com `LIKE`
* 🔐 Parâmetros SQL utilizando `?`
* 🧩 `JOIN` entre tabelas
* 📋 `fetchall()`
* 📦 Retorno de dados em formato JSON
* 🔌 Integração entre API e Front-end

### Funcionamento da busca

Quando o usuário informa um termo de pesquisa, o sistema utiliza:

```sql
WHERE pacientes.nome LIKE ?
   OR medicos.nome LIKE ?
```

O termo pesquisado é transformado em um padrão utilizando `%`:

```python
termo = f"%{busca}%"
```

Os valores são enviados como parâmetros da consulta SQL:

```python
(termo, termo)
```

Dessa forma, o sistema consegue pesquisar o termo tanto no nome do paciente quanto no nome do médico.

Quando o campo de busca está vazio, o sistema retorna normalmente todas as consultas cadastradas.

## 🧪 Testes realizados na Aula 10

A busca foi testada em diferentes situações:

* ✅ Busca por paciente com resultado
* ✅ Busca por médico com resultado
* ✅ Busca sem resultado
* ✅ Busca vazia
* ✅ Retorno de todas as consultas
* ✅ Verificação do status HTTP `200`
* ✅ Verificação do retorno em JSON
* ✅ Teste da busca diretamente pela API
* ✅ Teste da busca através da Dashboard
* ✅ Verificação de que as consultas continuam funcionando normalmente

## 🔌 API de consultas

O sistema possui uma API própria para gerenciamento das consultas.

### Listar todas as consultas

```text
GET /api/consultas
```

Retorna todas as consultas cadastradas quando nenhum termo de busca é informado.

### Buscar consultas

```text
GET /api/consultas?busca=João
```

A busca pode localizar consultas pelo nome do paciente ou pelo nome do médico.

### Buscar por médico

```text
GET /api/consultas?busca=Carlos
```

### Busca sem resultado

Quando nenhum registro corresponde ao termo informado, a API retorna uma lista vazia:

```json
[]
```

### Excluir consulta

```text
DELETE /api/consultas/<id>
```

A API permite excluir uma consulta específica utilizando seu ID.

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

## 📖 Jornada de desenvolvimento

O projeto está sendo desenvolvido de forma incremental, com cada etapa adicionando novos conhecimentos e funcionalidades.

### Etapas concluídas

* ✅ Estrutura inicial do projeto
* ✅ Banco de dados SQLite
* ✅ Criação das tabelas
* ✅ Cadastro e utilização de pacientes
* ✅ Cadastro e utilização de médicos
* ✅ Sistema de login
* ✅ Controle de sessão
* ✅ API de consultas
* ✅ Consumo de API externa com Requests
* ✅ CRUD de consultas
* ✅ Integração com Tabulator
* ✅ Exclusão de consultas
* ✅ Busca de consultas no Back-end

### 🐍 Aula 10 — Busca

**Status: ✅ Concluída**

Nesta etapa foram aplicados conhecimentos de:

* Python
* Flask
* SQLite
* SQL
* `WHERE`
* `LIKE`
* Parâmetros SQL
* `if/else`
* APIs
* JSON
* Integração entre Back-end e Front-end
* Testes de API

## 🎯 Próximos passos

O projeto continuará evoluindo com novas funcionalidades e melhorias, incluindo:

* 🔎 Melhorias na experiência de busca
* 🧹 Botão para limpar a busca
* 📅 Novos recursos para gerenciamento de consultas
* 🔐 Melhorias de segurança
* 🎨 Novos aprimoramentos na interface
* 🐳 Estrutura para execução com Docker
* 🧪 Ampliação dos testes
* 🚀 Novas funcionalidades de Back-end e API

## 💡 Objetivo do projeto

O objetivo da **Agenda Médica** é aplicar na prática conhecimentos de desenvolvimento Back-end com Python, criando um sistema completo que envolva:

**Python + Flask + SQLite + SQL + APIs + Front-end + Git/GitHub**

O projeto também faz parte da construção do meu portfólio profissional na área de tecnologia.

---

👨‍💻 **Desenvolvido por Wander Farias**

🐍 Python | 🌐 Flask | 🗄️ SQLite | 🔌 API | 📊 SQL | 🌱 Git/GitHub

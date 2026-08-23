# 🏥 Agenda Médica

Sistema web de gerenciamento de consultas médicas desenvolvido com **Python**, **Flask** e **SQLite**.

O projeto está sendo desenvolvido como parte da minha jornada de aprendizado em **desenvolvimento Back-end com Python**, aplicando na prática conceitos de desenvolvimento web, banco de dados, autenticação, APIs, CRUD, SQL, tratamento de erros e integração entre Front-end e Back-end.

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
* 🚨 Tratamento personalizado de erros 404 e 500
* 🛡️ Tratamento de exceções no banco de dados
* 🔄 Uso de `rollback()` em operações do banco
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

## 🛡️ Tratamento de erros — Aula 11

A **Aula 11** teve como objetivo tornar o sistema mais robusto e preparado para situações inesperadas durante sua execução.

Foram implementados tratamentos de erros no Back-end, banco de dados e integração com APIs externas.

### Tratamento de erros no Flask

Foram criadas páginas personalizadas para os principais erros HTTP:

* 🚨 **404 — Página não encontrada**
* 🚨 **500 — Erro interno do servidor**

As páginas foram criadas para apresentar mensagens amigáveis ao usuário, evitando a exibição de páginas técnicas do Flask.

### Tratamento de erros no SQLite

A conexão e as operações com o banco de dados passaram a utilizar tratamento de exceções com:

```python
try:
    # operação no banco
except sqlite3.Error as erro:
    # tratamento do erro
```

Também foi implementado:

```python
rollback()
```

para desfazer operações quando ocorre uma falha durante uma alteração no banco.

Além disso, foi utilizado:

```python
finally
```

para garantir o fechamento da conexão com o banco de dados.

### Tratamento de erros na API externa

A integração com a API externa utilizando `Requests` também recebeu melhorias.

Foram adicionados tratamentos para:

* ⏱️ `Timeout`
* 🌐 `ConnectionError`
* 🚨 `HTTPError`
* ⚠️ `RequestException`
* 📦 Respostas que não estejam em formato JSON válido

Também foi utilizado um tempo limite para a requisição:

```python
requests.get(url, timeout=5)
```

E a resposta HTTP passou a ser validada utilizando:

```python
resposta.raise_for_status()
```

### 🧪 Testes realizados na Aula 11

Durante a aula foram realizados testes para garantir que as alterações não quebrassem funcionalidades existentes:

* ✅ Teste da página 404
* ✅ Teste da aplicação Flask
* ✅ Teste da conexão com SQLite
* ✅ Teste da busca de consultas
* ✅ Teste da exclusão de consultas
* ✅ Teste da API externa
* ✅ Verificação do status HTTP `200`
* ✅ Teste de compilação do `app.py`
* ✅ Validação das funcionalidades existentes após as alterações

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
* ✅ Tratamento de erros no Back-end
* ✅ Tratamento de erros no SQLite
* ✅ Tratamento de erros em APIs externas
* ✅ Páginas personalizadas 404 e 500

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

### 🛡️ Aula 11 — Tratamento de Erros

**Status: ✅ Concluída**

Nesta etapa foram aplicados conhecimentos de:

* Python
* Flask
* `try/except`
* `finally`
* SQLite
* `sqlite3.Error`
* `rollback()`
* Tratamento de erros HTTP
* Erros 404 e 500
* Requests
* Timeout
* ConnectionError
* HTTPError
* RequestException
* Validação de respostas de API
* Testes e validação do sistema

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


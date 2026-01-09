## ℹ️ Sobre este repositório

Este repositório reúne **scripts novos e antigos em Python (.py)** que foram desenvolvidos há anos como parte dos meus estudos e práticas iniciais.  
Eles foram **commitados recentemente** apenas para organização e preservação, por isso as datas de criação no GitHub podem parecer diferentes das datas reais em que os códigos foram escritos.

O objetivo é manter um histórico acessível e transparente dos meus aprendizados em Python, mesmo que os arquivos tenham sido adicionados ao GitHub em datas mais recentes.


# 🐍 Roteiro de Estudo de Python


[📋 Checklist de Estudos em Python](https://github.com/GitLucasCoutinho/Python/blob/main/Checklist%20de%20Estudos%20em%20Python.md)




## 🔹 Fundamentos Essenciais
- **Instalação e ambiente**
  - Instale Python via [site oficial](https://www.python.org).
  - Configure `venv` para ambientes virtuais.
  - Use `python`, `pip`, `pip install`.
- **Sintaxe básica**
  - Tipos primitivos: `int`, `float`, `str`, `bool`.
  - Variáveis e constantes.
  - Operadores aritméticos e lógicos.
- **Controle de fluxo**
  - `if/elif/else`, `for`, `while`.
  - `break`, `continue`.
- **Funções**
  - Definição com `def`.
  - Parâmetros padrão, argumentos nomeados.
  - Retorno múltiplo.
- **Exercícios**
  - Programa que soma dois números.
  - Verificador de número primo.
  - Conversor de temperatura (Celsius ↔ Fahrenheit).

---

## 🔹 Estruturas de Dados
- **Listas**
  - Criação, indexação, slicing, métodos (`append`, `pop`, `sort`).
- **Tuplas**
  - Imutabilidade, desempacotamento.
- **Dicionários**
  - Chaves e valores, métodos (`get`, `items`, `update`).
- **Conjuntos**
  - Operações de união, interseção, diferença.
- **Exercícios**
  - Lista de compras com lista.
  - Contador de palavras usando dicionário.
  - Conjunto de números únicos.

---

## 🔹 Orientação a Objetos
- **Classes e objetos**
  - `__init__`, atributos e métodos.
- **Encapsulamento**
  - Atributos privados, propriedades (`@property`).
- **Herança**
  - Superclasse e subclasses.
- **Polimorfismo**
  - Métodos sobrescritos.
- **Exercícios**
  - Classe `Pessoa` com nome e idade.
  - Classe `Aluno` herdando de `Pessoa`.
  - Interface `Animal` com métodos `falar()`.

---

## 🔹 Funções Avançadas
- **Funções de ordem superior**
  - `map`, `filter`, `reduce`.
- **Expressões lambda**
- **Decoradores**
- **Geradores**
  - `yield`, iteradores.
- **Exercícios**
  - Função que aplica `map` para dobrar números.
  - Decorador que mede tempo de execução.
  - Gerador de números pares.

---

## 🔹 Módulos e Pacotes
- **Importação**
  - `import`, `from ... import`.
- **Bibliotecas padrão**
  - `math`, `datetime`, `os`, `sys`.
- **Pacotes externos**
  - `requests`, `numpy`, `pandas`.
- **Exercícios**
  - Script que lê arquivos com `os`.
  - Programa que consome API com `requests`.

---

## 🔹 Testes e Qualidade
- **Testes**
  - `unittest`, `pytest`.
- **Lint e formatação**
  - `flake8`, `black`.
- **Exceções**
  - `try/except/finally`.
- **Exercícios**
  - Testar função de soma.
  - Tratar exceção de divisão por zero.

---

## 🔹 Web e APIs
- **HTTP básico**
  - `requests`.
- **Frameworks**
  - `Flask`, `FastAPI`, `Django`.
- **JSON**
  - `json` module.
- **Exercícios**
  - API simples com Flask.
  - CRUD de tarefas com FastAPI.

---

## 🔹 Banco de Dados
- **SQLite**
  - `sqlite3`.
- **ORM**
  - `SQLAlchemy`, `Django ORM`.
- **Exercícios**
  - CRUD de usuários com SQLite.
  - CRUD com SQLAlchemy.

---

## 🔹 Concorrência e Paralelismo
- **Threads**
  - `threading`.
- **Processos**
  - `multiprocessing`.
- **Async**
  - `asyncio`, `await`.
- **Exercícios**
  - Programa que roda duas funções em paralelo.
  - API assíncrona com `asyncio`.

---

## 🔹 Projetos de Consolidação
- **Projeto 1 — CLI**
  - Ferramenta que lê CSV e gera relatórios.
- **Projeto 2 — API REST**
  - CRUD completo com FastAPI + SQLAlchemy.
- **Projeto 3 — Data Science**
  - Análise de dataset com Pandas + Matplotlib.
- **Projeto 4 — Web App**
  - Aplicação Django com autenticação e banco de dados.

---

## 🔹 Dicas de Estudo
- Pratique diariamente com pequenos scripts.
- Leia código open source em Python (ex.: Flask, Pandas).
- Use `black` e `flake8` para manter código limpo.
- Prefira clareza e simplicidade.

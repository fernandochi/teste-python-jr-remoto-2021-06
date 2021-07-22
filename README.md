# Instruct - Magpy

## Sobre o Projeto

Esta é uma api de teste da Instruct, que funciona guardar informações sobre quais pacotes determinado projeto utiliza, e sua versão.

## Tabela de conteúdo

===========================

- [Como utilizar](#how)

- [Todos os projetos ](#Projetos)

  - [Projetos por nome](#ProjetoNome)

- [Criação de Projetos](#CriarProjetos)

- [Deletar projetos](#Deletar)

- [Testes](#testes)

- [Tecnologias](#techs)

=============================

#### :construction: Projeto em construção :nerd_face:

<h3 id='how'>Como utilizar</h3>

Esta API está hospedada no [Heroku](https://instruct-magpy.herokuapp.com/) para utilização remota.

####Localmente
Caso queira utilizar locamente é possível clonar este repositório e instalar as dependências do `Pipfile` em ambiente virtual

<h3 id="Projetos">Projetos</h3>

_Requisição_

```
GET /api/projects/
```

_Resposta_

```
status = 200

[
    {
    name: "Foo",
    packages: [
        {name: Django, version: 3.2.5},
        {name: panda, version: 0.3.1}
    ]
    }, {
    name: "Bar",
    packages: [
        {name:Flask, version: 2.0.0}
    ]
    }
]
```

<h3 id="ProjetoNome">Projetos por nome</h3>

_Requisição_

```
GET /api/projects/foo/
```

_Resposta_

```
status = 200
{
    name: "Foo"
    packages: [
        {name: Django, version: 3.2.5},
        {name: panda, version: 0.3.1}
    ]
}
```

<h3 id="CriarProjetos">Criar projeto</h3>

_Requisição_

```
POST /api/projects/

BODY = {
    name: "Baz"
    packages: [
        {name: django},
        {name: panda, version: 0.1.5}
    ]
}
```

Tanto _name_, quanto _packages_ são obrigatórios para criação de um projeto. Se nenhuma versão não for passada será utilizada a última versão do pacote.

_Resposta_

```
status = 201
{
    name: "Baz",
    packages: [
        {name: Django, version: 3.2.5},
        {name: panda, version: 0.1.5}
    ]
}
```

Caso um pacote ou versão do pacote não exitsir será retornado uma BAD_REQUEST

_Requisição_

```
POST /api/projects/

BODY = {
    name: "Baz"
    packages: [
        {name: abcdefzwyz}
    ]
}
```

_Resposta_

```
status = 400
{
    error: One or more packages does not exist
}
```

<h3 id="Deletar">Deletar projetos</h3>

_Requisição_

```
DELETE /api/projects/foo/
```

_Resposta_

```
stauts = 204
No body content
```

<h3 id="testes">Testes</h3>

Os testes da aplicação podem ser rodados com o comando `manage.py test`. Estes testes irão verificar o comportamento das models e views da aplicação

É possível também verificar com os testes do [k6](https://k6.io/). Basta o instalar e rodar o comando de test com o host correto:

```
k6 run -e API_BASE='http://localhost:8000/' tests-open.js
```

Cobertura de código = 94%

<h3 id='techs'>Tecnologias</h3>

- [Django](https://docs.djangoproject.com/)
- [Django rest_framework](https://www.django-rest-framework.org/)

<h2 id='me'>Autor</h2>

[![BADGE](https://img.shields.io/static/v1?label=github&message=Fernandochi&color=181717&style=social&logo=github&link=https://github.com/fernandochi)](https://github.com/fernandochi)
[![BADGE](https://img.shields.io/static/v1?label=linkedin&message=Fernando&color=0A66C2&style=social&logo=linkedin&link=https://www.linkedin.com/in/fernando-l-santos/)](https://www.linkedin.com/in/fernando-l-santos/)

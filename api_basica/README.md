# Projeto Django - API Simples

Este é um projeto Django que disponibiliza um endpoint de API para receber e responder dados via requisições GET e POST em formato JSON.

## Requisitos

- Python 3.12
- Django

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/projeto-django-api-simples.git
cd projeto-django-api-simples
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

## Executando o servidor

Inicie o servidor local:
```bash
python manage.py runserver
```

A API estará disponível em:
```
http://localhost:8000/meu-endpoint/
```

## Como usar o endpoint

### Requisição GET

**Método**: GET  
**URL**: `http://localhost:8000/meu-endpoint/`

**Resposta**:
```json
{
  "mensagem": "Você fez uma requisição GET"
}
```

Você pode testar acessando diretamente no navegador.

### Requisição POST

**Método**: POST  
**URL**: `http://localhost:8000/meu-endpoint/`  
**Cabeçalho**: `Content-Type: application/json`

**Corpo da requisição**:
```json
{
  "nome": "Seu Nome"
}
```

**Resposta**:
```json
{
  "mensagem": "Olá, Seu Nome! Você fez uma requisição POST"
}
```

## Testando a API

### Usando curl

**Para GET**:
```bash
curl http://localhost:8000/meu-endpoint/
```

**Para POST**:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"nome":"Seu Nome"}' http://localhost:8000/meu-endpoint/
```

### Usando ferramentas como Postman ou Insomnia

1. Configure uma nova requisição com o URL `http://localhost:8000/meu-endpoint/`
2. Para GET, apenas envie a requisição
3. Para POST, selecione o método POST, adicione o cabeçalho `Content-Type: application/json` e no corpo da requisição adicione o JSON com o campo "nome"

## Estrutura do projeto

```
projeto-django-api-simples/
├── api_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── projeto/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## Contribuição

1. Faça o fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

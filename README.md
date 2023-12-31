# API de Previsão do Tempo
## Descrição
Esta aplicação backend, desenvolvida em Python e FastAPI, oferece uma API para acessar previsões do tempo dos próximos cinco dias. Utilizando dados da API do OpenWeatherMap, a aplicação também armazena o histórico de consultas em um banco de dados MongoDB para referências futuras.

## Stack Tecnológica
- **Linguagem**: Python 3.9
- **Framework Web**: FastAPI
- **Servidor ASGI**: Uvicorn
- **Contêinerização**: Docker
- **Banco de Dados**: MongoDB

## Pré-requisitos
- Docker instalado em sua máquina.
- Chave de API do [OpenWeatherMap](https://openweathermap.org/).

## Configuração
1. Clone o repositório do projeto para sua máquina local.
2. Configure a chave de API do OpenWeatherMap como uma variável de ambiente. Para isso, crie um arquivo `.env` na raiz do projeto e adicione a seguinte linha:
    ```
    OPENWEATHER_API_KEY=sua_chave_de_api
    ```
3. Certifique-se de que o Docker esteja instalado e funcionando em sua máquina.

##  Rodando localmente
```bash
docker-compose up --build
```
## Parar
```
docker-compose down
```
## Swagger do projeto
```
 http://0.0.0.0:8000/docs#/
```
## Autor  

- [@eltonmeurer](https://www.linkedin.com/in/elton-meurer-174191229/)

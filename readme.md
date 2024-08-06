# Projeto Segunda

Assistente virtual S.E.G.U.N.D.A

## Pré requisitos

Para iniciar o projeto é necessario ativar e configurar o ambiente virtual com os seguintes comandos:
<details><summary>Windows</summary>

Criar o ambiente:
```
python -m venv venv
```

Inicializar o ambiente com o seguinte comando:

```
venv\scripts\activate
```

Instalar as dependencias presentes dentro do `requirements.txt`:

```
pip install -r requirements.txt
```
</details>

<details><summary>Linux</summary>

Criar o ambiente:
```
python3 -m venv venv
```

Inicializar o ambiente com o seguinte comando:
```
source venv/bin/activate
```
Instalar as dependencias presentes dentro do `requirements.txt`:

```
pip install -r requirements.txt
```
</details>

## Utilizar a ferramenta

Para utilizar, basta dar inicio a aplicação com o comando:

```
python main.py
```

Ele irá consumir a API do servidor S.E.G.U.N.D.A, que está hospedando a IA e funcionalidades com APIs especificas.

## Detalhamento da IA

Foi desenvolvido uma IA exclusivamente para o projeto S.E.G.U.N.D.A utilizando o framework [Pytorch](https://pytorch.org/) e a linguagem de programação [Python](https://www.python.org/). Para a comunicação com o servidor, foi criada uma API usando [Golang](https://go.dev/), e o framework [FastAPI](https://fastapi.tiangolo.com/) foi utilizado para o desenvolvimento da API.

### Teste da IA
 Para realizar testes de funcionamento da IA pode-se iniciar o outro codigo na raiz do projeto com o seguinte comando:
 ```
 python segunda.py
 ```
 Ele irá iniciar o processo de conversa com a IA atraves de um chatbot.
 Para encerrar o segunda naturalmente, basta digitar 'Adeus'


## Steps do projeto

Por se o inicio do desenvolvimento, há desafios funcionalidades e libs a serem implementadas.

- [X] Iniciar projeto

- [X] Definir proximos passos

- [X] Preparar IA para o projeto

    ### TODO funcionalidades

    - [X] Consulta de hora
    - [X] Saudações
    - [X] Teste de velocidade de internet
    - [ ] Piadas
    - [ ] Noticias
    - [ ] Jogos
    - [ ] Indicação de restaurantes proximos a mim
    - [ ] Envio de email
    - [X] Conte me sobre
    - [ ] Controle de volume
    - [X] Clima tempo
    - [ ] Mensagens do Whatsapp
    - [X] Youtube
    - [ ] Player de musica
    - [ ] Controle residencial
    - [ ] Indicações

- [X] Conectar features ao projeto principal
- [ ] IA preparada para tomadas de decisão
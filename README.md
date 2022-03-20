# Projeto Bot Telegram
 Bot Telegram densenvolvido durante o aprendizado e estudo da API do Telegram.

<center><img src="img\botfather.jpg" alt="Imagem do Botfather, que é uma referência do Padrinho de Poderoso Chefão" width="200px"/></center>

## Descrição do Projeto
Este bot está hospedado na plataforma [Heroku](https://www.heroku.com/) e pode ser acessado pelo link [t.me/wemix_draco_bot](https://t.me/wemix_draco_bot).
Para o desenvolvimento desse bot foi utilizado as API da [Telegram](https://core.telegram.org/bots/api) e o [Wemix](https://api.mir4global.com).

## Instalação
Este projeto usa a versão [Python 3.10](https://www.python.org/downloads/).

Para baixar e rodar este código, siga as etapas abaixo no seu terminal:

```
1. git clone https://github.com/Jefferson472/bot-telegram-wemix-draco.git
2. cd bot-telegram-wemix-draco
```

Instale as dependências do projeto:
```
3. pip install -r requirements.txt
```

Crie um arquivo .env e adicione as informações de acesso ao seu bot (para obter o Token verifique a documentação da [API do Telegram](https://core.telegram.org/bots/api#authorizing-your-bot):
```
3. TELEGRAM_TOKEN = 'token_string'
```

Para iniciar a aplicação, execute os códigos abaixo:
```
4. python bot.py
```

Agora basta acessar o seu bot pelo link fornecido pelo Botfather e digitar o comando /start.

## Outros Comandos

/start - O bot irá iniciar e se apresentar

/hello - O bot dirá Olá e o seu nome

/draco - O bot irá informar o preço do Draco

/hidra - O bot irá informar o preço da Hidra agora

---
## Imagens

<img src="img\tela_inicial.png" alt="Um print da tela inicial do bot direto do Telegram" width="400px"/>

<img src="img\comandos.png" alt="Um print da tela de comandos do bot direto do Telegram" width="400px"/>

from crypto_price import Crypto_Price


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Olá eu sou um bot!"
    )


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text
    )


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Desculpe, não entendi o que você quis dizer."
    )

def hello(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f'Hello {update.effective_user.first_name}'
    )


def draco_price(update, context) -> None:
    crypto_price = Crypto_Price()
    text_cotent = (crypto_price.get_draco_wemix_price())
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text_cotent
    )


def hidra_price(update, context) -> None:
    crypto_price = Crypto_Price()
    text_cotent = (crypto_price.get_hidra_wemix_price())
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text_cotent
    )

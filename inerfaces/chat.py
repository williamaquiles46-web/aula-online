import justpy as jp

def chat():
    wp = jp.WebPage()
    jp.H1(text="Chat Estudante-Professor", classes="text-2xl m-4", a=wp)

    chat_box = jp.Div(classes="border m-2 p-2 h-64 overflow-auto", a=wp)
    msg_input = jp.Input(placeholder="Digite sua mensagem...", classes="m-2 p-2 border w-3/4", a=wp)

    def enviar(btn, chat_box=chat_box):
        jp.Div(text=f"Você: {msg_input.value}", classes="m-1 p-1", a=chat_box)
        msg_input.value = ""

    jp.Button(text="Enviar", classes="bg-green-500 text-white m-2 p-2", a=wp, click=enviar)

    return wp

jp.justpy(chat)

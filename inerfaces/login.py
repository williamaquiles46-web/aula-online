import justpy as jp

def login():
    wp = jp.WebPage()
    jp.H1(text="Login", classes="text-2xl m-4", a=wp)

    user_input = jp.Input(placeholder="Usuário", classes="m-2 p-2 border", a=wp)
    pass_input = jp.Input(placeholder="Senha", type="password", classes="m-2 p-2 border", a=wp)

    msg = jp.Div(classes="m-2 p-2 text-red-600", a=wp)

    def autenticar(btn, msg=msg):
        if user_input.value == "admin" and pass_input.value == "123":
            msg.text = "✅ Login realizado com sucesso!"
        else:
            msg.text = "⚠ Usuário ou senha inválidos."

    jp.Button(text="Entrar", classes="bg-green-500 text-white m-2 p-2", a=wp, click=autenticar)

    return wp

jp.justpy(login)

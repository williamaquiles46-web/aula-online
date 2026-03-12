import justpy as jp
from controles.gerenciador_estudante import GerenciadorEstudante
from modolos.estudante import Estudante

gerenciador = GerenciadorEstudante()

def cadastro_estudante():
    wp = jp.WebPage()
    jp.H1(text="Cadastro de Estudante", classes="text-2xl m-4", a=wp)

    nome_input = jp.Input(placeholder="Nome", classes="m-2 p-2 border", a=wp)
    email_input = jp.Input(placeholder="Email", classes="m-2 p-2 border", a=wp)
    matricula_input = jp.Input(placeholder="Matrícula", classes="m-2 p-2 border", a=wp)

    msg = jp.Div(classes="m-2 p-2 text-green-600", a=wp)

    def cadastrar(btn, msg=msg):
        est = Estudante(nome_input.value, email_input.value, matricula_input.value)
        gerenciador.cadastrarEstudante(est)
        msg.text = f"✅ Estudante {est.getNome()} cadastrado com sucesso!"

    jp.Button(text="Cadastrar", classes="bg-blue-500 text-white m-2 p-2", a=wp, click=cadastrar)

    return wp

jp.justpy(cadastro_estudante)

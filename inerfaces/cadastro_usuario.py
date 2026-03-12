import justpy as jp
from modolos.estudante import Estudante
from modolos.professor import Professor
from controles.gerenciador_estudante import GerenciadorEstudante
from controles.gerenciador_professor import GerenciadorProfessor

ger_est = GerenciadorEstudante()
ger_prof = GerenciadorProfessor()

def cadastro_usuario():
    wp = jp.WebPage()
    jp.H1(text="Cadastro de Usuário", classes="text-2xl m-4", a=wp)

    tipo = jp.Select(a=wp, classes="m-2 p-2 border")
    jp.Option(text="Estudante", value="estudante", a=tipo)
    jp.Option(text="Professor", value="professor", a=tipo)

    nome = jp.Input(placeholder="Nome", classes="m-2 p-2 border", a=wp)
    email = jp.Input(placeholder="Email", classes="m-2 p-2 border", a=wp)
    extra = jp.Input(placeholder="Matrícula ou Especialidade", classes="m-2 p-2 border", a=wp)

    msg = jp.Div(classes="m-2 p-2 text-green-600", a=wp)

    def cadastrar(btn, msg=msg):
        if tipo.value == "estudante":
            est = Estudante(nome.value, email.value, extra.value)
            ger_est.cadastrarEstudante(est)
            msg.text = f"✅ Estudante {est.getNome()} cadastrado!"
        else:
            prof = Professor(nome.value, email.value, extra.value)
            ger_prof.cadastrarProfessor(prof)
            msg.text = f"✅ Professor {prof.getNome()} cadastrado!"

    jp.Button(text="Cadastrar", classes="bg-blue-500 text-white m-2 p-2", a=wp, click=cadastrar)
    return wp

jp.justpy(cadastro_usuario)

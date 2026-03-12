import justpy as jp
from controles.gerenciador_plataforma import GerenciadorPlataforma
from modolos.estudante import Estudante
from modolos.professor import Professor
from modolos.aula import Aula
from modolos.horario import Horario
from modolos.pagamento import Pagamento
from modolos.mentoria import Mentoria
from modolos.exercicio import Exercicio
from modolos.avaliacao import Avaliacao

# Fachada única para acessar todos os gerenciadores
plataforma = GerenciadorPlataforma()

class AulaOnlineApp:
    def __init__(self):
        self.aba_ativa = "dashboard"
        self.container_principal = None
        self.notificacao = None

    def avisar(self, msg, erro=False):
        """Notificação visual (Toast) profissional."""
        self.notificacao.text = msg
        cor = "bg-red-600" if erro else "bg-emerald-600"
        self.notificacao.classes = f"fixed top-5 right-5 p-4 rounded-lg shadow-2xl text-white z-50 {cor} block text-sm font-bold"

    async def navegar(self, msg):
        """Troca de aba e redesenha o conteúdo instantaneamente."""
        self.aba_ativa = msg.target.value
        await self.renderizar_tela(msg.page)

    async def renderizar_tela(self, page):
        """Limpa e reconstrói a área de conteúdo baseada na aba ativa."""
        self.container_principal.delete_components()
        try:
            # MAPEAMENTO DE TODOS OS MÓDULOS (Evita AttributeError)
            if self.aba_ativa == "dashboard": self.view_dashboard()
            elif self.aba_ativa == "estudantes": self.view_estudantes()
            elif self.aba_ativa == "professores": self.view_professores()
            elif self.aba_ativa == "aulas": self.view_aulas()
            elif self.aba_ativa == "mentorias": self.view_mentorias()
            elif self.aba_ativa == "exercicios": self.view_exercicios()
            elif self.aba_ativa == "avaliacoes": self.view_avaliacoes()
            elif self.aba_ativa == "financeiro": self.view_financeiro()
        except Exception as e:
            self.avisar(f"Erro no sistema: {str(e)}", erro=True)
        await page.update()

    # --- VIEWS DE CADASTRO E INTERAÇÃO ---

    def view_dashboard(self):
        jp.H1(a=self.container_principal, text="🏠 Painel Geral", classes="text-3xl font-black text-slate-800 mb-8")
        grid = jp.Div(a=self.container_principal, classes="grid grid-cols-1 md:grid-cols-4 gap-6")
        stats = [
            ("Estudantes", len(plataforma.getGerenciadorEstudante().getEstudantes()), "blue"),
            ("Professores", len(plataforma.getGerenciadorProfessor().getProfessores()), "purple"),
            ("Exercícios", len(plataforma.getGerenciadorExercicio().getExercicios()), "amber"),
            ("Aulas", len(plataforma.getGerenciadorAula().get_todas_aulas()), "emerald")
        ]
        for t, v, c in stats:
            card = jp.Div(a=grid, classes=f"p-6 bg-white border-l-8 border-{c}-500 rounded-xl shadow-md")
            jp.P(a=card, text=t, classes="text-xs font-bold text-slate-400 uppercase tracking-widest")
            jp.P(a=card, text=str(v), classes="text-3xl font-black text-slate-800")

    def view_estudantes(self):
        jp.H2(a=self.container_principal, text="👨‍🎓 Estudantes", classes="text-2xl font-bold text-slate-800 mb-6")
        f = jp.Div(a=self.container_principal, classes="bg-white p-6 rounded-xl shadow-md mb-8 grid grid-cols-1 md:grid-cols-3 gap-4")
        nome = jp.Input(a=f, placeholder="Nome", classes="border p-2 rounded text-slate-900 border-slate-300")
        matr = jp.Input(a=f, placeholder="Matrícula", classes="border p-2 rounded text-slate-900 border-slate-300")
        async def salvar(btn, msg):
            try:
                plataforma.getGerenciadorEstudante().cadastrarEstudante(Estudante(nome.value, "email@ufs.br", matr.value))
                self.avisar("Estudante cadastrado!")
                await self.renderizar_tela(msg.page)
            except Exception as e: self.avisar(str(e), True)
        jp.Button(a=f, text="Cadastrar Aluno", click=salvar, classes="bg-blue-600 text-white font-bold p-2 rounded")
        self.gerar_tabela_interativa(["Nome", "Matrícula"], plataforma.getGerenciadorEstudante().getEstudantes(), ["getNome", "getMatricula"], "estudante")

    def view_professores(self):
        jp.H2(a=self.container_principal, text="👨‍🏫 Professores", classes="text-2xl font-bold text-slate-800 mb-6")
        f = jp.Div(a=self.container_principal, classes="bg-white p-6 rounded-xl shadow-md mb-8 grid grid-cols-1 md:grid-cols-3 gap-4")
        nome = jp.Input(a=f, placeholder="Nome", classes="border p-2 rounded text-slate-900 border-slate-300")
        disc = jp.Input(a=f, placeholder="Disciplina", classes="border p-2 rounded text-slate-900 border-slate-300")
        async def salvar(btn, msg):
            try:
                p = Professor(nome.value, "p@ufs.br", "01", disc.value, "DEP")
                plataforma.getGerenciadorProfessor().cadastrarProfessor(p)
                self.avisar("Professor cadastrado!")
                await self.renderizar_tela(msg.page)
            except Exception as e: self.avisar(str(e), True)
        jp.Button(a=f, text="Salvar Professor", click=salvar, classes="bg-purple-600 text-white font-bold p-2 rounded")
        self.gerar_tabela_interativa(["Nome", "Disciplina"], plataforma.getGerenciadorProfessor().getProfessores(), ["getNome", "getDisciplina"], "professor")

    def view_aulas(self):
        jp.H2(a=self.container_principal, text="📅 Aulas", classes="text-2xl font-bold text-slate-800 mb-6")
        f = jp.Div(a=self.container_principal, classes="bg-white p-6 rounded-xl shadow-md mb-8 grid grid-cols-1 md:grid-cols-3 gap-4")
        sala = jp.Input(a=f, placeholder="Sala", classes="border p-2 rounded text-slate-900 border-slate-300")
        p_nome = jp.Input(a=f, placeholder="Nome do Professor", classes="border p-2 rounded text-slate-900 border-slate-300")
        async def salvar(btn, msg):
            try:
                prof = next((x for x in plataforma.getGerenciadorProfessor().getProfessores() if x.getNome().lower() == p_nome.value.lower()), None)
                if not prof: raise ValueError("Professor não encontrado.")
                h = Horario("Segunda", "08:00", "12:00")
                plataforma.getGerenciadorAula().cadastrarAula(Aula(prof, h, sala.value, 40))
                self.avisar("Aula agendada!")
                await self.renderizar_tela(msg.page)
            except Exception as e: self.avisar(str(e), True)
        jp.Button(a=f, text="Agendar Aula", click=salvar, classes="bg-emerald-600 text-white font-bold p-2 rounded")
        self.gerar_tabela_interativa(["Sala", "Professor"], plataforma.getGerenciadorAula().get_todas_aulas(), ["getSala", "getProfessor"], "aula")

    def view_mentorias(self):
        jp.H2(a=self.container_principal, text="🤝 Mentorias", classes="text-2xl font-bold text-slate-800 mb-6")
        f = jp.Div(a=self.container_principal, classes="bg-white p-6 rounded-xl shadow-md mb-8 grid grid-cols-1 md:grid-cols-3 gap-4")
        p_n = jp.Input(a=f, placeholder="Professor", classes="border p-2 rounded text-slate-900")
        e_n = jp.Input(a=f, placeholder="Estudante", classes="border p-2 rounded text-slate-900")
        tema = jp.Input(a=f, placeholder="Tema", classes="border p-2 rounded text-slate-900")
        async def agendar(btn, msg):
            try:
                p = next((x for x in plataforma.getGerenciadorProfessor().getProfessores() if x.getNome().lower() == p_n.value.lower()), None)
                e = next((x for x in plataforma.getGerenciadorEstudante().getEstudantes() if x.getNome().lower() == e_n.value.lower()), None)
                if not p or not e: raise ValueError("Professor ou Estudante não encontrado.")
                plataforma.getGerenciadorMentoria().cadastrarMentoria(Mentoria(p, e, tema.value, 60))
                self.avisar("Mentoria agendada!")
                await self.renderizar_tela(msg.page)
            except Exception as ex: self.avisar(str(ex), True)
        jp.Button(a=f, text="Agendar", click=agendar, classes="bg-indigo-600 text-white p-2 rounded")
        self.gerar_tabela_interativa(["Tema", "Professor"], plataforma.getGerenciadorMentoria().getMentorias(), ["getTema", "getProfessor"], "mentoria")

    def view_exercicios(self):
        jp.H2(a=self.container_principal, text="📝 Exercícios", classes="text-2xl font-bold text-slate-800 mb-6")
        f = jp.Div(a=self.container_principal, classes="bg-white p-6 rounded-xl shadow-md mb-8 grid grid-cols-1 md:grid-cols-3 gap-4")
        desc = jp.Input(a=f, placeholder="Descrição", classes="border p-2 rounded text-slate-900")
        dif = jp.Input(a=f, placeholder="Dificuldade", classes="border p-2 rounded text-slate-900")
        async def salvar(btn, msg):
            try:
                plataforma.getGerenciadorExercicio().cadastrarExercicio(Exercicio(desc.value, dif.value, "A"))
                self.avisar("Exercício adicionado!")
                await self.renderizar_tela(msg.page)
            except Exception as e: self.avisar(str(e), True)
        jp.Button(a=f, text="Adicionar", click=salvar, classes="bg-pink-600 text-white font-bold p-2 rounded")
        self.gerar_tabela_interativa(["Descrição", "Dificuldade"], plataforma.getGerenciadorExercicio().getExercicios(), ["getDescricao", "getDificuldade"], "exercicio")

    def view_avaliacoes(self):
        jp.H2(a=self.container_principal, text="🎓 Avaliações", classes="text-2xl font-bold text-slate-800 mb-6")
        f = jp.Div(a=self.container_principal, classes="bg-white p-6 rounded-xl shadow-md mb-8 grid grid-cols-1 md:grid-cols-4 gap-4")
        e_n = jp.Input(a=f, placeholder="Nome do Estudante", classes="border p-2 rounded text-slate-900")
        ex_d = jp.Input(a=f, placeholder="Descrição Exercício", classes="border p-2 rounded text-slate-900")
        nota = jp.Input(a=f, placeholder="Nota", type="number", classes="border p-2 rounded text-slate-900")
        async def salvar(btn, msg):
            try:
                est = next((x for x in plataforma.getGerenciadorEstudante().getEstudantes() if x.getNome().lower() == e_n.value.lower()), None)
                exe = next((x for x in plataforma.getGerenciadorExercicio().getExercicios() if x.getDescricao().lower() == ex_d.value.lower()), None)
                if not est or not exe: raise ValueError("Aluno ou Exercício não encontrado.")
                plataforma.getGerenciadorAvaliacao().cadastrarAvaliacoes(Avaliacao(est, exe, float(nota.value)))
                self.avisar("Nota lançada!")
                await self.renderizar_tela(msg.page)
            except Exception as e: self.avisar(str(e), True)
        jp.Button(a=f, text="Lançar Nota", click=salvar, classes="bg-rose-600 text-white font-bold p-2 rounded")
        self.gerar_tabela_interativa(["Estudante", "Nota"], plataforma.getGerenciadorAvaliacao().getAvaliacoes(), ["getEstudante", "getNota"], "avaliacao")

    def view_financeiro(self):
        jp.H2(a=self.container_principal, text="💰 Financeiro", classes="text-2xl font-bold text-slate-800 mb-6")
        f = jp.Div(a=self.container_principal, classes="bg-white p-6 rounded-xl shadow-md mb-8 grid grid-cols-1 md:grid-cols-3 gap-4")
        e_n = jp.Input(a=f, placeholder="Nome Estudante", classes="border p-2 rounded text-slate-900")
        valor = jp.Input(a=f, placeholder="Valor", type="number", classes="border p-2 rounded text-slate-900")
        async def pagar(btn, msg):
            try:
                est = next((x for x in plataforma.getGerenciadorEstudante().getEstudantes() if x.getNome().lower() == e_n.value.lower()), None)
                if not est: raise ValueError("Estudante não encontrado.")
                plataforma.getGerenciadorFinanceiro().registrarPagamento(Pagamento(est, float(valor.value)))
                self.avisar("Pagamento registrado!")
                await self.renderizar_tela(msg.page)
            except Exception as e: self.avisar(str(e), True)
        jp.Button(a=f, text="Registrar", click=pagar, classes="bg-amber-600 text-white font-bold p-2 rounded")
        self.gerar_tabela_interativa(["Estudante", "Valor"], plataforma.getGerenciadorFinanceiro().getPagamentos(), ["getEstudante", "getValor"], "financeiro")

    # --- TABELA INTERATIVA (POLIMORFISMO DE REMOÇÃO) ---
    def gerar_tabela_interativa(self, colunas, lista, metodos, tipo):
        if not lista:
            jp.P(a=self.container_principal, text="Nenhum registro encontrado.", classes="italic text-slate-400 mt-4")
            return
        t = jp.Table(a=self.container_principal, classes="w-full mt-6 bg-white shadow-xl rounded-xl")
        thead = jp.Thead(a=t, classes="bg-slate-900 text-white")
        tr_h = jp.Tr(a=thead)
        for col in colunas: jp.Th(a=tr_h, text=col, classes="p-4 text-left font-bold uppercase text-xs")
        jp.Th(a=tr_h, text="Ação", classes="p-4 text-center")
        tbody = jp.Tbody(a=t)
        for item in lista:
            tr = jp.Tr(a=tbody, classes="border-b hover:bg-slate-50")
            for met in metodos:
                val = getattr(item, met)()
                txt = val.getNome() if hasattr(val, 'getNome') else str(val)
                jp.Td(a=tr, text=txt, classes="p-4 text-slate-700 font-medium")
            td_acao = jp.Td(a=tr, classes="p-4 text-center")
            btn_del = jp.Button(a=td_acao, text="🗑️", classes="text-red-500 hover:scale-125 transition", alvo=item)
            async def remover(btn, msg):
                if tipo == "estudante": plataforma.getGerenciadorEstudante().removerEstudante(btn.alvo)
                elif tipo == "professor": plataforma.getGerenciadorProfessor().removerProfessor(btn.alvo)
                elif tipo == "aula": plataforma.getGerenciadorAula().removerAula(btn.alvo.getSala())
                elif tipo == "financeiro": plataforma.getGerenciadorFinanceiro().removerPagamento(btn.alvo)
                elif tipo == "exercicio": plataforma.getGerenciadorExercicio().removerExercicio(btn.alvo.getDescricao())
                elif tipo == "mentoria": plataforma.getGerenciadorMentoria().removerMentoria(btn.alvo)
                elif tipo == "avaliacao": plataforma.getGerenciadorAvaliacao().removerAvaliacao(btn.alvo.getEstudante())
                self.avisar("Removido!")
                await self.renderizar_tela(msg.page)
            btn_del.on('click', remover)

    def main_page(self):
        wp = jp.WebPage(title="Aula Online Pro", head_html='<script src="https://cdn.tailwindcss.com"></script>')
        layout = jp.Div(a=wp, classes="flex h-screen bg-slate-100 overflow-hidden")
        sidebar = jp.Div(a=layout, classes="w-72 bg-slate-900 text-white p-6 flex flex-col shadow-2xl overflow-y-auto")
        jp.Div(a=sidebar, text="AULA ONLINE", classes="text-2xl font-black text-blue-500 mb-8 border-b border-slate-700 pb-4")
        menus = [
            ("🏠 Página inicial", "dashboard"), ("👨‍🎓 Estudantes", "estudantes"), ("👨‍🏫 Professores", "professores"),
            ("📅 Aulas", "aulas"), ("🤝 Mentorias", "mentorias"), ("📝 Exercícios", "exercicios"),
            ("🎓 Avaliações", "avaliacoes"), ("💰 Financeiro", "financeiro")
        ]
        for texto, valor in menus:
            btn = jp.Button(a=sidebar, text=texto, value=valor, classes="w-full text-left p-3 mb-2 rounded hover:bg-slate-800 transition")
            btn.on('click', self.navegar)
        right_side = jp.Div(a=layout, classes="flex-1 flex flex-col")
        self.notificacao = jp.Div(a=right_side, text="", classes="hidden")
        self.container_principal = jp.Div(a=right_side, classes="p-10 flex-1 overflow-y-auto")
        self.view_dashboard()
        return wp

app_instance = AulaOnlineApp()
@jp.SetRoute("/")
def render(): return app_instance.main_page()
jp.justpy(port=8001)
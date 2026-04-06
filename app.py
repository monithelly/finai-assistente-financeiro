import streamlit as st
from functions import investimento, emprestimo

st.set_page_config(
    page_title="FinAI",
    page_icon="💰",
    layout="wide"
)

# -----------------------------
# ESTILO
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }

    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
        color: #f8fafc;
    }

    .subtitle {
        font-size: 1rem;
        color: #cbd5e1;
        margin-bottom: 1.5rem;
    }

    .info-box {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 18px;
        color: #e2e8f0;
    }

    .feature-card {
        background-color: #111827;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 12px;
    }

    .feature-card h4 {
        margin: 0 0 8px 0;
        color: #f8fafc;
    }

    .feature-card p {
        margin: 0;
        color: #cbd5e1;
        font-size: 0.95rem;
    }

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #1e293b;
        color: white;
        padding: 0.7rem 1rem;
        font-weight: 600;
    }

    .stButton > button:hover {
        border: 1px solid #475569;
        background-color: #334155;
        color: white;
    }

    section[data-testid="stSidebar"] {
        background-color: #020617;
        border-right: 1px solid #1e293b;
    }

    div[data-testid="stChatMessage"] {
        border-radius: 14px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# ESTADO
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_input" not in st.session_state:
    st.session_state.user_input = None

# -----------------------------
# FUNÇÃO RESPOSTA
# -----------------------------
def responder(user_input):
    texto = user_input.lower()

    if "investir" in texto or "investimento" in texto:
        valor = investimento(200, 0.01, 24)
        return (
            "Ótima escolha pensar no futuro financeiro.\n\n"
            "### Simulação de investimento\n"
            "- Valor mensal: **R$ 200**\n"
            "- Período: **24 meses**\n"
            "- Taxa usada: **1% ao mês**\n\n"
            f"**Resultado estimado: R$ {valor}**\n\n"
            "Essa simulação mostra como os juros compostos ajudam o dinheiro a crescer ao longo do tempo.\n\n"
            "⚠️ Esta é uma simulação educativa."
        )

    elif "emprestimo" in texto or "empréstimo" in texto:
        parcela = emprestimo(5000, 0.02, 12)
        return (
            "Vamos analisar esse cenário com cuidado.\n\n"
            "### Simulação de empréstimo\n"
            "- Valor solicitado: **R$ 5.000**\n"
            "- Taxa usada: **2% ao mês**\n"
            "- Prazo: **12 meses**\n\n"
            f"**Parcela estimada: R$ {parcela}**\n\n"
            "Empréstimos podem ajudar em emergências, mas é importante avaliar o impacto das parcelas no orçamento.\n\n"
            "⚠️ Esta é uma simulação educativa."
        )

    elif "cdi" in texto:
        return (
            "### O que é CDI?\n\n"
            "CDI é uma taxa de referência muito usada no mercado financeiro.\n\n"
            "Muitos investimentos informam sua rentabilidade como um percentual do CDI.\n"
            "Exemplo: **100% do CDI** significa que o investimento acompanha essa taxa.\n\n"
            "Ele é bastante usado para comparar aplicações de renda fixa."
        )

    elif "juros" in texto:
        return (
            "### O que são juros?\n\n"
            "Juros representam o custo ou rendimento do dinheiro ao longo do tempo.\n\n"
            "**Principais tipos:**\n"
            "- **Juros simples:** calculados só sobre o valor inicial\n"
            "- **Juros compostos:** calculados sobre o valor inicial + rendimentos acumulados\n\n"
            "Os juros compostos são os mais comuns em investimentos e financiamentos."
        )

    elif "cartao" in texto or "cartão" in texto:
        return (
            "### Como funciona o cartão de crédito?\n\n"
            "O cartão permite fazer compras agora e pagar depois, normalmente na data de vencimento da fatura.\n\n"
            "**Atenção:**\n"
            "- pagar o valor total evita juros\n"
            "- pagar só o mínimo pode gerar dívida cara\n\n"
            "Usado com planejamento, ele pode ser útil. Sem controle, pode virar problema."
        )

    elif "score" in texto:
        return (
            "### O que é score de crédito?\n\n"
            "Score é uma pontuação que indica como o mercado enxerga seu comportamento financeiro.\n\n"
            "Em geral, scores maiores podem facilitar acesso a crédito.\n\n"
            "Fatores comuns:\n"
            "- histórico de pagamentos\n"
            "- dívidas em aberto\n"
            "- relacionamento com instituições financeiras"
        )

    else:
        return (
            "Posso te ajudar com estes temas:\n\n"
            "- **investimento**\n"
            "- **empréstimo**\n"
            "- **CDI**\n"
            "- **juros**\n"
            "- **cartão de crédito**\n"
            "- **score**\n\n"
            "Experimente digitar algo como:\n"
            "- `quero investir`\n"
            "- `simular empréstimo`\n"
            "- `o que é CDI?`"
        )

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.markdown("## 💰 FinAI")
    st.caption("Assistente financeiro educativo")

    st.markdown("---")
    st.markdown("### Ações rápidas")

    if st.button("💰 Simular investimento"):
        st.session_state.user_input = "quero investir"

    if st.button("💳 Simular empréstimo"):
        st.session_state.user_input = "simular empréstimo"

    if st.button("📚 O que é CDI?"):
        st.session_state.user_input = "o que é cdi"

    if st.button("📈 Explicar juros"):
        st.session_state.user_input = "o que são juros"

    if st.button("💳 Como funciona cartão de crédito?"):
        st.session_state.user_input = "como funciona cartão de crédito"

    if st.button("🧹 Limpar conversa"):
        st.session_state.messages = []
        st.session_state.user_input = None
        st.rerun()

    st.markdown("---")
    st.markdown(
        """
        **Sobre o projeto**  
        Este assistente foi criado para apoiar o entendimento de conceitos financeiros
        de forma clara, segura e educativa.
        """
    )

# -----------------------------
# CABEÇALHO
# -----------------------------
st.markdown('<div class="main-title">FinAI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Seu assistente financeiro educativo com experiência conversacional moderna.</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="info-box">
        ⚠️ Este assistente apresenta simulações demonstrativas e explicações educativas.
        Ele não substitui orientação financeira profissional.
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# TELA INICIAL
# -----------------------------
if len(st.session_state.messages) == 0:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>💰 Investimentos</h4>
            <p>Entenda simulações básicas e visualize crescimento com juros compostos.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>💳 Empréstimos</h4>
            <p>Veja exemplos de parcelas e compreenda o impacto financeiro.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>📚 Educação financeira</h4>
            <p>Receba explicações claras sobre termos como CDI, juros e score.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Sugestões para começar")
    sug1, sug2, sug3 = st.columns(3)

    with sug1:
        if st.button("Quero investir"):
            st.session_state.user_input = "quero investir"

    with sug2:
        if st.button("Simular empréstimo"):
            st.session_state.user_input = "simular empréstimo"

    with sug3:
        if st.button("O que é CDI?"):
            st.session_state.user_input = "o que é cdi"

# -----------------------------
# CHAT INPUT
# -----------------------------
chat_text = st.chat_input("Digite sua dúvida financeira...")

if chat_text:
    st.session_state.user_input = chat_text

if st.session_state.user_input:
    user_input = st.session_state.user_input

    st.session_state.messages.append({"role": "user", "content": user_input})
    response_text = responder(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response_text})

    st.session_state.user_input = None
    st.rerun()

# -----------------------------
# RENDER CHAT
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
import streamlit as st

st.set_page_config(
    page_title="UPM - Ultimate Prediction Machine",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 ULTIMATE PREDICTION MACHINE")
st.caption("Advanced Sports Analysis | Football & Basketball")

sport = st.sidebar.selectbox(
    "Selecionar desporto",
    ["Futebol", "Basquetebol"]
)

st.sidebar.selectbox(
    "Competição",
    ["Todas as competições", "Selecionar competição"]
)

st.sidebar.selectbox(
    "Filtro de qualidade",
    ["Rigoroso"]
)

st.header("🌍 Radar Mundial")
st.info("Aguardando integração das fontes de jogos e estatísticas.")

if sport == "Futebol":
    st.subheader("⚽ Motor de Futebol")
    markets = [
        "Over/Under golos",
        "BTTS Sim/Não",
        "Golos por equipa",
        "Cantos totais e por equipa",
        "Resultado 1X2",
        "Dupla possibilidade"
    ]
else:
    st.subheader("🏀 Motor de Basquetebol")
    markets = [
        "Over/Under pontos",
        "Pontos por equipa",
        "Vencedor",
        "Handicap",
        "Totais por quarto"
    ]

st.subheader("Mercados disponíveis")
for market in markets:
    st.write("• " + market)

st.divider()

st.header("🔎 Análise individual por jogo")

team_a = st.text_input("Equipa da casa / Equipa A")
team_b = st.text_input("Equipa visitante / Equipa B")

if team_a and team_b:
    st.subheader(team_a + " vs " + team_b)

    st.write("### Visão geral dos mercados")

    for market in markets:
        st.write(market + " — Aguardando dados")

    selected_market = st.selectbox(
        "Escolher mercado para análise avançada",
        markets
    )

    st.write("### Análise avançada")
    st.write("Mercado selecionado:", selected_market)
    st.warning(
        "Ainda não existem previsões calculadas. "
        "Aguardando integração de dados e validação dos modelos."
    )

st.divider()

st.header("📊 Centro de controlo")
st.metric("Desportos", "2")
st.metric("Filtro de qualidade", "Rigoroso")
st.metric("Previsões validadas", "0")

st.caption(
    "UPM - Nenhuma previsão será aprovada sem dados "
    "suficientes e validação histórica."
)

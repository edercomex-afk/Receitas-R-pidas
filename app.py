import streamlit as st

st.set_page_config(page_title="Receitas Rápidas", page_icon="🍳")

# Banco de dados inicial (Independente)
dados_receitas = [
    {"nome": "Omelete de Queijo", "ingredientes": ["ovo", "queijo", "sal"], "preparo": "Bata os ovos, misture o queijo e frite em uma frigideira untada."},
    {"nome": "Arroz com Alho", "ingredientes": ["arroz", "alho", "azeite", "sal"], "preparo": "Refogue o alho no azeite, adicione o arroz e cubra com água quente até cozinhar."},
    {"nome": "Macarrão Alho e Óleo", "ingredientes": ["macarrao", "alho", "azeite", "sal"], "preparo": "Cozinhe o macarrão. Em outra panela, doure o alho no azeite e misture a massa."},
    {"nome": "Frango Grelhado", "ingredientes": ["frango", "limao", "sal"], "preparo": "Tempere o frango com limão e sal e grelhe até dourar."},
    {"nome": "Salada de Tomate", "ingredientes": ["tomate", "cebola", "azeite", "sal"], "preparo": "Pique o tomate e a cebola, misture e tempere com azeite e sal."}
]

st.title("🍳 Projeto: Receitas Rápidas")
st.write("Selecione o que você tem em casa e veja o que pode cozinhar!")

# Barra lateral para os ingredientes
st.sidebar.header("🛒 Sua Despensa")
# Criar uma lista única de todos os ingredientes disponíveis no banco
todos_ing = sorted(list(set([i for r in dados_receitas for i in r["ingredientes"]])))

selecionados = st.sidebar.multiselect("Ingredientes que você possui:", todos_ing)

if selecionados:
    st.subheader("📋 Sugestões de Receitas:")
    encontrou = False
    
    for receita in dados_receitas:
        # Verifica se o usuário tem TODOS os ingredientes daquela receita
        if all(item in selecionados for item in receita["ingredientes"]):
            with st.expander(f"✅ {receita['nome']}"):
                st.write(f"**Ingredientes:** {', '.join(receita['ingredientes'])}")
                st.write(f"**Modo de Preparo:** {receita['preparo']}")
            encontrou = True
            
    if not encontrou:
        st.warning("Puxa, com esses ingredientes exatos ainda não temos receitas. Tente selecionar temperos básicos como 'sal' ou 'azeite'!")
else:
    st.info("👈 Use a barra lateral para selecionar seus ingredientes!")

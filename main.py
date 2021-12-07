import streamlit as st
import style
import database as db

st.set_page_config(
  page_title="Ficha de membro",
  page_icon=":church:",
  layout="centered",
)
style.setStyle()

form = st.empty()
btnSalvar = st.empty()
#btnSalvar = False
pg2 = False

with form.container():
    st.write("This is inside the container")
    if st.button("Hide me!"):
        form.empty()
        var = True

with form.container():
    st.subheader('Para que serve esse formulário?')
    st.write('A ficha de membros serve para que tenhamos meios de contatos atualizados com todos os membros. Não se preocupe, seus dados estarão seguros com a gente!')
    st.write('Vale ressaltar que é muito importante cadastrar todos os membros, pois é assim que será feita a contagem de de presença para a assembléia, que só tem início quando a maioria estiver reunida.')

    st.write('\n')
    st.write('\n')
    st.write('\n')

    qnt_membros = int(st.number_input('Informe a quantidade de membros que deseja cadastrar', step=1, min_value=0, max_value=15))
    listaGrupoMembros = []

    for i in range(qnt_membros):
        st.markdown("***")
        dadosMembro =[]
        if qnt_membros > 1:
            st.subheader(f'{i+1}° membro:')
        dadosMembro.append(st.text_input('Nome Completo', key=f'nome{i}'))
        dadosMembro.append(st.text_input('Data de nascimento', key=f'dtNasc{i}'))
        dadosMembro.append(st.text_input('Telefone (Whatsapp)', key=f'telefone{i}'))
        dadosMembro.append(st.text_input('E-mail', key=f'email{i}'))
        listaGrupoMembros.append(dadosMembro)
    if qnt_membros > 0:
        st.markdown("***")
    st.write('\n')
    #st.text(listaGrupoMembros)

    if qnt_membros > 0 and "''"  in str(listaGrupoMembros):
        st.warning('Por favor, preencha todos os campos antes de prosseguir!')

    if qnt_membros > 0:
        with btnSalvar:
            if st.button("Salvar"):
                btnSalvar.empty()
                form.empty()
                #btnSalvar = True
                pg2 = True

if pg2:
    db.salvarFicha(listaGrupoMembros)
    st.header('Ficha atualizada com sucesso!')
    st.write("[Clique aqui](https://youtube.com/QuadrangularDoAlto) para assistir a assembéia.")

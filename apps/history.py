import streamlit as st


def app():
    st.markdown("""---""")

    if "key" in st.session_state:
        for i in st.session_state['key']:
            for k, v in i.items():
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.success(k)
                with col2:
                    st.info(v)


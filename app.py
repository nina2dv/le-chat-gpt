from streamlit_login_auth_ui.widgets import __login__
import streamlit as st
from multipage import MultiPage
from apps import home, history


app = MultiPage()
st.set_page_config(page_title="Le Chat-GPT", page_icon="cat")
st.title('Le Chat-GPT 🐈')

__login__obj = __login__(auth_token = st.secrets['API'],
                    company_name = "Shims",
                    width = 200, height = 250,
                    logout_button_name = 'Logout', hide_menu_bool = False,
                    hide_footer_bool = True,
                    lottie_url = 'https://assets8.lottiefiles.com/packages/lf20_bzNe5b.json')

LOGGED_IN= __login__obj.build_login_ui()
username= __login__obj.get_username()

if LOGGED_IN == True:
  
   # Streamlit Application
   # st.markdown(st.session_state)
  st.markdown(f"##### Hello _*{username}*_")

  # st.markdown("""---""")
  # Applications
  app.add_app("Home", home.app)
  app.add_app("History", history.app)
  app.run()
                                      

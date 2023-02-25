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
  
   # st.markdown("Your Streamlit Application Begins here!")
   # st.markdown(st.session_state)
   # st.write(username)
  with st.expander("About me"):
      st.write("Meow!")
      st.write("Ask me anything!")
      st.markdown(
         """
         Example Prompts:
         - What would you do if ...?
         - There is cat food nearby.
         - What do you think of ...?
         """
      )

      st.warning(
         "Be aware! Some of the most toxic food for cats include onions & garlic, raw eggs & meat, bones, chocolate, caffeinated beverages, raw dough, dairy products, alcohol, grapes and raisins.")
  st.markdown("""---""")
  # Add all your application here
  app.add_app("Home", home.app)
  app.add_app("History", history.app)
  app.run()
                                      

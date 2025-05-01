import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar


def home():
    st.write("The start of a streamlit project")


def kpop():
    st.write("A K-Pop Page")


def pop():
    st.write("A Pop Page")


def about():
    with st.expander("About Me: Name"):
        st.write("This is all about me")
    with st.expander("About Me: Name 2"):
        st.write("This is all about me (person 2)")
    st.write("These are our contact details for if you need to contact us")
    st.write("abc123@email.com")




selected = option_menu(
    menu_title = "Navigation",
    options = ["Home", "K-Pop", "Pop", "About"],
    icons = ["house", "person-add", "person", "book"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal",
)

if selected == "Home":
    st.title(f"{selected}")
    home()
    
if selected == "K-Pop":
    st.title(f"{selected}")
    kpop()

if selected == "Pop":
    st.title(f"{selected}")
    pop()

if selected == "About":
    st.title(f"{selected} Page")
    about()








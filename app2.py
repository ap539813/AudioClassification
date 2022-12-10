import altair as alt
import streamlit as st

# importing the local modules
from assets import css_file_path
from application_pages import main, homepage
from add_style import local_css
import tensorflow as tf

from PIL import Image


## Basic setup and app layout
st.set_page_config(layout="wide")

alt.renderers.set_embed_options(scaleFactor=2)


local_css(css_file_path)

print(st.session_state)

if 'home_page' not in st.session_state:
    st.session_state['home_page'] = True

    


if __name__ == '__main__':
    if st.session_state['home_page']:
        homepage()
    else:
        main()


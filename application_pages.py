import streamlit as st
from assets import theme_image_name, Support_Vector_Regressor, Random_Forest_Regressor
from prediction import make_prediction

def main():
    st.sidebar.markdown(
    f'<img style="max-width: 100%; height: auto;" src="data:image/gif;base64,{theme_image_name}" alt="homepage gif">',
    unsafe_allow_html=True,
)

    st.sidebar.title("Control Panel")

    type_model = st.sidebar.radio("Select Type of Model: ", ('Support Vector Regressor', 'Random Forest Regressor'))

    # if type_model == 'Data Visualization':
    #     st.title(f"Data Visualization")
    #     show()

    if type_model == 'Support Vector Regressor':
        st.title(f"Voice Authentication Using {type_model}")
        st.write('**Click the Button saying "Click to record" to start recording, to stop recording press the same button again. The usage instruction must be on the button as well**')

        make_prediction(Support_Vector_Regressor)

    elif type_model == 'Random Forest Regressor':
        st.title(f"Voice Authentication Using {type_model}")
        st.write('**Click the Button saying "Click to record" to start recording, to stop recording press the same button again. The usage instruction must be on the button as well**')

        make_prediction(Random_Forest_Regressor)

    

def homepage():
    home_image = st.markdown(
    f'<img style="max-width: 100%; height: auto;" src="data:image/gif;base64,{theme_image_name}" alt="homepage gif">',
    unsafe_allow_html=True,
)

    c1, c2, c3 = st.columns([2,1,2])


    c2.markdown('')
    c2.markdown('')
    continue_forward = c2.button('Authenticate >>>')

    st.session_state['home_page'] = False    

    if continue_forward:
        print('going to the application!!')
        home_image.empty()
        main()



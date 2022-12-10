
from create_models import load_model, get_results
from process_data import scale_data, get_label
from assets import column_names, mode_data, months, neighbourhood, object_cols
from assets import division, location_type, premises_type, ucr_code, ucr_ext, offence
import streamlit as st
import pandas as pd
import pickle
import datetime

from audiorecorder import audiorecorder


def make_prediction(model_path):
    model = load_model(model_path)
    c11, c12 = st.columns([1, 1])
    c11.markdown('### Show model performance: ')
    if c12.checkbox(''):
        get_results(model)
    else:
        st.title("Audio Recorder")
        audio = audiorecorder("Click to record", "Recording click to stop...")
        if len(audio) > 0:
            # To play audio in frontend:
            st.audio(audio)
            
            # To save audio to a file:
            wav_file = open("audio.wav", "wb")
            wav_file.write(audio.tobytes())

            st.button('Authenticate')
        # print(result)
        # input_X = 
        # X = pd.DataFrame(input_X)
        # encoders = pickle.load(open('saved_models/LabelEncoder', 'rb'))
        # for col in object_cols:
        #     X[col] = encoders[col].transform(X[col])
        
        # predict = st.button('Make Prediction >>>')
        # if predict:
        #     X = scale_data(X)
        #     pred = get_label(model.predict(X)[0])


        #     st.success(f'The Predicted label is: {pred}')

        
        
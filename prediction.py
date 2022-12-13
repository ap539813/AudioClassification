
from create_models import load_model
from process_data import scale_data
import streamlit as st

from audiorecorder import audiorecorder
# import speech_recognition as sr



def make_prediction(model_path):
    model = load_model(model_path)
    c11, c12 = st.columns([1, 1])
    # c11.markdown('### Show model performance: ')
    # if c12.checkbox(''):
    #     get_results(model)
    if True:
        st.title("Audio Recorder")
        audio = audiorecorder("Click to record", "Recording click to stop...")
        # r = sr.Recognizer()
        

        # text = r.recognize_google(audio)
        # print('Converting audio transcripts into text ...')
        # st.write(text)
        if len(audio) <= 0:
            pass
        elif (len(audio) <= 64082/2) and (len(audio) > 0):
            st.warning('The audio was too short!!! Record again.')
        else:
            # To play audio in frontend:
            st.audio(audio)
            
            # To save audio to a file:
            wav_file = open("sample_collected/audio.wav", "wb")
            wav_file.write(audio.tobytes())
            wav_file.close()

            st.write(audio.max())

            predict = st.button('Authenticate')
            if predict:
                X = scale_data(audio.reshape(1, -1))
                st.write(X.max())
                pred = model.predict(X)[0]

                st.success(f'The age of the speeker is close to: {round(pred)}')

        
        
# defined function to load the model

import pickle



def load_model(model_path):
    model = pickle.load(open(model_path, 'rb'))
    return model


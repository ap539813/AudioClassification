import pickle
from assets import standerdscaler


def scale_data(data):
    scaler = pickle.load(open(standerdscaler, 'rb'))
    return scaler.transform(data[:, :len(scaler.get_feature_names_out())])



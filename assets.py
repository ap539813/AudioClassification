import base64

Random_Forest_Regressor = 'saved_models/RandomForestRegressor(n_estimators=1'
Support_Vector_Regressor = 'saved_models/SVR'
standerdscaler = 'saved_models/StandardScaler'

data_url = 'assets_files/VoiceAuthentication.gif'
file_ = open(data_url, "rb")
contents = file_.read()
theme_image_name = base64.b64encode(contents).decode("utf-8")
file_.close()



css_file_path = 'style/style.css'
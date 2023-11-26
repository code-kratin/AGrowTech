from flask import Flask, render_template, jsonify, request
from model import predict_image
import pickle
import utils
import requests
import config
import numpy as np
import pandas as pd
from markupsafe import Markup
Markup()

app = Flask(__name__)

crop_recommendation_model_path = 'D:\spectragrow\models\LGBMClassifier.pkl'
# fert_recommendation_model_path = 'models/classifier.pkl'
fert_recommendation_model_path = 'D:\spectragrow\models\classifier.pkl'
fert2_recommendation_model_path= 'D:\spectragrow\models\\fertilizer.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))
model = pickle.load(
    open(fert_recommendation_model_path, 'rb'))
ferti = pickle.load(
    open(fert2_recommendation_model_path, 'rb'))

def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + "10436c6acff0c83f9ea4b3a2558ff8a6" + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None

ph_val=0
rain_val=0
def getloc():
    url2="https://ipinfo.io/json?token=eb8939ae17feee"
    response=requests.get(url2)
    data2=response.json()
    state=data2["region"]
    ph_val=utils.features[state]["ph"]
    rain_val=utils.features[state]["rain"]
    print(ph_val, "   ", rain_val)
        # weatherPart.querySelector(".ph span").innerText=ph_val;
        # weatherPart.querySelector(".rain span").innerText=`${rain_val}mm`;
    


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Crop Recommendation'
    return render_template('crop.html', title=title)

@app.route('/irrigation')
def irrigation():
    return render_template('irrigation.html')

@app.route('/fertilizer')
def fert_recommend():
    return render_template('fertilizer.html')

@app.route('/map')
def map():
    return render_template('test.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)
            print(prediction)
            res = Markup(utils.disease_dic[prediction])
            return render_template('display.html', status=200, result=res)
        except:
            pass
    return render_template('index.html', status=500, res="Internal Server Error")

@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        getloc()
        # ph = float(request.form['ph'])
        # rainfall = float(request.form['rainfall'])
        ph=ph_val
        rainfall=rain_val
        # state = request.form.get("stt")
        city = str(request.form['city'])

        if weather_fetch(city) != None:
            temperature, humidity = weather_fetch(city)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]

            return render_template('crop-result.html', prediction=final_prediction, title=title)

        else:

            return render_template('try_again.html', title=title)



@app.route('/fert-predict',methods=['POST'])
def fert_predict():
    title = 'Fertilizer Recommendation'
    city = request.form.get('city')
    mois = request.form.get('mois')
    soil = request.form.get('soil')
    crop = request.form.get('crop')
    N = int(request.form['nitrogen'])
    P = int(request.form['phosphorous'])
    K = int(request.form['pottasium'])
    if weather_fetch(city) != None:
            temp, humi = weather_fetch(city)

            input = [int(temp),int(humi),int(mois),int(soil),int(crop),int(N),int(K),int(P)]

            res = ferti.classes_[model.predict([input])]

            Nhigh=40
            Nlow=40
            Phigh=50
            Plow=25
            Khigh=80
            Klow=40
            result=""

            if N==Nlow:
                result="Nitrogen content is adequate"
            if P>Plow and P<Phigh:
                result="Phosphorus content is adequate"
            if K>Klow and K<Khigh:
                result="Potassium content is adequate"

            if N>Nhigh:
                result=utils.fertilizer_dic['NHigh']
            elif N<Nlow:
                result=utils.fertilizer_dic['Nlow']
            
            if P>Phigh:
                result=utils.fertilizer_dic['PHigh']
            elif P<Plow:
                result=utils.fertilizer_dic['Plow']
            
            if K>Khigh:
                result=utils.fertilizer_dic['KHigh']
            elif K<Klow:
                result=utils.fertilizer_dic['Klow']
            
            result=Markup(result)
            # return render_template('crop-result.html', prediction=final_prediction, title=title)
            return render_template('fertilizer-result.html',x = ('Predicted Fertilizer is {}'.format(res)), y=result)

    else:

            return render_template('try_again.html', title=title)
    


if __name__ == "__main__":
    app.run(debug=True)

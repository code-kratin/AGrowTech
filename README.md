<div align="center">


### <a href="" target="_blank">AgrowTech</a>


 </div>

## Description

Food security for billions of people on earth requires minimizing crop damage by timely detection of diseases.Developing methods
for detection of plant diseases serves the dual purpose of increasing crop yield and reducing pesticide use without knowing
about the proper disease. Along with development of better crop varieties, disease detection is thus paramount goal for achieving
food security. The traditional method of disease detection has been to use manual examination by either farmers or experts, which
can be time consuming and costly, proving infeasible for millions of small and medium sized farms around the world.

This project is an approach to the development of plant disease recognition model, based on leaf image classification, by the
use of deep convolutional networks. The developed model is able to recognize 38 different types of plant diseases out of of 14 different plants with the ability to distinguish plant leaves from their surroundings.

🌱 AGrowTech: Revolutionizing Agricultural Growth

AGrowTech is not just a software; it's a commitment to merge cutting-edge technology with the very foundations of agriculture, aiming to enhance productivity in the agricultural sector. Leveraging Machine Learning, Deep Learning, and Full Stack Web Development through Python Flask, AGrowTech introduces a suite of features tailored for farmers and agricultural enthusiasts.

Key Features:

Crop Disease Prediction:

Utilizing Deep Learning Resnet34 CNN Model trained on over a lakh images of crop diseases.
Predicts diseases from crop leaf photos for a variety of crops such as Tomato, Strawberry, Peach, Potato, Pepper, Orange, Corn, Cherry, Apple, and more.
Users can easily upload images, identify the cause of the disease, and receive prevention recommendations.
Crop Recommendation:

Employs LGBM Classifier to recommend crops based on real-time weather conditions (moisture, humidity, rain mm) and NPK values (Nitrogen, Phosphorous, Potassium) of the soil.
Fetches weather conditions from OpenWeatherAPI, enabling users to receive personalized crop recommendations by entering their area and soil details.
Fertilizer Prediction:

Predicts the most suitable fertilizer based on real-time weather conditions, NPK values, soil type, and the chosen crop.
Ensures optimal fertilizer usage for improved crop growth and productivity.
Map:

Interactive Indian map displaying soil details such as pH and rain content in mm for each state.
Valuable for understanding regional weather and soil characteristics, facilitating informed decisions at both individual and production levels.
Government Schemes for Farmers:

Provides information on government schemes tailored for farmers, ensuring accessibility to crucial resources and support.
Tech Stack:

Machine Learning: LGBM Classifier, Resnet 34 CNN Model (PyTorch library)
Web Development: HTML, CSS, JavaScript, Python Flask
APIs: OpenWeatherAPI, CountryMapAPI for map integration
Why AGrowTech:

Precision Farming: Tailored recommendations for crop diseases, selection, and fertilization.
Real-time Insights: Access to up-to-date weather and soil information for informed decision-making.
Empowering Farmers: Government schemes and comprehensive data to support farmers.
AGrowTech is not just transforming agriculture; it's empowering those who feed the world. Join us in cultivating a sustainable future.

## Leaf Image Classification

## <img src="./Assets/batch.png" alt="batch of image"/>


## Usage:

- `Flask` : Code for Flask Server and deployment
- `TestImages` : Sample image for model testing
- `Src` : All The source code for building models
- `Models` : All the Pretrained Models of Pytorch





import pickle
import os

input = [[-1.44798723, -0.45602336, -1.36665103, -1.15012411,  0.72871411,
         0.70042803,  2.81483311, -0.13333286,  1.09302444,  2.5038276 ,
        -0.28069568, -0.04146398, -0.48565435, -0.49871449,  0.83604093,
         3.38589232,  9.01560288,  3.47515764,  2.594434  ,  2.1802771 ,
        -1.2340441 , -0.4929645 , -1.24389273, -0.97719402,  0.69398379,
         1.15926893,  4.7006688 ,  0.91959172,  2.14719008,  1.85943247]]

def predict() :
    #file_path = "C:\\Users\\KHALID\\Desktop\\FlaskApp\\models\\model.pkl"
    file_path = "..\models\model.pkl"
    file = open(file_path,"rb")
    model = pickle.load(file)
    
    prediction = model.predict(input)
    return str(prediction[0])

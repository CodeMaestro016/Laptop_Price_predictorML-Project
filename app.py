# Flask import kara ganna ona
from flask import Flask, render_template, request
import pickle
import numpy as np

#application ek setup karagamu
app = Flask(__name__)

#web pages hadagamu
"""
@app.route('/')
def index():
    return "Hello Piyumal"
"""

def prediction(list):
    filename = 'model/predictor.pickle'
    with open(filename,  'rb') as file:
        model = pickle.load(file)
        predict = model.predict([list])
        return predict


@app.route('/', methods = ['POST', 'GET'])
def index():
    predict = 0
    if request.method == 'POST':
        ram = request.form['ram']
        weight = request.form['weight']
        company = request.form['company']
        typename = request.form['typename']
        opsys = request.form['opsys']
        cpu = request.form['cpuname']
        gpu = request.form['gpuname']
        touchscreen = request.form.getlist('touchscreen')
        ips = request.form.getlist('ips')
        
        featureList = []
        featureList.append(int(ram))
        featureList.append(float(weight))
        featureList.append(len(touchscreen))
        featureList.append(len(ips))
        company_list = ['acer','apple','asus','dell','hp','lenovo','msi','other','toshiba']
        typename_list = ['2in1convertible','gaming','netbook','notebook','ultrabook','workstation']
        opsys_list = ['linux','mac','other','windows']
        cpu_list = ['amd','intelcorei3','intelcorei5','intelcorei7','other']
        gpu_list = ['amd','intel','nvidia']

       

        def travers(list, value):
            for item in list:
                if item == value:
                    featureList.append(1)
                else:
                    featureList.append(0)
        travers(company_list,company) 
        travers(typename_list, typename ) 
        travers(opsys_list, opsys) 
        travers(cpu_list, cpu)    
        travers(gpu_list, gpu) 

        predict = prediction(featureList) 
        predict = np.round(predict[0],2)*306

      

    return render_template("index.html" ,predict = predict)

if __name__ == '__main__':
    app.run(debug=True)  #api dn run karanna file name ekt call karanna ona "python app.py"


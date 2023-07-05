from flask import Flask,request,render_template,jsonify
import utils
from utils import Fish_weight_prediction
import config

app=Flask(__name__)

@app.route('/fish_weight')
def home():
    return render_template('fish_weight.html')

@app.route('/predict_weight',methods=['GET','POST'])
def predict_weight():
    if request.method=='GET':
        data=request.args.get
        Length1=float(data('Length1'))
        Length2=float(data('Length2'))
        Length3=float(data('Length3'))
        Height=float(data('Height'))
        Width=float(data('Width'))
        Species=data('Species')

        obj=Fish_weight_prediction(Length1,Length2,Length3,Height,Width,Species)
        pred_wt=obj.input_array()
        return render_template('fish_weight.html',prediction=pred_wt)
    
    elif request.method=='POST':
        data=request.form
        print("Data :",data)
        Length1=float(data['Length1'])
        Length2=float(data['Length2'])
        Length3=float(data['Length3'])
        Height=float(data['Height'])
        Width=float(data['Width'])
        Species=data['Species']

        obj=Fish_weight_prediction(Length1,Length2,Length3,Height,Width,Species)
        pred_wt=obj.input_array()
        return render_template('fish_weight.html',prediction=pred_wt)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)

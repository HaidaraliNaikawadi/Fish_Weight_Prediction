import numpy as np
import pickle
import json
import config

class Fish_weight_prediction():
    def __init__(self,Length1,Length2,Length3,Height,Width,Species):
        self.Length1=Length1
        self.Length2=Length2
        self.Length3=Length3
        self.Height=Height
        self.Width=Width
        self.Species=Species

    def Load_data(self):
        with open(config.json_file_path,'r') as f:
            self.json_data=json.load(f)

        with open(config.model_file_path,'rb') as f:
            self.model=pickle.load(f)

    def input_array(self):
        
        self.Load_data()
        Species_name='Species_'+self.Species
        Species_index=self.json_data['Column_list'].index(Species_name)
        Species_index
        test_array=np.zeros([1,len(self.json_data['Column_list'])])
        test_array[0][0]=self.Length1
        test_array[0][1]=self.Length2
        test_array[0][2]=self.Length3
        test_array[0][3]=self.Height
        test_array[0][4]=self.Width
        test_array[0][Species_index]=1

        predicted_weight=np.round(self.model.predict(test_array)[0],3)
        return predicted_weight
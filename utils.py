
import warnings
warnings.filterwarnings("ignore")
import pickle
import json
import numpy as np
import pandas as pd

class Laptop_Price():
    def __init__(self,processor_brand,processor_name,ram_gb,ssd,hdd,os,graphic_card_gb,Touchscreen,brand,
                 processor_gnrtn):
               
        self.processor_brand =  processor_brand
        self.processor_name =  processor_name
        self.ram_gb = ram_gb
        self.ssd = ssd
        self.hdd = hdd 
        self.os = os
        self.graphic_card_gb = graphic_card_gb
        self.Touchscreen = Touchscreen
        self.brand = "brand_" + brand
        self.processor_gnrtn = "processor_gnrtn_" + processor_gnrtn
        
    def load_data(self):
        with open("model.pkl","rb") as r:
            self.model = pickle.load(r)
            
        with open("pro_data.json","r") as e:
            self.data = json.load(e)
            
    def lap_price(self):
        self.load_data()   
         
        processor_gnrtn_index = self.data["col"].index(self.processor_gnrtn)
        brand_index = self.data["col"].index(self.brand)
       
        array = np.zeros([1,len(self.data["col"])])
        
        array[0][0] = self.data["processor_brand"][self.processor_brand]
        array[0][1] = self.data["processor_name"][self.processor_name]
        array[0][2] = self.ram_gb
        array[0][3] = self.ssd
        array[0][4] = self.hdd
        array[0][5] = self.data["os"][self.os]
        array[0][6] = self.graphic_card_gb
        array[0][7] = self.data["Touchscreen"][self.Touchscreen]
        
        array[0,brand_index] = 1
        array[0,processor_gnrtn_index] = 1

        price = self.model.predict(array)[0].round()
        return price
    
obj = Laptop_Price("Intel","Core i5",4,250,500,"Windows",2,"No","DELL","4th")
obj.lap_price()

# SUGGESTION **
# OS
# Touchscreen
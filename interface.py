from flask import Flask , jsonify , render_template , request
from utils import Laptop_Price # lap_price
import config

app = Flask(__name__)

@app.route("/")
def home():
   
    return render_template("index.html")

@app.route("/Prediction",methods = ["GET","POST"])
def prediction():

    if request.method == "POST":

        data = request.form
        processor_brand =  data["processor_brand"]
        processor_name =  data["processor_name"]
        ram_gb = data["ram_gb"]
        ssd = data["ssd"]
        hdd = data["hdd"]
        os = data["os"]
        graphic_card_gb = data["graphic_card_gb"]
        Touchscreen = data["Touchscreen"]
        brand = data["brand"]
        processor_gnrtn = data["processor_gnrtn"]

        obj = Laptop_Price(processor_brand,processor_name,ram_gb,ssd,hdd,os,graphic_card_gb,
                           Touchscreen,brand,processor_gnrtn)
        
        pred = obj.lap_price()
        return jsonify({"Approximate Laptop Price":pred})
    
    

    elif request.method == "GET":

        data = request.args.get

        processor_brand =  data("processor_brand")
        processor_name =  data("processor_name")
        
        ram_gb = data("ram_gb")
        ssd = data("ssd")
        hdd = data("hdd")
        os = data("os")
        graphic_card_gb = data("graphic_card_gb")
        Touchscreen = data("Touchscreen")
        brand = data("brand")
        processor_gnrtn = data("processor_gnrtn")

        obj = Laptop_Price(processor_brand,processor_name,ram_gb,ssd,hdd,os,graphic_card_gb,
                           Touchscreen,brand,processor_gnrtn)
        
        pr = obj.lap_price()
        return render_template("index.html",R = pr)
    return jsonify({"METHOD":"NO GET & POST"})

if __name__ == "__main__":
    app.run(host=config.HOST_NO, port=config.PORT_NO, debug = False)

#from curses import ACS_GEQUAL
from datetime import date
from http import client
#from xmlrpc.client import _DateTimeComparable
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from prediction_model import predict_covid

# parameters = {
#     "patient_name": "John Doeeeeeeeee",
#     "procedure_date": "12/00/21 1400hrs",
#     "age": 22,
#     "sex": "M",
#     "doctor_name": "Jane Doeeeeeeeee",
#     "institution": "AIIMS",
#     "reported_time": "12/03/21 1430hrs",
# }

app = Flask(__name__)
CORS(app, resources={r"/reportUpload": {"origins": "*"}})

@app.route("/")
def hello():
    return "Hello Aviroop"

@app.route('/reportUpload', methods=['POST'])
def reportUpload():
    if (request.method == 'POST'):
        print("image: ", request.files['file'])
        print("form: ", request.form)
        patient_name = request.form['patient_name']
        age = request.form['age']
        sex = request.form['sex']
        doctor_name = request.form['doctor_name']
        institution = request.form['institution']
        date = request.form['date']
        time = request.form['time']
        low_contrast = request.form['low_contrast']
        image = request.files['file']
        
        parameters = {
            "patient_name": patient_name,
            "procedure_date": date,
            "age": age,
            "sex": sex,
            "doctor_name": doctor_name,
            "institution": institution,
            "reported_time": time,
            "low_contrast": low_contrast,
        } 
        print(parameters)
        predicted_label = predict_covid(parameters, image)
        return predicted_label

        # res = client.add(image)
        # print(res)
        # return pdf

# if __name__ == "__main__":
#     img_path = r"C:\Users\akshat\Desktop\BIMCV(COVIDQU)\BIMCV(COVID-QU-Ex)\images\sub-S09340_ses-E20837_run-1_bp-chest_vp-ap_cr.png"
#     pdf = predict_covid(parameters, img_path)
#     pdf.output(f"pdf-{img_path[-8:-4]}.pdf")

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='localhost', port = 5050, debug=True )
    #app.run(host='192.168.12.12')

#export FLASK_APP=server.py
from flask import Flask,jsonify,request
app = Flask(__name__)


@app.route("/api/BMI", methods=["POST"])
def BB():
    berat= float(request.form['berat'])
    tinggi= float(request.form['tinggi'])
    BMI = berat/(tinggi/100)
    if BMI < 18.5 :
        return jsonify({"Ideal": "Kurus", "BMI": BMI})
    elif BMI >= 18.5 and BMI <= 25:
        return jsonify({"Ideal": "Normal", "BMI": BMI})
    elif BMI >= 25 and BMI <= 40:
        return jsonify({"Ideal": "Berlebihan", "BMI": BMI})
    else :
        return jsonify({"Ideal": "Bahaya", "BMI": BMI})
    
if __name__ == '__main__':
    app.run(debug = True,port=4000)
    
    
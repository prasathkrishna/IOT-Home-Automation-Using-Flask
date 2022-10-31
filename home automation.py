from flask import Flask
from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

led1 = 2
led2 = 3
led3 = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.output(led1, 0)
GPIO.output(led2, 0)
GPIO.output(led3, 0)
print ("Done")

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/A')
def led1on():
    GPIO.output(led1, 1)
    return render_template('index.html')

@app.route('/a')
def led1off():
    data1="a"
    GPIO.output(led1, 0)
    return render_template('index.html')

@app.route('/B')
def led2on():
    data1="B"
    GPIO.output(led2, 1)
    return render_template('index.html')

@app.route('/b')
def led2off():
    data1="b"
    GPIO.output(led2, 0)
    return render_template('index.html')

@app.route('/C')
def led3on():
    data1="C"
    GPIO.output(led3, 1)
    return render_template('index.html')

@app.route('/c')
def led3off():
    data1="c"
    GPIO.output(led3, 0)
    return render_template('index.html')

if __name__ == "__main__":
    print ("Start")
    app.run(host='192.168.43.2',port=5010)




#uname -m gives machine nname namely x86_64 in my case
# app link! https://flask-app-rpy.oa.r.appspot.com/?temperature=24

from flask import Flask
from flask import request, escape

app = Flask(__name__)

#Project ID on GCloud
#flask-app-rpy



@app.route('/')

def index():
    temperature = str(escape(request.args.get('temperature','')))

    if temperature:
        converted = fahrenheit_to_celsius(temperature)
    else:
        converted = ''

    return f'''<header> Hello!! </header> \n 
    <section>
    <p>Welcome to the temperature fcn converter!</p> \n 
    <p>Provide your input in °F and we'll convert it to °C for you!</p>
    </section>
    <section>
    <form action=\'\' method = \'get\'>
    Input Temperature here in °F: <input type = \'text\', name=\'temperature\'>
    <input type = \'submit\', value = \'Convert your input to °C\'>
    </form>
    </section> 
    <p> {temperature}°F converted to °C is: {converted}°C </p>''' 

#@app.route('/<int:temperature>')

def fahrenheit_to_celsius(temperature):
    ''' This function will convert fahrenheit to celsius '''

    try:
        temperature = temperature.strip()
        celsius = (float(temperature) -32)* ( 5 / 9 ) 
        celsius = round(celsius, 3)  # Round to three decimal places
        return str(celsius)
    except ValueError:
        return "invalid input"

if __name__ == '__main__':
    app.run(host = '127.0.0.1',
    port = 8080,
    debug = True)


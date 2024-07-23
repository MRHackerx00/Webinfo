
from flask import Flask, render_template
from flask import request
import requests

app = Flask(__name__, template_folder='.site', static_url_path='/.site')



@app.route('/')
def index():
 return render_template("index.html")



@app.route('/submit', methods=['POST', 'GET'])
def submit_form():
    oo = request.form['main']
    url ='http://ip-api.com/json/'
    y ='?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,quey'
    main = requests.post(url+oo+y)
    data = main.json()
    st = data['status']
    return render_template('index.html', data=data,  main=st, con=data['country'], res=data['regionName'], city=data['city'], lat=data['lat'], lon=data['lon'],  isp=data['isp'])

#offset
if __name__ == '__main__':
    app.run(debug=True)

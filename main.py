import csv
from flask import Flask
from flask import send_file
from flask import request
import subprocess
import sys
import datetime

# Starts the script

pid = subprocess.Popen([sys.executable, "/home/pi/sensors.py"])

# Flask Server

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <html>
  <head>
    <title>Aedea's Web Server</title>
  </head>
  <body>
    <h1>Current time: {0}</h1>
    <p>Reload this page when you start and copy the time into a document.</p>
    <br><br>
    <a href="/get" download="values.csv">Download CSV</a>
    <br />
    <h4>Directions</h4>
    <p>
      1. Plug in Raspberry Pi, this will start collecting data ASAP<br />2.
      Record time<br />3. Perform experiment<br />4. When done, press "Download
      CSV" and record the time<br />5. Get rid of any data that's outside the
      recorded start and stop times.
    </p>
  </body>
</html>
""".format(datetime.datetime.now())

@app.route('/get')
def return_files():
#     startDate = datetime.datetime.strptime(request.args.get('start'), '%Y-%m-%d %H:%M:%S.%f')
#     endDate = datetime.datetime.strptime(request.args.get('end'), '%Y-%m-%d %H:%M:%S.%f')
#     with open('values.csv', mode='w') as csvFile:
    try:
        return send_file('/home/pi/values.csv', attachment_filename='values.csv')
    except Exception as e:
        return str(e)
    

if __name__ == '__main__':
    app.run(host="0.0.0.0")

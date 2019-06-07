from datetime import datetime
from flask import Flask, request, jsonify
import json
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)



@app.route('/get_time')
def get_time():
    now = datetime.utcnow()
    return jsonify(time=now)

@app.route("/log")
def logTest():
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    app.logger.info('testing info log')
    return "Log testing."

@app.route('/api/event', methods=['POST'])
def event():
	if request.json:
		response = jsonify({'status':'success','data':request.json['event']})

		event = request.json['event']
		data = request.json['data']
		if event == 'participant_connected' and data['has_media']:
			app.logger.info('Participant: {} Connected to conference: {}'.format(data['source_alias'],data['conference']))
		
		if event == 'participant_disconnected':
			app.logger.info('Participant: {} Disconnected from conference: {}'.format(data['source_alias'],data['conference']))

		return response

if __name__ == '__main__':
	logHandler = RotatingFileHandler('events.log', maxBytes=10000, backupCount=1)
	
	# set the log handler level
	logHandler.setLevel(logging.INFO)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	logHandler.setFormatter(formatter)
	# set the app logger level
	app.logger.setLevel(logging.INFO)

	app.logger.addHandler(logHandler)  
	app.run(host="0.0.0.0", debug=True)


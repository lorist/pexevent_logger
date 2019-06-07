# pexevent_logger
Quick and dirty flask app to log connect and disconnect events

`virtualenv -p python3 venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

I use ngrok to quickly setup a publicly accessible URL to send the Pexip Event Sinks

This example only logs participants that connect to a conference with media. It logs the source_alias of the calling participant and the conference to which it connects.






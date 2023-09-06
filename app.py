from flask import Flask, request, render_template
from IDhandling import IDProcesser
from users import User
from ninerEngageInterface import NinerEngageHandler
import requests

NINER_ENGAGE_EVENT_TOKEN = "Token here"

app = Flask(__name__)

s = requests.session()
s.cookies.set(".AspNetCore.Antiforgery.Pnjfq5WAl6o", "COOKIE HERE")
handler = NinerEngageHandler(NINER_ENGAGE_EVENT_TOKEN, s)

@app.route("/")
def index():
    return render_template("station.jinja")


@app.route("/scan", methods = ["GET", "POST"])
def card_scanned():
    try:
        scan_value = request.args.get('scan')
        if(scan_value):
            num = IDProcesser.scan_to_800(scan_value)
            print(f"NUMBER put in {num}")
            u = handler.log_attendance(num)
            print(u)
        return render_template('station.jinja', user=u)
    finally:
        return render_template('station.jinja')
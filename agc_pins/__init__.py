from flask import Flask
app = Flask(__name__)
app.config['tray_b_svg'] = "agc_tray_b_2003100.svg"
app.config['delphi'] = "delphi.db"
app.config['pins_table'] = "PINS_2003100_071"
import agc_pins.views

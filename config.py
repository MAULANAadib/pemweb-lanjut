from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# init app & db connect
app = Flask(__name__)

# Konfigurasi MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pemweblanjut_basicscene:67e874a8660ad00268eccbcad526d1586c3cf748@wxqwb.h.filess.io:3306/pemweblanjut_basicscene'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()

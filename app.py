from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'youremail@gmail.com'
app.config['MAIL_PASSWORD'] = 'yourpassword'
app.config['MAIL_DEFAULT_SENDER'] = 'youremail@gmail.com'

mail = Mail(app)

@app.route("/"):
def index():
    msg = Message("Flask Mail App",recipients=['sunil.mnair@gmail.com'])
    msg.html = '<b>This is Test Email sent from a Flask Web App'

    with app.open_resource("attachment.txt") as file:
            msg.attach("attachment.txt", "text/plain", file.read())
        
    # Common MIME Types
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
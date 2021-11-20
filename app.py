# Run:
#   pip install -r requirements.txt OR pip3 install -r requirements.txt
#   python app.py OR python3 app.py
#   Visit localhost:5000 
#   Success should appear on screen (else an error on console :'))

from flask import Flask
from flask_mail import Mail, Message, Attachment
import recipients
from os.path import exists

app = Flask(__name__)
app.app_context().push()
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = "acesitsadsc@gmail.com"
app.config['MAIL_PASSWORD'] = "aces_itsa.csd"
app.config['MAIL_DEFAULT_SENDER'] = "acesitsadsc@gmail.com" 

mail = Mail()
mail.init_app(app)

def send_mail():
    with mail.connect() as conn:
        for r in recipients.get_data():
            recipient_email = r["Email"] 
            filename = r["filename"]    
            print(f"{recipient_email} : {filename}")   
            message = Message(
                subject="Particiaption certificate",     
                body="Dear Candidate,\n\nWe appreciate your interest in the Mock Placement Drive. Find attached herewith your certificate of participation.\nWe look forward to bring you more such exciting and significant events in the future.\n\nBest wishes,\nCore Team,\nMock Placement Drive"           
            )
            message.add_recipient(recipient_email)
            filename = filename.split(".")[0]
            f = open("certificates/"+filename+".png",'rb')
            message.attach(filename+"_Certificate.png",content_type="image/png",data=f.read())
            f.close()
            path = "reports/"+filename+".pdf"
            if(exists(path)):
                f = open(path,'rb')
                message.attach(filename=filename+"_Report.pdf",content_type="application/pdf",data=f.read())
                f.close()
            conn.send(message)
    return "<h1>Success</h1>"

@app.route('/')
def index():
    return send_mail()

if __name__ == "__main__":
    app.run(port=5000)
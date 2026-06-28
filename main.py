import logging
import os
import threading
from flask import Flask, render_template, request, flash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

logger = logging.getLogger(__name__)

def send_email_async(subject, body, to_email):
    """Send an email via SendGrid API in a background thread."""
    logger.info('Starting async email send...')
    try:
        sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        message = Mail(
            from_email=os.environ.get('SENDGRID_FROM_EMAIL'),
            to_emails=to_email,
            subject=subject,
            plain_text_content=body,
        )
        sg.send(message)
        logger.info('Email sent successfully')
    except Exception as e:
        logger.exception('Failed to send contact form email (async): %s', e)

def is_mail_configured():
    """Return True if required SendGrid env vars are present."""
    return all([
        os.environ.get('SENDGRID_API_KEY'),
        os.environ.get('SENDGRID_FROM_EMAIL'),
    ])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
       
        subject = 'New Contact Form Message'
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Send mail only when properly configured; handle errors gracefully
        if not is_mail_configured():
            app.logger.warning('Mail settings are not configured; skipping send.')
            flash('Mail service is not configured. Your message was not sent. Please contact via email directly.', 'danger')
        else:
            try:
                thread = threading.Thread(
                    target=send_email_async,
                    args=(subject, body, 'bcpythondev@gmail.com'),
                )
                thread.daemon = True
                thread.start()
                logger.info('Spawning email thread...')
                flash('Thank you for your message! We will get back to you soon.', 'success')
            except Exception:
                app.logger.exception('Failed to send contact form email')
                flash('An error occurred while sending your message. Please try again later.', 'danger')
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
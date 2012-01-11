# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def send(subject, recipients, body, sender=None, smtp=None):
    """
    In this implementation, parameter "sender" may not work
    """
    if isinstance(recipients, str):
        recipients = [recipients]
        
    # Import the email modules we'll need
    from email.mime.text import MIMEText

    # msg text
    msg = MIMEText(body)

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients[0]

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    smtp = smtp or defaultsmtp()
    smtp.sendmail(sender, recipients, msg.as_string())
    # smtp.quit()
    
    return


# Import smtplib for the actual sending function
import smtplib
def defaultsmtp():
    return gmailsmtp()


class Account:

    username = None
    password = None
    

gmail_account = Account()
gmail_account.username = "username@gmail.com"
gmail_account.password = "password"
def gmailsmtp():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(gmail_account.username, gmail_account.password)
    return s
    

# End of File

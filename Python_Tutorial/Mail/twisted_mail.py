import sys
from twisted.python import log


def send(message, subject, sender, recipients, host):
    from email.mime.text import MIMEText
    from twisted.mail.smtp import sendmail
    from twisted.internet import reactor
    """
    Send email to one or more addresses.
    """
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    dfr = sendmail(host, sender, recipients, msg.as_string().encode('utf-8'))
    def success(r):
        reactor.stop()
    def error(e):
        print(e)
        reactor.stop()
    dfr.addCallback(success)
    dfr.addErrback(error)

    reactor.run()


if __name__ == '__main__':
    msg = 'This is the message body'
    subject = 'This is the message subjet'

    host = 'smtp3.hpe.com'
    sender = 'liang.yan@hpe.com'
    recipients = ['ke.wang@hpe.com']

    log.startLogging(sys.stdout)
    send(msg, subject, sender, recipients, host)
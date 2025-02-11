import smtplib,ssl


class Email:

    def send(self,message):
        host ="smtp.gmail.com"
        port = 465
        username = "your email"
        password = "your app password"
        msg = f"""Subject: Events

        {message}"""

        receiver = "receiver email"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host,port,context=context) as server:
            server.login(username,password)
            server.sendmail(username,receiver,msg)
            print('email sent')

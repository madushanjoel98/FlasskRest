import smtplib
from propritesReader import loadFilers

password = loadFilers()["mailpassword"]
print(password)
server = smtplib.SMTP('smtp.gmail.com', 465)

server.starttls()

server.login('madushanjoel@gmail.com', password=password)

server.sendmail('madushanjoel@gmail.com', 'madushanjoel@gmail.com', 'TEST EMAIL from Python')

print('Mail sent')

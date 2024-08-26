import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import price_comp as pc

def display(final_str, sdict):
    for iter1 in sdict:
        temp=("\t"+pc.wl[int(iter1[0])]+"\t:\tRs."+str(iter1[1])+"/-")
        final_str+=("\n"+temp)
    return final_str

def generate_mail(ipn,ipm,ipq,sdict):
    strfinal = "\n"
    li = []
    li.append(ipm)
    compStr = display(strfinal, sdict)
    message = "Hello "+ipn+"!\n\nThanks for using our Price Comparator.\nOur team at CT Price Comapare has found the best results for you. We hope this will be helpful.\n\nHappy Shopping :)\n\nYour Query was:   "+ipq+"\nCompare here: "+compStr
    # print(message)
    for i in range(len(li)):send_email("message from price comparator", message, li[i])

def send_email(subject, body, to_email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = os.getenv('APP_SEND_EMAIL')
    password = os.getenv('APP_EMAIL_PWD')

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        # Login
        server.login(from_email, password)
        # Send email
        server.sendmail(from_email, to_email, msg.as_string())
        print("Email sent successfully")
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTPAuthenticationError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server.quit()

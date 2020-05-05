import requests
import time
import smtplib
from bs4 import BeautifulSoup

URL = 'https://www.emag.ro/tastatura-gaming-razer-cynosa-lite-iluminare-rgb-negru-rz03-02740600-r3m1/pd/DCW7PGBBM/' 
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}




def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title =  soup.find(class_="page-title").get_text() 
    price = soup.find(class_="product-new-price").get_text()
    converted_price = int(price[:-7])

    if(converted_price > 150): 
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('youremail@gmail.com', 'yourpassword')

    subject = "Price fell down!"
    body = 'Check the Emag link: https://www.emag.ro/tastatura-gaming-razer-cynosa-lite-iluminare-rgb-negru-rz03-02740600-r3m1/pd/DCW7PGBBM/'
    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'from email number 1',
        'to email number 2',
        msg
    )

    print('Email has been sent!')
    server.quit()

while(True):
    check_price()
    time.sleep(43200) # 12 ore
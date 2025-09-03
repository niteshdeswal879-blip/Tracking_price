import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
load_dotenv(dotenv_path="p1.env")
import os

email=os.getenv("EMAIL")
password=os.getenv("PASSWORD")

url="https://www.amazon.in/Cubelelo-Speedcube-Ultra-Smooth-Leviation-Brain-Teasing/dp/B0DJR1FJ3M/ref=sr_1_2_sspa?crid=2NJE1BMF8PACF&dib=eyJ2IjoiMSJ9.sloypoCKT4-nLgoHs8uFnSQlJbaTghgmFh-x9KPov5Yd-HttFkoteTZsxUQO3FqZV-xWjdrhsFU-3FuMy2nJ9GwRnpmTWGwhhtsNtswcugSY8LI7rDrJbL2k5yqh8hdsh71yluMpRLEZwea-ZlvsqOY4h2-VZYK96Bmu_n0D4WPQjnB8HmPj_ZRtEIie-El-oM1TqbkjKfK9J_nE7vgUIz5_i6Cy2JIaLwZLh9SoBNv7QZqoSwphGl8ZBGu9dIJXRDua4RIi3Tfniz7uUepJXN04CP2fPqpdFDTFo4Q0i3w.y_pMDVJXEIumVneMMxNcRZeukX6Z9nPmQJOryzRY3Ac&dib_tag=se&keywords=magnetic%2B3x3%2Brubik%27s%2Bcube&nsdOptOutParam=true&qid=1753442522&sprefix=magnetic%2B3x%2Caps%2C243&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,hi;q=0.8,da;q=0.7",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding":"gzip, deflate, br, zstd",
    "Priority":"u=0, i",
    "Sec-Ch-Ua-Mobile":"?0",
    "Sec-Ch-Ua-Platform":"Windows",
    "Sec-Fetch-Dest":"document",
    "Sec-Fetch-Mode":"navigate",
    "Sec-Fetch-Site":"cross-site",
    "Sec-Fetch-User":"?1",
    "Upgrade-Insecure-Requests":"1",
}

response=requests.get(url=url,headers=headers)
data=response.text


soup=BeautifulSoup(data,"html.parser")
whole=soup.find(class_="a-price-whole")
price=(whole.getText().split("."))
amount="".join(price[0].split(","))

if int(amount) <1000:
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,to_addrs="niteshdeswal879@gmail.com",msg=f"Subject: Hello, \n \n buy the item quickly the price is {price}")
    connection.close()

else:
    print("don't worry I will get you this")


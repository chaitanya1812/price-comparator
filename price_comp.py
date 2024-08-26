from bs4 import BeautifulSoup
import requests as req
from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import send_email as se

price_dic={}
d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
wl=["flipkart","snapdeal","gadgetsnow","paytmmall","smartprix","croma","pricebaba"]
vl=[]

def getSortedPriceDict():
    return sorted(price_dic.items(), key=lambda x: x[1])

def filterprice(s):
    n = ""
    l = list(s)
    for t in s:
        if t not in d:
            l.remove(t)
    for t in l:
        n = n + t
    return (n)

def getprice(url):
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    #print(soup.title)
    #print(soup.title.text)
    #print(soup.prettify())
    #print(soup.find("div", class="_1vC4OE _3qQ9m1"))
    if wl[0] in url:
        try:
            t = soup.find('div', {'class': '_1vC4OE _3qQ9m1'})
            #print("flipkart price :  Rs.",filterprice(t.text),"/-")
            p = filterprice(t.text)
            price_dic[0]=int(p)
        except AttributeError:print(end=" ")
    elif wl[1] in url:
        try:
            t = soup.find('span', {'class': 'payBlkBig'})
            p = filterprice(t.text)
            #print("snapdeal price : Rs.",p,"/-")
            price_dic[1]=int(p)
        except AttributeError:
            print(end=" ")
    elif wl[2] in url:
        try:
            t = soup.find('div', {'class': '_1vC4OE _3qQ9m1'})
            #print("GadgetsNow price : Rs.",filterprice(t.text),"/-")
            p = filterprice(t.text)
            price_dic[2]=int(p)
        except AttributeError:print(end=" ")
    elif wl[3] in url:
        try:
            t = soup.find('span', {'class': '_1V3w'})
            #print("Paytmmall price : Rs.",filterprice(t.text),"/-")
            p = filterprice(t.text)
            price_dic[3]=int(p)
        except AttributeError:print(end=" ")
    elif wl[4] in url:
        try:
            t = soup.find('span', {'class': 'price'})
            #print("Paytmmall price : Rs.",filterprice(t.text),"/-")
            p = filterprice(t.text)
            price_dic[4]=int(p)
        except AttributeError:print(end=" ")
    elif wl[5] in url:
        try:
            t = soup.find('span', {'class': 'pdpPrice'})
            # print("Paytmmall price : Rs.",filterprice(t.text),"/-")
            p = filterprice(t.text)
            p=list(p)
            p.pop()
            p.pop()
            xy=""
            for xyz in p:
                xy+=xyz
            price_dic[5] = int(xy)
        except AttributeError:
            print(end=" ")
    elif wl[6] in url:
        try:
            t = soup.find('span', {'class': 'txt-xl txt-wt-b txt-clr-light-black lowestPrice'})
            # print("Paytmmall price : Rs.",filterprice(t.text),"/-")
            p = filterprice(t.text)
            price_dic[6] = int(p)
        except AttributeError:
            print(end=" ")
def gsearch(ipq):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    query = "buy "+ipq+" online"
    print(query)
    # query = "buy online google pixel 3A mobile"
    #p="amazon"
    for j in search(query, tld="co.in", num=5, stop=50, pause=2):
        for t in wl:
            if (t not in vl) and (t in j):
                vl.append(t)
                getprice(j)
def input():
    root = Tk()
    root.geometry('500x500')
    root.title("compare")

    Fullname = StringVar()
    Query = StringVar()
    Email = StringVar()

    label_0 = Label(root, text="Price Comparator", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)

    label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)

    entry_1 = Entry(root, textvar=Fullname)
    entry_1.place(x=240, y=130)

    label_2 = Label(root, text="Query", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)

    entry_2 = Entry(root, textvar=Query)
    entry_2.place(x=240, y=180)

    label_3 = Label(root, text="Email", width=20, font=("bold", 10))
    label_3.place(x=70, y=230)

    entry_3 = Entry(root, textvar=Email)
    entry_3.place(x=240, y=230)

    def callback():
        ipname = Fullname.get()
        ipquery = Query.get()
        ipmail = Email.get()
        # print(ipname, ipquery, ipmail)
        gsearch(ipquery)
        se.generate_mail(ipname,ipmail,ipquery, getSortedPriceDict())

    Button(root, text='Mail Me!', width=20, bg='brown', fg='white', command=callback).place(x=180, y=380)

    root.mainloop()

if __name__ == "__main__":input()
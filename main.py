import os
import sys
from urllib2 import urlopen
import urllib2
import csv
import time
from bs4 import BeautifulSoup
import os


quote_page = ['https://www.bloomberg.com/quote/USDCAD:CUR','https://www.bloomberg.com/quote/EURUSD:CUR','https://www.bloomberg.com/quote/GBPUSD:CUR','https://www.bloomberg.com/quote/EURCHF:CUR','https://www.bloomberg.com/quote/USDHKD:CUR']
def get_currency(link_w) :
    data = []
    flag_l = 0
    for pg in link_w :
        page=urllib2.urlopen(pg)
        soup=BeautifulSoup(page,'html.parser')
        name_box=soup.find('div',attrs={'class': 'ticker'})
        if not name_box == None :
            name=name_box.text.strip()
        else :
            flag_l =1
        price_box=soup.find('div',attrs={'class': 'price'})
        if not name_box == None :
            price=price_box.text.strip()
        else :
            flag_l =1
        data.append((name,price))

    with open('index.csv','a') as csv_file:
        writer=csv.writer(csv_file)
        tm=time.strftime("%Y-%m-%d %H:%M")
        for name,price in data:
            writer.writerow([name,price,tm])
            print name,price,tm


def get_link(addres_l):
    page=urllib2.urlopen(addres_l)
    soup=BeautifulSoup(page,'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
def clean():
    os.system('clear')
def display_title():
    clean()

    print("\t**********************************************")
    print("\t****************** Hello! ********************")
    print("\t**********************************************")

def get_images(addres_l):
    page=urllib2.urlopen(addres_l)
    soup=BeautifulSoup(page,'html.parser')
    ans=raw_input("\nDo you want to download them? (Y\N)\n")
    if (ans =='Y') or (ans == 'y') :
        for link in soup.find_all('img'):
            link_src=link.get('src')
            link_src_n = link_src.split("://")
            if link_src_n[0] != 'http' or link_src_n[0] != 'https'  :
                link_src = addres_l + link_src
            print(link_src)
            os.system("wget " + link_src)
    elif (ans =='N') or (ans == 'n') :
        for link in soup.find_all('img'):
            print(link.get('src'))
    else :
        print("\nI didn't understand that choice.\n")


def get_user_choice() :
    print("\n[1] Get the all currency that I listed")
    print("\n[2] Get the all link on the site that you give")
    print("\n[3] Get the all images on the site that you give")
    print("\n[q] Quit.. ")

    return raw_input("\nWhat would you like to do?\n")



if __name__ == "__main__" :
    choice=''
    display_title()


    while choice !='q' :
        choice = get_user_choice()

        clean()

        if choice == '1':
            print("\nHere are the currency list I know.\n")

            get_currency(quote_page)
        elif choice == '2':
            get_link(raw_input("Please link : "))
        elif choice =='3' :
            get_images(raw_input("Please link : "))
        elif choice == 'q':
            print("\nThanks for playing. Bye.")
        else:
            print("\nI didn't understand that choice.\n")
else:
    print "Something went wrong"

from bs4 import BeautifulSoup
from urllib.request import *
import re
from functools import reduce
import vk
import time

def read_userfile(userfile_name: str):
    """Function for getting info about user settings to search
    1st line: first part of link to saved search page (should finish w/ "...p=")
    2nd line: second part of link
    3rd+ lines: user domains vk (send messages whom)
    """
    with open(userfile_name, 'r') as file:
        global cian_link1, cian_link2, users
        cian_link1 = file.readline()
        cian_link2 = file.readline()
        users = file.readlines()
        for i in range(0,users.__len__()):
            users[i] = users[i].rstrip("\n")
        cian_link1 = cian_link1.rstrip("\n")
        cian_link2 = cian_link2.rstrip("\n")

def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html

def write_flats(filename):
    with open(filename, 'w') as file:
        file.writelines(str(num_offers)+"\n")
        file.writelines([offer+"\n" for offer in offers])

def read_flats(filename):
    with open(filename, 'r') as file:
        global offers_old
        offers_old = file.readlines()
        for i in range(0,offers_old.__len__()):
            offers_old[i] = offers_old[i].rstrip("\n") 

def send_vk(link):
    session = vk.Session(access_token='TOKEN_FROM_VK_COM_KKFKFKFKFKFKKFKFKFK')
    api = vk.API(session)
    global users
    for user in users:
        api.messages.send(domain=user, message = "NEW FLAT", v = 5.80)
        api.messages.send(domain=user, message = link, v = 5.80)
    #sleep because we can't send 20+ msgs per sec
    time.sleep(60//users.__len__()+1)

def print_time():
    print("Updated on:")
    print(time.ctime())
    print("_____________")

def main():
    read_userfile("cian_info.txt")
        
    opener = build_opener()
    opener.addheaders = [("User-Agent", "Mozilla/6.0")]
    install_opener(opener)
    
    data_file = "cian_flats.txt"


    try:
        while True:
            global num_offers, offers, offers_old
            num_offers = 25
            offers = list()
            offers_old = list() 

            read_flats(data_file)
            n = num_offers//25+((num_offers%25 == 0 and 0) or 1)
            for i in range(0,n):#TOD0
                html = get_html(cian_link1+str(i+1)+cian_link2)
                soup = BeautifulSoup(html, "html.parser")
                tag = soup.find(attrs={"class" : re.compile('totalOffers')})
                #total number of flats
                num_offers = int(tag.text.split()[0])
                if i != n-1:
                    tagset = soup.findAll(attrs={"href" : re.compile('rent/flat/\d')}, limit=25)
                else:
                    tagset = soup.findAll(attrs={"href" : re.compile('rent/flat/\d')}, limit=num_offers%25)
                #func for merging list of lists
                listmerge=lambda s: reduce(lambda d,el: d.extend(el) or d, s, [])
                #list of links
                offers = listmerge([offers, [tag.attrs["href"] for tag in tagset]])
            if (list(set(offers)-set(offers_old)).__len__() != 0):
                for offer in list(set(offers)-set(offers_old)):
                    send_vk(offer)
                write_flats(data_file)
            print_time()
            time.sleep(300)
    except KeyboardInterrupt:
        pass

if __name__=="__main__":
    main()
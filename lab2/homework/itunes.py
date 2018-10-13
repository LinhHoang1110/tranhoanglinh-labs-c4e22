from urllib.request import urlopen 
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/" #doawload webpage

conn = urlopen(url) #open connection

raw_data = conn.read()#read raw data

webpage_text = raw_data.decode("utf-8")#decode data
#find ROI
soup = BeautifulSoup(webpage_text, "html.parser") #connect to soup

section = soup.find("section","section chart-grid")

li_list = section.find_all("li")

new_list =[]
for li in li_list:
    a1 = li.h3.a
    a2 = li.h4.a
    namesong = a1.string
    artist = a2.string
    song ={
        "Namesong": namesong,
        "artist": artist
    }
    new_list.append(song)


pyexcel.save_as(records=new_list, dest_file_name="itunes.xlsx")#convert to excel file




from youtube_dl import YoutubeDL
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

new_list1 = []
for i in range(len(new_list)):
    a = new_list[i]["Namesong"] + " " + new_list[i]["artist"]
    new_list1.append(a)

for i in range(len(new_list1)):
    options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
    }
    dl = YoutubeDL(options)
    dl.download([new_list1[i]])
    
    
    
  
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)

raw_data = conn.read()

webpage_text =raw_data.decode("utf-8")

soup = BeautifulSoup(webpage_text, "html.parser")

table = soup.find("table", id="tableContent")

tr1_list = table.find_all("tr")
new_list = []

for i in range(len(tr1_list)):
    
    td_list = tr1_list[i].find_all("td")
    for j in td_list:
        data ={
        "Name": td_list[0].string,
        "quy4": td_list[1].string,
        "quy1": td_list[2].string,
        "quy2": td_list[3].string,
        "quy3": td_list[4].string
        }
    new_list.append(data)   

pyexcel.save_as(records = new_list, dest_file_name = "table.xlsx")
    














    





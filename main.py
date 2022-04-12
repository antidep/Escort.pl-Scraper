import requests
from bs4 import BeautifulSoup
import re

from collections import OrderedDict

import warnings
warnings.filterwarnings("ignore")

import json

s = requests.Session()
s.headers = OrderedDict((
      ("Host","en.escort.pl"),
      ("User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"),
      #("Accept","application/json, text/javascript, */*; q=0.01"),
      ("Accept-Language","en-US,en;q=0.5"),
      ("Accept-Encoding","gzip, deflate, br"),
      #("Content-Type","application/x-www-form-urlencoded; charset=UTF-8"),
      #("X-Requested-With","XMLHttpRequest"),
      #("Content-Length","8"),
      ("Origin","https://en.escort.pl"),
      ("Connection","keep-alive"),
      #("Cookie","escortsession=d00p2mlc9i5q47eei2rc966chn; warning=1"),
      ("Sec-Fetch-Dest","empty"),
      ("Sec-Fetch-Mode","cors"),
      ("Sec-Fetch-Site","same-origin"),
      ("Pragma","no-cache"),
      ("Cache-Control","no-cache"),
      ("TE","trailers"),
    ))

proxies = {"http":"http://seak20667nyaz48722:NhIgDw8yhRLTUaur_country-Canada@isp2.hydraproxy.com:9989"}

for i in range(1,157):
  url = "https://178.162.139.45/szukaj/page"+str(i)+".html?province=&city=&district=&filter_price_type=&filter_price=0%3B10000&filter_breasts=0%3B8&filter_age=18%3B100&filter_weight=30%3B200&filter_height=100%3B220&q="
  r = s.get(url, allow_redirects=False, verify=False, proxies=proxies)
  soup = BeautifulSoup(r.text, "html.parser")
  
  links = soup.find_all("a",attrs={"href":re.compile("/anons/[0-9]{1,10}\.html$")})
  for link in links:
    f = open("whores.txt","a+")
    try:
      whore_page_url_real = link.get("href")
      
      whore_page_url = re.sub("[a-z]{1,3}\.escort\.pl","178.162.139.45",whore_page_url_real)
      whore_page_url = whore_page_url.replace("https://","http://")
      
      whore_id = whore_page_url.split("/")
      whore_id = whore_id[len(whore_id)-1].split(".")[0]
      print("ID: "+whore_id)
      
      print(whore_page_url_real)
      r2 = s.get(whore_page_url)
      whore_soup = BeautifulSoup(r2.text, "html.parser")

      new_headers = OrderedDict((
        ("Host","en.escort.pl"),
        ("User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"),
        ("Accept","application/json, text/javascript, */*; q=0.01"),
        ("Accept-Language","en-US,en;q=0.5"),
        ("Accept-Encoding","gzip, deflate, br"),
        ("Referer",whore_page_url_real),
        ("Content-Type","application/x-www-form-urlencoded; charset=UTF-8"),
        ("X-Requested-With","XMLHttpRequest"),
        ("Content-Length","8"),
        ("Origin","https://en.escort.pl"),
        ("Connection","keep-alive"),
        #("Cookie","escortsession=d00p2mlc9i5q47eei2rc966chn; warning=1"),
        #("Cookie",s.headers["Cookie"]),
        ("Sec-Fetch-Dest","empty"),
        ("Sec-Fetch-Mode","cors"),
        ("Sec-Fetch-Site","same-origin"),
        ("Pragma","no-cache"),
        ("Cache-Control","no-cache"),
        ("TE","trailers"),
      ))
      
      try:
        phone_r = s.post("https://178.162.139.45/includes/ajax.show-phone.php",data={"id":whore_id}, allow_redirects=False, verify=False, headers=new_headers)
        phone_number = json.loads(phone_r.text)["phone"]
        print("Phone Number: "+str(phone_number))
        f.write("\n"+str(phone_number))
      except:
        print(phone_r.text)
        print("UH OH couldnt get the phone number")
    except:
      pass
    f.close()

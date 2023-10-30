import requests
import pygsheets
import pandas as pd
from urllib.request import urlopen
import json

import urllib3

m1 = "headline='Google Cloud Computing Foundations: Cloud Computing Fundamentals'"
m2 = "headline='Google Cloud Computing Foundations: Infrastructure in Google Cloud'"
m3 = "headline='Google Cloud Computing Foundations: Networking &amp;amp; Security in Google Cloud'"
m4 = "headline='Google Cloud Computing Foundations: Data, ML, and AI in Google Cloud'"
m5 = "headline='Create and Manage Cloud Resources'"
m6 = "headline='Perform Foundational Infrastructure Tasks in Google Cloud'"
m7 = "headline='Build and Secure Networks in Google Cloud'"
m8 = "headline='Perform Foundational Data, ML, and AI Tasks in Google Cloud'"
l3 = "headline='Level 3 GenAI: Prompt Engineering'"

url = "https://storage.googleapis.com/jsonbkt/service.json"


r = requests.get(url)
print(r.json())
f = open("servicee.json", "a")
f.write(str(r.text))
f.close()

gc = pygsheets.authorize(service_file="servicee.json")


#Create a service account key and downlaod the key json(make sure google sheets api is enabled)
#Replace with your old progress report sheet.
sh = gc.open('MLR Institute of Technology - Hyderabad [29 Oct]')
wks = sh.worksheet_by_title("MLR Institute of Technology - Hyderabad [29 Oct]")


Course = []
Skill = [] 
Gen = []
Total = []

#replace with the index of your last
last = 200

for i in range(2, last):
    purl=wks.cell('F'+str(i)).value
    print(purl)

    data = requests.get(url=purl).text
    total = 0
    mod = ""
    c = 0
    s = 0
    g = 0
    if m1 in data:
        total+=1
        mod+="1,"
        c+=1
    if m2 in data:
        total+=1
        mod+="2,"
        c+=1
    if m3 in data:
        total+=1
        mod+="3,"
        c+=1
    if m4 in data:
        total+=1
        mod+="4,"
        c+=1
    if m5 in data:
        total+=1
        mod+="5,"
        s+=1
    if m6 in data:
        total+=1
        mod+="6,"
        s+=1
    if m7 in data:
        total+=1
        mod+="7,"
        s+=1
    if m8 in data:
        total+=1
        mod+="8,"
        s+=1
    if l3 in data:
        total+=1
        mod+="ai"
        g+=1
    if mod == "":
        mod = "NA"
    print(mod)
    print(total)
    Course.append(c)
    Skill.append(s)
    Gen.append(g)
    if total == 9:
        Total.append("Yes")
    else : Total.append("No")

df = pd.DataFrame()
df['# of Courses Completed'] = Course
df['# of Skill Badges Completed'] = Skill
df['# of GenAI Game Completed'] = Gen
df['Total Completions of both Pathways'] = Total


print(df)
wks.set_dataframe(df,(1,7))


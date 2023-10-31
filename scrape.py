import requests
import pygsheets
import pandas as pd


m1 = "headline='Google Cloud Computing Foundations: Cloud Computing Fundamentals'"
m2 = "headline='Google Cloud Computing Foundations: Infrastructure in Google Cloud'"
m3 = "headline='Google Cloud Computing Foundations: Networking &amp;amp; Security in Google Cloud'"
m4 = "headline='Google Cloud Computing Foundations: Data, ML, and AI in Google Cloud'"
m5 = "headline='Create and Manage Cloud Resources'"
m6 = "headline='Perform Foundational Infrastructure Tasks in Google Cloud'"
m7 = "headline='Build and Secure Networks in Google Cloud'"
m8 = "headline='Perform Foundational Data, ML, and AI Tasks in Google Cloud'"
l3 = "headline='Level 3 GenAI: Prompt Engineering'"

gc = pygsheets.authorize(service_file='scrape1.json')

sh = gc.open('CJ-Assign')
wks = sh.worksheet_by_title("Main")
Badges = []
Status = []


for i in range(2, 153):
    purl=wks.cell('D'+str(i)).value
    print(purl)

    data = requests.get(url=purl).text
    total = 0
    mod = ""
    if m1 in data:
        total+=1
        mod+="1,"
    if m2 in data:
        total+=1
        mod+="2,"
    if m3 in data:
        total+=1
        mod+="3,"
    if m4 in data:
        total+=1
        mod+="4,"
    if m5 in data:
        total+=1
        mod+="5,"
    if m6 in data:
        total+=1
        mod+="6,"
    if m7 in data:
        total+=1
        mod+="7,"
    if m8 in data:
        total+=1
        mod+="8,"
    if l3 in data:
        total+=1
        mod+="ai"
    if mod == "":
        mod = "NA"
    print(mod)
    print(total)
    Badges.append(mod)
    if total == 9:
        Status.append("Completed")
    else : Status.append("Not Completed")

df = pd.DataFrame()
df['Modules'] = Badges
df['Status'] = Status
print(df)
wks.set_dataframe(df,(1,9))


import requests

m1 = "headline='Google Cloud Computing Foundations: Cloud Computing Fundamentals'"
m2 = "headline='Google Cloud Computing Foundations: Infrastructure in Google Cloud'"
m3 = "headline='Google Cloud Computing Foundations: Networking &amp;amp; Security in Google Cloud'"
m4 = "headline='Google Cloud Computing Foundations: Data, ML, and AI in Google Cloud'"
m5 = "headline='Create and Manage Cloud Resources'"
m6 = "headline='Perform Foundational Infrastructure Tasks in Google Cloud'"
m7 = "headline='Build and Secure Networks in Google Cloud'"
m8 = "headline='Perform Foundational Data, ML, and AI Tasks in Google Cloud'"
l3 = "headline='Level 3 GenAI: Prompt Engineering'"


def count(purl):
    data = requests.get(url=purl).text
    print(data)
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
    print(mod)
    if total == 9:
        return "Completed"
    else : return "Not Completed"

count("https://www.cloudskillsboost.google/public_profiles/0a9db359-c578-4ea4-b064-115573cc5c4b")
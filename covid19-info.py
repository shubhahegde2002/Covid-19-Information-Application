import json
import requests
print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                  WELCOME TO COVID-19 INFORMATION APPLICATION")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
print()

def continent():
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/asia"

    headers = {
    'x-rapidapi-key': "533c58ba9bmsh9ad85665de7f9e9p1e826cjsnc78c8791fc95",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    print("Enter Country in Asia: ")
    inp1=input().capitalize()
    inp2=inp1.upper()
    z=response.json()
    for x in z:
        if(x['Country'].upper()==inp2):
            print("Total Cases in " +inp1+ " : " ,x['TotalCases'])
            print("Total Deaths in " + inp1 + " : " , x['TotalDeaths'])
            print("Total Recovered in " + inp1 + " : " , x['TotalRecovered'])
            print("Serious/Critical Cases in " + inp1 + " : " , x['Serious_Critical'])
            print("Total Tests in " + inp1 + " : " , x['TotalTests'])


def country():
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/api-covid-data/reports/IND"

    headers = {
        'x-rapidapi-key': "533c58ba9bmsh9ad85665de7f9e9p1e826cjsnc78c8791fc95",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    m = response.json()
    print("Enter State in India :")
    i1 = input().capitalize()
    i2 = i1.upper()
    for x in m:
        if (x['province'].upper() == i2):
            print("Confirmed Cases In " + i1 + " is ", x['confirmed'])
            print("Recovered Cases In " + i1 + " is ", x['recovered'])
            print("Deaths In " + i1 + " is ", x['deaths'])



def news():
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/news/get-vaccine-news/0"

    headers = {
        'x-rapidapi-key': "533c58ba9bmsh9ad85665de7f9e9p1e826cjsnc78c8791fc95",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    f = response.json()['news']
    count = 1
    for i in f:
        print(count, ". " + i['title'])
        count += 1


print("CHOOSE YOUR OPTIONS : ")
print("1. Covid-19 Cases Around Asia")
print("2. Covid-19 Cases In India")
print("3. Covid-19 Trending News")
choice=int(input())
if choice==1:
    continent()
elif choice==2:
    country()
elif choice==3:
    news()
else:
    print("INVALID! ")



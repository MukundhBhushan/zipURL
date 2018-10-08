import requests
import json

#database used restdb.io https://restdb.io/

#getting the long url from the shortten url
def get(querry):
    url='<name of the url generated>?q={\"short_url\":"<hostinig site url>/%s"}'%(querry)
    headers = {
        'content-type': "application/json",
        'x-apikey': "<generated key>",
        'cache-control': "no-cache"
        }
    print(url)

    response = requests.request("GET", url,headers=headers)

    data=response.text
    print(data)
    dataJL = json.loads(data)[0]
    return(dataJL['long_url'])

#inserting the long and short urls to the database
def post(large,short):
    url = "<data base url>"

    payload = json.dumps({"long_url": large, "short_url": short})
    headers = {
        'content-type': "application/json",
        'x-apikey': "<generated key>",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)  #printing the db to the console return not needed


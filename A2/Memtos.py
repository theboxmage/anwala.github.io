#Use in a seperate folder, this generates a lot of files.
import urllib.request, json
import requests
Count={}
c=0
Count[0] = 0
with open("links.txt", "r") as ins:
    for line in ins:
        URIT= 'http://memgator.cs.odu.edu/timemap/json/'
        print(c)
        c = c + 1
        print(URIT + line)
        r = requests.get(URIT + line)
        if r.status_code == 404:
            Count[0] = Count[0] + 1
            print(Count[0])
        else:
            response = r.text
            json_response = json.loads(response)
            if json_response.get('mementos') is not None:
                num=len(json_response['mementos']['list'])
                if Count.get(num) is not None:
                        print(num)
                        Count[num] = Count[num] + 1
                else:
                        Count[num] = 1
            stri='data' + str(c) + '.json'
            with open(stri, "w+") as outfile:
                json.dump(json_response, outfile)

for key, value in Count.items():
    print(key)
    print(value)
    print("\n")
        #response = r.text
        #json_response = json.loads(response)
        #if json_response.get('mementos') is not None:
        #    print(len(json_response["mementos"]["list"]))
#     for line in ins:
#         with urllib.request.urlopen(line) as url:
#             data = json.loads(url.read().decode())
#             print(len(data["mementos"]["list"]))

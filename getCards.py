import requests, json

url = "https://omgvamp-hearthstone-v1.p.rapidapi.com/cards/sets/Battlegrounds"

headers = {
    'x-rapidapi-host': "omgvamp-hearthstone-v1.p.rapidapi.com",
    'x-rapidapi-key': "ac56c66660msh5b3a85cf7fc0eb2p162381jsn3c49219793ce"}

r = requests.request("GET", url, headers=headers)

a = json.loads(r.text)

collumns = ['name','cardId','dbfId','cost','attack','health','race','img','text','mechanics']

for c in collumns:
    print(c, end=",")
print()

for i in a:
    try:
        if i["type"] != 'Minion':
            continue
    except KeyError:
        continue
    for c in collumns:
        try:
            if c == 'mechanics':
                try:
                    print(len(i[c]),end=',{')
                except KeyError:
                    print(end='0,{}');
                for m in i[c]:
                    print(m['name'],end=',')
                print(end='}')
                continue
            print(i[c], end=",")
        except KeyError:
            print(end=",")
    print()

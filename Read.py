import json

def ReadJson():
    y=open('test2.json')
    data=json.loads(y.read())
    print(data)
    print(type(data))
    return data

if __name__ == '__main__':
    ReadJson()
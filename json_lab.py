import json

# loads a json into list or dict
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''

info = json.loads(data)
print(type(info))
print(info[1]['name'])
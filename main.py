import json

# read file
with open('sample_request.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

print("name: " + str(obj['username']))

id = 1
data = json.loads(open('sample_template.json').read())



data = {}
data['id'] = id
id+=1
data['tasks'] = str(obj['title'])
data['notes'] = str(obj['notes'])
data['owner'] = []
data['owner'].append({
     'username': str(obj['username']),
     'fullname': str(obj['name']['first']+" "+obj['name']['last'])
 })
data['completed'] = bool(obj['completed'])

with open('response.json', 'w') as outfile:
        json.dump(data,outfile, indent='\t')

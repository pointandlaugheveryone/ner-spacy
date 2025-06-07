import json


with open('azurelabels.json', 'r') as file:
    text = json.loads(file.read())
    # print(text)
    documents = text['documents']

    for doc in documents:
        i = 1
        path = f'/home/ronji/repos/CVdata/DATA/{doc['contents']}' # renamed 'location' to contents previously
        with open(path, 'r') as f:
            contents = f.read()
            doc['contents'] = contents
            doc['ID'] = i
        i += 1

with open('labels.json', 'w') as labels:
    labels.write(json.dumps(text, indent = 4, sort_keys=True))


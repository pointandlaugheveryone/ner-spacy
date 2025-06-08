import json


with open('/home/ronji/repos/CVdata/data_azure/azurelabels.json', 'r') as file:
    text = json.loads(file.read())
    # print(text)
    documents = text['documents']

    i = 1
    for doc in documents:
        path = f'/home/ronji/repos/CVdata/data_azure/{doc['contents']}' # renamed 'location' to contents previously
        with open(path, 'r') as f:
            contents = f.read().replace("\n", " ").replace("\t", " ").replace("\r", " ")
            if len(contents) < 50:
                continue
            else:
                doc['contents'] = contents
                doc['ID'] = i
        i += 1

with open('labels.json', 'w') as labels:
    labels.write(json.dumps(text, indent = 4, sort_keys=True))


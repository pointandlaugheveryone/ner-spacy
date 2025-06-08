import json
from classes import Document, Annotation


data = {}
documents = []

with open('labels.json', 'r') as f:
    labels_old = json.loads(f.read())
    docs = labels_old['documents']

    for doc in docs:
        content = doc['contents']
        annotations = []

        i = 1
        for ent in doc['entities'][0]['labels']: 
            start = ent['offset']
            end = ent['length'] + start
            tag_name = ent['category']
            value = content[start:end]

            annotations.append(Annotation(start, end, tag_name, value))
            i+=1

        documents.append(Document(content,annotations))
data['documents'] = [doc.to_dict() for doc in documents]

with open('labels_new.json', 'w') as labels:
    labels.write(json.dumps(data, indent=4, sort_keys=True))
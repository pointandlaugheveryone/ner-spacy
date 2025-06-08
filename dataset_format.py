import json
from data_model import Document, Annotation


documents = []

with open('labels.json', 'r') as f:
    labels_old = json.loads(f.read())
    docs = labels_old['documents']

    for doc in docs:
        id = doc['ID']
        content = doc['contents']
        annotations = []

        i = 1
        for ent in doc['entities'][0]['labels']: 
            ent_id = i
            start = ent['offset']
            end = ent['length'] + start
            tag_name = ent['category']
            value = content[start:end]

            annotations.append(Annotation(ent_id, start, end, tag_name, value))
            i+=1

        documents.append(Document(id,content,annotations))

with open('labels.json', 'w') as labels:
    labels.write(json.dumps([doc.to_dict() for doc in documents], indent=4, sort_keys=True))
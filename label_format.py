import json
from classes import Document, Annotation


def read_exported_labels():
    data = {}
    documents = []

    with open('labels2.json', 'r') as file:
        text = json.loads(file.read())
        documents_read = text['assets']['documents']

        i = 1
        for doc in documents_read:
            path = f'/home/ronji/repos/CVdata/data_src/{doc['contents']}' # renamed 'location' to contents previously
            try:
                with open(path, 'r') as f:
                    id = i
                    contents = f.read().replace("\n", " ").replace("\t", " ").replace("\r", " ")
                    annotations = []

                    j = 1
                    for ent in doc['entities'][0]['labels']:
                        id = j
                        start = ent['offset']
                        end = ent['length'] + start
                        label = ent['category']
                        annotation = Annotation(id,start,end,label).to_dict()
                        annotations.append(annotation)
                        j+=1
                        print(f'{start},{end},{label}')
                    i += 1
                document = Document(id,contents,annotations).to_dict(annotations)
                documents.append(document)
            except FileNotFoundError or ValueError as e:
                print(f"file deleted previously; {e.filename}")

    data['documents'] = documents
    with open('labels_new.json', 'w') as labels:
        labels.write(json.dumps(data, indent = 4, sort_keys=True))


read_exported_labels()

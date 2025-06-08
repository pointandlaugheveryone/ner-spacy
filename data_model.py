from typing import List, Any


class Annotation:
    id: int
    start: int
    end: int
    tag_name: str
    value: str

    def __init__(self, id: int, start: int, end: int, tag_name: str, value: str) -> None:
        self.id = id 
        self.start = start
        self.end = end
        self.tag_name = tag_name
        self.value = value

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "start": self.start,
            "end": self.end,
            "tag_name": self.tag_name,
            "value": self.value,
        }



class Document:
    id: int
    content: str
    annotations: List[Annotation]

    def __init__(self, id: int, content: str, annotations: List[Annotation]) -> None:
        self.id = id
        self.content = content
        self.annotations = annotations

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "content": self.content,
            "annotations": [annotation.to_dict() for annotation in self.annotations],
        }



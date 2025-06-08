from typing import List, Any


class Annotation:
    id: int
    start: int
    end: int
    tag_name: str
    value: str

    def __init__(self, start: int, end: int, tag_name: str, value: str) -> None:
        self.start = start
        self.end = end
        self.tag_name = tag_name
        self.value = value

    def to_dict(self) -> dict:
        return {
            "start": self.start,
            "end": self.end,
            "tag_name": self.tag_name,
            "value": self.value,
        }



class Document:
    id: int
    content: str
    annotations: List[Annotation]

    def __init__(self, content: str, annotations: List[Annotation]) -> None:
        self.content = content
        self.annotations = annotations

    def to_dict(self) -> dict:
        return {
            "content": self.content,
            "annotations": [annotation.to_dict() for annotation in self.annotations],
        }



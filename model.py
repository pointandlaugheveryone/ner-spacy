from uuid import UUID
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



class Example:
    id: UUID
    content: str
    annotations: List[Annotation]
    classifications: List[Any]

    def __init__(self, id: UUID, content: str, annotations: List[Annotation]) -> None:
        self.id = id
        self.content = content
        self.annotations = annotations




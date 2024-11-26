import uuid

class Grade:
    def __init__(self, name=None, subject=None, score=None, id=None):
        self.name = name
        self.subject = subject
        self.score = score
        self.id = id if id else str(uuid.uuid4())



class Document:

    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ""

    def insert(self, character):
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        with open(self.filename, "w") as f:
            f.write("".join(self.characters))

    @property
    def string(self):
        return "".join(self.characters)


class Cursor:

    def __init__(self, document):
        self.document = document
        self.position = 0
    
    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        while self.document.characters[self.position - 1] != "\n":
            self.position -=1
            if self.position == 0:
                break
    
    def end(self):
        while(
            self.position < len(self.document.characters)
            and self.document.characters[self.position] != "\n"
        ):
            self.position += 1




if __name__ == "__main__":
    
    doc = Document()
    doc.filename = "test_document"
    doc.insert("h")
    doc.insert("e")
    doc.insert("l")
    doc.insert("l")
    doc.insert("o")
    doc.insert("\n")
    doc.insert("w")
    doc.insert("o")
    doc.insert("r")
    doc.insert("l")
    doc.insert("d")
    doc.cursor.home()
    doc.insert("*")
    print(doc.string)

    








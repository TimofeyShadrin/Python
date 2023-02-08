from datetime import date


class Note:

    id = 0

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.create_date = date.today()
        self.id += 1

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_text(self):
        return self.text

    def get_create_date(self):
        return self.create_date



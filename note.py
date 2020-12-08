class Note:
    def __init__(self, name, note):
        if name is None or name == "" or type(name) != str or type(note) != float:
            raise TypeError

        if note < 2 or note > 6:
            raise ValueError

        self.name = name
        self.note = note

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note


class NotesStorage:
    def __init__(self):
        self.notes = []

    def get_all_notes_of(self, name):
        pass

    def clear(self):
        pass

    def add(self, note):
        pass


class NotesService:
    def __init__(self):
        self.storage = NotesStorage()

    def add(self, note):
        self.storage.add(note)

    def average_of(self, name):
        notes = self.storage.get_all_notes_of(name)
        if len(notes) != 0:
            res = 0
            for note in notes:
                res += note.note
            return res / len(notes)
        else:
            raise Exception

    def clear(self):
        self.storage.clear()

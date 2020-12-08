import unittest
from note import Note


class TestNote(unittest.TestCase):
    def test_note_setting(self):
        Note('test', 2.23)

    def test_note_error(self):
        name = 'test'
        note = 8
        self.assertRaises(TypeError, Note, name, note)

    def test_note_error2(self):
        name = ''
        note = 0.2
        self.assertRaises(TypeError, Note, name, note)

    def test_note_get_note(self):
        name = '123'
        note = 3.5
        test_object = Note(name, note)
        self.assertEqual(test_object.get_note(), note)
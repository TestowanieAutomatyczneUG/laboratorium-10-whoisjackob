import unittest
from note import Note, NotesService, NotesStorage
from unittest.mock import *


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


class TestNotesService(unittest.TestCase):
    def setUp(self):
        self.temp = NotesService()

    @patch.object(NotesStorage, "get_all_notes_of")
    def test_add_note(self, mock_method):
        name = "Kuba"
        note = 4.23
        mock_method.return_value = [Note("Kuba", 4.23)]
        self.temp.add(Note(name, note))
        self.assertEqual(self.temp.average_of(name), 4.23)

    @patch.object(NotesStorage, "clear")
    def test_note_clear(self, mock_method):
        mock_method.return_value = None
        temp = NotesService()
        self.assertEqual(temp.clear(), None)

    # @patch.object(NotesStorage, "get_all_notes_of")
    # def test_average_name_does_not_exist(self, mock_method):
    #     self.temp.add(Note("Kuba", 5.0))
    #     mock_method.return_value = []
    #     self.assertEqual(self.temp.average_of("Wiktor"), "Name does not exist")

    # @patch.object(NotesStorage, "get_all_notes_of")
    # def test_average_name(self, mock_method):
    #     mock_method.return_value = [Note("test1", 5)]
    #     self.assertRaises(self.temp.average_of("test2"), ValueError)

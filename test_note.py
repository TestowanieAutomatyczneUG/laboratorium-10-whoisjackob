import unittest
from note import Note


class TestNote(unittest.TestCase):
    def test_note_setting(self):
        Note('test', 2.23)



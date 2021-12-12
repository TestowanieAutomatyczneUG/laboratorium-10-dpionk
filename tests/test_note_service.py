import unittest
from unittest.mock import *
from functions.Note import Note
from functions.NotesStorage import NotesStorage
from functions.NotesService import NotesService


class Test_note_service(unittest.TestCase):
    @patch.object(NotesStorage, 'add')
    def test_note_service_add(self, mock_method):
        notesService = NotesService()
        notatka = Note('notatka', 4.56)
        mock_method.return_value = True
        self.assertEqual(notesService.add(notatka), True)
        
    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_notes(self, mock_method):
        notesService = NotesService()
        mock_method.return_value = [Note('notatka', 5.0), Note('notatka', 4.5), Note('notatka', 5.5)]
        self.assertEqual(notesService.averageOf('notatka'), 5.0)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_one_note(self, mock_method):
        notesService = NotesService()
        mock_method.return_value = [Note('notatka', 4.643)]
        self.assertEqual(notesService.averageOf('notatka'), 4.643)
        
    @patch.object(NotesStorage, 'clear')
    def test_clear(self, mock_method):
        notesService = NotesService()
        mock_method.return_value = None
        self.assertIsNone(notesService.clear())
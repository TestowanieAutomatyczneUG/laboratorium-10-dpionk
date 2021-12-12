import unittest
from functions.Note import Note
from parameterized import parameterized


class Test_note(unittest.TestCase):
    def test_note_ok(self):
        Note('notatka', 4.5)
        self.assertTrue(True)

    def test_note_name_jest_None(self):
        self.assertRaises(Exception, Note, None, 2.3)

    def test_note_name_jest_puste(self):
        self.assertRaises(Exception, Note, '', 3.2)

    def test_note_name_nie_jest_str(self):
        self.assertRaises(Exception, Note, 4545, 2.5)

    def test_note_name_nie_jest_str_2(self):
        self.assertRaises(Exception, Note, [], 6.0)

    def test_note_name_nie_jest_str_2(self):
        self.assertRaises(Exception, Note, False, 5.0)

    def test_note_note_nie_jest_float(self):
        self.assertRaises(Exception, Note, 'notatkaaa', '2.5')

    def test_note_note_nie_jest_float_2(self):
        self.assertRaises(Exception, Note, 'notatkaaa546546', None)

    def test_note_note_nie_jest_float_3(self):
        self.assertRaises(Exception, Note, 'daria', (3.0,5.7,6.2))

    @parameterized.expand([
		("notatka", 2.0),
        ("notatka", 2.5),
		("notatka", 3.0),
        ("notatka", 3.7),
		("notatka", 4.0),
        ("notatka", 4.8),
		("notatka", 5.0),
        ("notatka", 5.9),
		("notatka", 6.0)
	])

    def test_note_jest_poprawne(self, name, note):
        Note(name, note)
        self.assertTrue(True)

    @parameterized.expand([
		("notatka", 1.0),
        ("notatka", 1.999999),
        ("notatka", 7.0),
        ("notatka", 6.0000001),
	])

    def test_note_poza_przedzialem(self, name, note):
        self.assertRaises(Exception, Note, name, note)

    def test_getter_name(self):
        notatka = Note('notatka', 3.0)
        self.assertEqual(notatka.getName(), 'notatka')

    def test_getter_note(self):
        notatka = Note('notatka', 3.0)
        self.assertEqual(notatka.getNote(), 3.0)


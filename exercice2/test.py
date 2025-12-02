import unittest
from exercice2 import Film

class TestFilm(unittest.TestCase):

    def test_creation_et_json(self):
        f = Film("Titanic", "James Cameron", 1997, 9.5)
        self.assertEqual(f.titre, "Titanic")
        self.assertEqual(f.to_json(), '{"titre": "Titanic", "realisateur": "James Cameron", "annee": 1997, "note": 9.5}')

    def test_est_classique(self):
        f1 = Film("Matrix", "Wachowski", 1999, 8.7)
        f2 = Film("Inception", "Nolan", 2010, 9.0)
        self.assertTrue(f1.est_classique())
        self.assertFalse(f2.est_classique())

    def test_from_json(self):
        json_str = '{"titre": "Avatar", "realisateur": "James Cameron", "annee": 2009, "note": 7.8}'
        f = Film.from_json(json_str)
        self.assertEqual(f.titre, "Avatar")
        self.assertEqual(f.note, 7.8)

    def test_note_invalide(self):
        with self.assertRaises(ValueError):
            Film("Film test", "Réalisateur", 2020, 12)

    def test_tri_par_note(self):
        f1 = Film("Film A", "R1", 2001, 6.0)
        f2 = Film("Film B", "R2", 2002, 9.0)
        f3 = Film("Film C", "R3", 1999, 7.5)
        films = [f1, f2, f3]
        films.sort()
        self.assertEqual([f.note for f in films], [6.0, 7.5, 9.0])

if __name__ == "__main__":
    unittest.main()

import unittest
from storage import connect, add_meal, add_symptom, get_rows

class StorageTests(unittest.TestCase):
    def setUp(self): self.con=connect(':memory:')
    def tearDown(self): self.con.close()
    def test_meals(self):
        add_meal(self.con, '2026-10-16','Oatmeal', 200, 7.5)
        self.assertEqual(get_rows(self.con,'meals')[0]['calories'], 200)
    def test_bad_meal(self):
        with self.assertRaises(ValueError): add_meal(self.con, '2026-10-16','', -20)
    def test_symptoms(self):
        add_symptom(self.con,'2026-10-16','Fatigue',4)
        self.assertEqual(get_rows(self.con,'symptoms')[0]['severity'],4)
    def test_bad_severity(self):
        with self.assertRaises(ValueError): add_symptom(self.con,'2026-10-16','Pain',12)
if __name__ == '__main__': unittest.main()

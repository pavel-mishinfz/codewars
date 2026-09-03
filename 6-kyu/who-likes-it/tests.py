import unittest
from .solution import likes


class TestWhoLikesIt(unittest.TestCase):
    def test_no_one(self):
        self.assertEqual(likes([]), 'no one likes this')
        
    def test_one_name(self):
        self.assertEqual(likes(['Peter']), 'Peter likes this')
        
    def test_two_names(self):
        self.assertEqual(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    
    def test_three_names(self):
        self.assertEqual(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        
    def test_four_names_or_more(self):
        self.assertEqual(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
        self.assertEqual(likes(['Alex', 'Jacob', 'Mark', 'Max', 'Pavel']), 'Alex, Jacob and 3 others like this')
        
    def test_same_names(self):
        self.assertEqual(likes(['Alex', 'Alex', 'Alex', 'Alex', 'Alex']), 'Alex, Alex and 3 others like this')
        
    def test_name_and_surname(self):
        self.assertEqual(likes(['Peter Ivanov']), 'Peter Ivanov likes this')
        self.assertEqual(likes(['Alex A', 'Jacob J', 'Mark M', 'Max M', 'Pavel P']), 'Alex A, Jacob J and 3 others like this')
        
    def test_random_names(self):
        import uuid
        
        n1 = str(uuid.uuid4())
        n2 = str(uuid.uuid4())
        self.assertEqual(likes([n1, n2]), f'{n1} and {n2} like this')

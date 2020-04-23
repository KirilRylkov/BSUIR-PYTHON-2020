import sys
sys.path.append('./')

import json
import unittest
from time import perf_counter
from Cached.core import cached
from MyVector.core import Vector
from MySort.core import sort
from MyJson.core import from_json
from MyJson.core import to_json


class Test(unittest.TestCase):

    def test_my_vector(self):
        vector = Vector([1, 2, 3])
        self.assertEqual(vector, Vector([1, 2, 3]))
        self.assertEqual(repr(vector), '[1, 2, 3]')
        self.assertEqual(str(vector), 'Vector(1, 2, 3)')
        vector[2] = 4
        self.assertNotEqual(vector, Vector([4, 5, 6]))
        self.assertNotEqual(vector, Vector([4, 5, 6, 7]))
        self.assertNotEqual(vector, "qewew")
        self.assertEqual(len(vector), len(Vector([1, 2, 3])))
        self.assertEqual(vector + Vector([1, 2, 3]), Vector([2, 4, 7]))
        self.assertEqual(vector - Vector([1, 2, 3]), Vector([0, 0, 1]))
        self.assertEqual(vector * 100, Vector([100, 200, 400]))
        self.assertEqual(vector * Vector([1, 1, 1]), 7)
        self.assertEqual(str(Vector([])), "Vector()")
        self.assertEqual(vector[0], 1)
        self.assertEqual(-vector, Vector([-1, -2, -4]))
        vector += vector
        vector -= Vector([1, 1, 1])
        vector *= 2
        self.assertEqual(vector, Vector([2, 6, 14]))
        self.assertEqual(abs(Vector([2, 0])), 2)
        self.assertEqual(bool(Vector([2, 1])), True)
        self.assertEqual(bool(Vector([])), False)

        with self.assertRaises(Exception):
            vector["yty"] = "fasd"
        with self.assertRaises(Exception):
            vector = Vector([1, "faded"])

    sort("input.txt", "output.txt")

    def test_my_sort(self):
        def check_file(file_name="output.txt"):
            with open(file_name) as file:
                current = file.readline()
                while current:
                    next = file.readline()
                    if int(current) > int(next):
                        return False
                    current = file.readline()
            return True

        self.assertTrue(check_file())

    def test_sort_exception(self):
        with self.assertRaises(Exception):
            sort("input.txt", "output.txt" ,-2)
        with self.assertRaises(Exception):
            sort("bad_input.txt", "output.txt")

    def test_my_to_json(self):
        self.assertEqual(
            from_json(
                '{ \t"name": "John", "age": 30, "isAdmin": false,"courses": ["html", "css", "js", "hhhh\"], "wife": null, "tre": true, "wewq": [],"re": 12.1}'),
            json.loads(
                '{ \t"name": "John", "age": 30, "isAdmin": false,"courses": ["html", "css", "js", "hhhh\"], "wife": null, "tre": true, "wewq": [], "re": 12.1}'))
        self.assertEqual(from_json('{}'), json.loads('{}'))
        with self.assertRaises(Exception):
            from_json('[')

    def test_to_json(self):
        obj = {"asfd": None, "asdf": 30, "asdf": 30.123, "agfds": False, "fdsad": "asd", "sdfg": True, "gsdf": [],"asdf": "dsaf","empty": {},"cards": ["14", "21", "234.234" "qweEe+", False, True, None, 12, 12.1, [], {}, [1, 2, 3.4]]}
        self.assertEqual(to_json(obj), json.dumps(obj))

    def test_my_cached(self):
        @cached
        def fib(n):
            if n < 2:
                return n
            else:
                return fib(n - 1) + fib(n - 2)

        first = perf_counter()
        fib(200)
        second = perf_counter()
        fib(200)
        fib(200)
        third = perf_counter()
        self.assertLess(third - second, second - first)



if __name__ == '__main__':
    unittest.main()

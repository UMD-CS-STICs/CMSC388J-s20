import unittest
import practice as p
import random
import collections
import operator

class TestPythonPractice(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual('Hello, World!', p.hello_world())

    def test_empty_sum_unique(self):
        l = []
        self.assertEqual(0, p.sum_unique(l))
    
    def test_sum_unique(self):
        copies = random.randint(2, 10)

        self.assertEqual(9, p.sum_unique(([5] * copies) + [4]))

        copies = random.randint(2, 10)
        l1 = [1, 2, 4, 5] * copies
        random.shuffle(l1)

        self.assertEqual(12, p.sum_unique(l1))

        copies = random.randint(2, 10)

        self.assertEqual(4, p.sum_unique([4] * copies))
    
    def test_single_element_palindrome(self):
        self.assertTrue(p.palindrome(''))
        self.assertTrue(p.palindrome('f'))
        self.assertTrue(p.palindrome('7'))
    
    def test_longer_palindromes(self):
        self.assertTrue(p.palindrome('aa'))
        self.assertTrue(p.palindrome(33))
        self.assertFalse(p.palindrome('ab'))
        self.assertFalse(p.palindrome(48))

    def test_even_longer_palindromes(self):
        self.assertTrue(p.palindrome('racecar'))
        self.assertTrue(p.palindrome(1337331))
        self.assertFalse(p.palindrome('python'))
        self.assertFalse(p.palindrome(1234567))

    def test_small_sum_multiples(self):
        self.assertEqual(0, p.sum_multiples(2))
        self.assertEqual(0, p.sum_multiples(3))

        self.assertEqual(3, p.sum_multiples(5))
        self.assertEqual(8, p.sum_multiples(6))
        self.assertEqual(14, p.sum_multiples(7))
    
    def test_large_sum_multiples(self):
        self.assertEqual(60, p.sum_multiples(16))
        self.assertEqual(143, p.sum_multiples(25))
        self.assertEqual(354858, p.sum_multiples(1234))
    
    def test_empty_lists_num_func_mapper(self):
        nums = []
        funs = [p.sum_unique, sum]
        self.assertEqual([0, 0], p.num_func_mapper(nums, funs))

        nums = [2, 2, 2, 4, 5]
        funs = []
        self.assertEqual([], p.num_func_mapper(nums, funs))
    
    def test_num_func_mapper_1(self):
        nums = [2, 2, 2, 4, 5]
        funs = [p.sum_unique, sum]
        self.assertEqual([11, 15], p.num_func_mapper(nums, funs))
    
    def test_num_func_mapper_2(self):
        def most_occurring(nums):
            c = collections.Counter(nums)
            # Returns key in dict with highest value
            return max(c.items(), key=operator.itemgetter(1))[0]

        nums = [2, 2, 2, 4, 5, 8, 9]
        funs = [sum, max, most_occurring]
        self.assertEqual([32, 9, 2], p.num_func_mapper(nums, funs))

    def test_pythagorean_triples(self):
        self.assertEqual([(3, 4, 5)], p.pythagorean_triples(10))
        self.assertEqual([(3, 4, 5), (6, 8, 10)], p.pythagorean_triples(11))
        self.assertEqual([(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17)],
                         p.pythagorean_triples(20))

if __name__ == '__main__':
    unittest.main()
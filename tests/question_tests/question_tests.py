#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config


#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import is_prime
from src.question_b.question_b import get_miles_per_hour
from src.question_c.question_c import get_sum_of_evens
from src.question_d.question_d import get_day_of_week

class Test_Config(unittest.TestCase):


    def test_is_prime(self):
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(11), True)



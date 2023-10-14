#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
#from src.question_a.question_a import test_config


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


    def test_get_miles_per_hour(self):
        self.assertEqual(19.883872, get_miles_per_hour(32, 60))

    def test_get_sum_of_evens(self):
       self.assertEqual(30, get_sum_of_evens(11))
       self.assertEqual(30, get_sum_of_evens(10))
       self.assertEqual(20, get_sum_of_evens(8))
    


    def test_question_d(self):
        self.assertEqual(get_day_of_week(0),'Invalid Number')
        self.assertEqual(get_day_of_week(1),'Monday')
        self.assertEqual(get_day_of_week(2),'Tuesday')
        self.assertEqual(get_day_of_week(3),'Wednesday')
        self.assertEqual(get_day_of_week(4),'Thursday')
        self.assertEqual(get_day_of_week(5),'Friday')
        self.assertEqual(get_day_of_week(6),'Saturday')
        self.assertEqual(get_day_of_week(7),'Sunday')
        self.assertEqual(get_day_of_week(8),'Invalid Number')

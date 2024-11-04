import unittest
import re

from skeleton_code.bootcamp_exercise_marker import *
from unittest.mock import patch
from io import StringIO as sio

class BootcampExerciseMarkerTest(unittest.TestCase):

    @patch('sys.stdin', sio('C\n'))
    def test_display_question_and_choices_1(self):
        '''
        Testing std output of one question 
        '''
        with patch ('sys.stdout', new = sio()) as output:
            question = 'How many leaves are in a tree?, C, A - 23, B - 45, C - 78'
            q_num = 1
            display_question(q_num, question)
            self.assertEqual(output.getvalue(),'''1. How many leaves are in a tree?
A - 23
B - 45
C - 78
''')


    @patch('sys.stdin', sio('C\n'))
    def test_display_question_and_choices_2(self):
        '''
        Testing std output of one question 
        '''
        with patch ('sys.stdout', new = sio()) as output:
            question = 'How many leaves are in a tree?, C, A - 23, B - 45, C - 78'
            q_num = 2
            display_question(q_num, question)
            self.assertEqual(output.getvalue(),'''2. How many leaves are in a tree?
A - 23
B - 45
C - 78
''')


    @patch('sys.stdin', sio('C\n'))
    def test_display_question_and_choices_3(self):
        '''
        Testing std output of one question 
        '''
        with patch ('sys.stdout', new = sio()) as output:
            question = 'How many leaves are in a tree?, C, A - 23, B - 45, C - 78'
            q_num = 3
            display_question(q_num, question)
            self.assertEqual(output.getvalue(),'''3. How many leaves are in a tree?
A - 23
B - 45
C - 78
''')


    @patch('sys.stdin', sio('C\n'))
    def test_display_question_and_choices_4(self):
        '''
        Testing std output of one question 
        '''
        with patch ('sys.stdout', new = sio()) as output:
            question = 'How many leaves are in a tree?, C, A - 23, B - 45, C - 78'
            q_num = 4
            display_question(q_num, question)
            self.assertEqual(output.getvalue(),'''4. How many leaves are in a tree?
A - 23
B - 45
C - 78
''')


    @patch('sys.stdin', sio('C\n'))
    def test_display_question_and_choices_5(self):
        '''
        Testing std output of one question 
        '''
        with patch ('sys.stdout', new = sio()) as output:
            question = 'How many leaves are in a tree?, C, A - 23, B - 45, C - 78'
            q_num = 5
            display_question(q_num, question)
            self.assertEqual(output.getvalue(),'''5. How many leaves are in a tree?
A - 23
B - 45
C - 78
''')

    @patch('sys.stdin', sio('C\n'))
    def test_valid_answer_input(self):
        '''
        Testing std input of one question 
        '''
        question = 'How many leaves are in a tree?, C, A - 23, B - 45, C - 78'
        q_num = 1
        answer = display_question(q_num, question)
        
        self.assertTrue(isinstance(answer, str))
        self.assertEqual(1, len(answer))
        self.assertTrue(re.match("[A-C]", answer))
        
        
    def test_read_file_return_equal_to_five(self):
        '''
        Testing that read_file() returns a list of length 5
        '''        
        self.assertTrue(len(read_file()) == 5)


    def test_read_file_return_length_not_greater_than_5(self):
        '''
        Testing that read_file() does not return a list of length greater than 5
        '''
        self.assertFalse(len(read_file()) > 5)


    def test_read_file_return_length_not_less_than_five(self):
        '''
        Testing that read_file() does not return a list of length shorter than 5
        '''
        self.assertFalse(len(read_file()) < 5)


    def test_read_file_return_length_not_none(self):
        '''
        Testing that read_file() returns only a list
        '''
        self.assertFalse(len(read_file()) == None)


    def test_read_file_return_type(self):
        '''
        Testing that read_file() returns only a list
        '''
        self.assertTrue(isinstance(read_file(), list))
    
    
    def test_is_correct_answer(self):
        '''
        Testing that only True and False is returned by is_correct_answer()
        '''
        
        self.assertTrue(is_correct_answer('A', 'A'))
        self.assertTrue(is_correct_answer('C', 'C'))
        self.assertFalse(is_correct_answer('A', 'a'))
        self.assertFalse(is_correct_answer('B', 'b'))
        
    def test_is_correct_answer_does_not_correctly_handle_integer_values(self):
        '''
        Testing that only False is returned for invalid answers
        '''
        self.assertFalse(is_correct_answer('A', '1'))
        self.assertFalse(is_correct_answer('A', 1))


    def test_is_correct_answer_returns_boolean(self):
        '''
        Testing that only boolean value is returned
        '''
        self.assertTrue(isinstance(is_correct_answer('A', 'A'), bool))


    def test_moves_to_next_round(self):
        '''
        Testing that next_round() returns an incremented value after starting at round 0
        '''
        
        self.assertEqual(1, next_round(0))


    def test_moves_to_next_round_from_higher_round(self):
        '''
        Testing that next_round() returns an incremented value from round 2
        '''
        self.assertEqual(3, next_round(2))


    def test_next_round_does_not_return_same_value(self):
        '''
        Testing that next_round() does not return the same round number
        '''
        self.assertNotEqual(2, next_round(2))


    def test_next_round_does_not_decrement(self):
        '''
        Testing that next_round() does not return a decremented value
        '''
        self.assertNotEqual(2, next_round(3))


if __name__ == '__main__':
    unittest.main()
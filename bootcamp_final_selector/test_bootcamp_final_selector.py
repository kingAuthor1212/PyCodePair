import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
import bootcamp_final_selector

class TestBootcampFinalSelector(unittest.TestCase):
    @patch("sys.stdin", StringIO("StudentA\n"))
    @patch("builtins.print")
    def test_user_name(self):
        output = StringIO()
        sys.stdout = output

        result = bootcamp_final_selector.user_name()
        self.assertEqual(output.getvalue(), '''Enter username: ''')
        self.assertEqual(result,"studentA")
        sys.stdout = sys.__stdout__
    def test_user_name_valid(self, mock_print):
        result = bootcamp_final_selector.user_name()
        mock_print.assert_called_with("Username exists in the bootcampers list")
        self.assertEqual(result, "studentA")
    @patch("sys.stdin", StringIO("NonExistentUser\n"))
    @patch("builtins.print")

    def test_file_exists(self):
        # ask Sam for the relevant path
        boolean = os.path.isfile("bootcamp_final_selector/student_results.txt")
        self.assertEqual(boolean, True)


    def test_exam_score(self):
        exam_score = bootcamp_final_selector.exam_score([30, 10, 20])
        self.assertEqual(exam_score, 18)


    def test_exam_percentage(self):
        exam_percentage = bootcamp_final_selector.exam_percentage([30, 10, 20])
        self.assertEqual(exam_percentage, 18)


    def test_group_project_score(self):
        exam_score = bootcamp_final_selector.group_project_score([30, 10, 20])
        self.assertEqual(exam_score, 20)


    def test_group_project_percentage(self):
        exam_percentage = bootcamp_final_selector.group_project_percentage([30, 10, 20])
        self.assertEqual(exam_percentage, 50)


    def test_daily_exercise_score(self):
        exam_score = bootcamp_final_selector.daily_exercise_score([30, 10, 20])
        self.assertEqual(exam_score, 13)


    def test_daily_exercise_percentage(self):
        exam_percentage = bootcamp_final_selector.daily_exercise_percentage([30, 10, 20])
        self.assertEqual(exam_percentage, 13)


    def test_final_result(self):
        final_result = bootcamp_final_selector.final_result(18, 20, 13)
        self.assertEqual(final_result, 13)


    def test_first_class_pass(self):
        type_pass = bootcamp_final_selector.type_of_pass(91)
        self.assertEqual(type_pass, "First Class Pass")

    
    def test_pass(self):
        type_pass = bootcamp_final_selector.type_of_pass(45)
        self.assertEqual(type_pass, "Pass")


    def test_fail(self):
        type_pass = bootcamp_final_selector.type_of_pass(20)
        self.assertEqual(type_pass, "Fail")

if __name__ == '__main__':
    unittest.main()

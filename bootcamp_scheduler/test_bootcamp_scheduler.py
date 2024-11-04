# Abdur-Raheem Lee <abdur-raheem@wethinkcode.co.za>

import unittest
import sys

from ..skeleton_code.bootcamp_scheduler import *
from unittest.mock import patch
from io import StringIO as sio

class BootcampSchedulerTests(unittest.TestCase):

    @patch('sys.stdin', sio('H\n'))
    def test_home_screen_output(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            home_screen()
            self.assertEqual(output.getvalue(),'''Welcome to the Bootcamp Scheduler!
Would you like to [H]ost or [A]ttend a workshop?: ''')

    @patch('sys.stdin', sio('Host\n'))
    def test_home_screen_valid_host_input_1(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            home_screen()
            self.assertEqual(output.getvalue(),'''Welcome to the Bootcamp Scheduler!
Would you like to [H]ost or [A]ttend a workshop?: ''')

    @patch('sys.stdin', sio('H\n'))
    def test_home_screen_valid_host_input_2(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            home_screen()
            self.assertEqual(output.getvalue(),'''Welcome to the Bootcamp Scheduler!
Would you like to [H]ost or [A]ttend a workshop?: ''')

    @patch('sys.stdin', sio('host\n'))
    def test_home_screen_valid_host_input_3(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            home_screen()
            self.assertEqual(output.getvalue(),'''Welcome to the Bootcamp Scheduler!
Would you like to [H]ost or [A]ttend a workshop?: ''')

    @patch('sys.stdin', sio('h\n'))
    def test_home_screen_valid_host_input_4(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            home_screen()
            self.assertEqual(output.getvalue(),'''Welcome to the Bootcamp Scheduler!
Would you like to [H]ost or [A]ttend a workshop?: ''')

    @patch('sys.stdin', sio('Attend\n'))
    def test_home_screen_valid_attendee_input_1(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            home_screen()
            self.assertEqual(output.getvalue(),'''Welcome to the Bootcamp Scheduler!
Would you like to [H]ost or [A]ttend a workshop?: ''')

    @patch('sys.stdin', sio('A\n'))
    def test_home_screen_valid_attendee_input_2(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            home_screen()
            self.assertEqual(output.getvalue(),'''Welcome to the Bootcamp Scheduler!
Would you like to [H]ost or [A]ttend a workshop?: ''')

    @patch('sys.stdin', sio('attend\n'))
    def test_home_screen_valid_attendee_input_3(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            home_screen()
            self.assertEqual(output.getvalue(),'''Welcome to the Bootcamp Scheduler!
Would you like to [H]ost or [A]ttend a workshop?: ''')

    @patch('sys.stdin', sio('a\n'))
    def test_home_screen_valid_attendee_input_4(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            home_screen()
            self.assertEqual(output.getvalue(),'''Welcome to the Bootcamp Scheduler!
Would you like to [H]ost or [A]ttend a workshop?: ''')

    @patch('sys.stdin', sio('hosts\nh\n'))
    def test_home_screen_invalid_input_1(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            home_screen()
            self.assertEqual(output.getvalue(),'''Welcome to the Bootcamp Scheduler!
Would you like to [H]ost or [A]ttend a workshop?: 
Invalid input!

Would you like to [H]ost or [A]ttend a workshop?: ''')

    @patch('sys.stdin', sio('attends\na\n'))
    def test_home_screen_invalid_input_2(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            home_screen()
            self.assertEqual(output.getvalue(),'''Welcome to the Bootcamp Scheduler!
Would you like to [H]ost or [A]ttend a workshop?: 
Invalid input!

Would you like to [H]ost or [A]ttend a workshop?: ''')

    @patch('sys.stdin', sio('A\nJerry\nLoops\n'))
    def test_attendee_application_one_available_workshop(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            add_attendee()
            self.assertEqual(output.getvalue(),'''Please enter your name: 

Which workshop would you like to join?
- Loops
''')

    @patch('sys.stdin', sio('Natasha\nJSON\n'))
    def test_attendee_application_two_available_workshops(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            add_attendee()
            self.assertEqual(output.getvalue(),'''Please enter your name: 

Which workshop would you like to join?
- Loops
- JSON
''')

    @patch('sys.stdin', sio('Jerry\n'))
    def test_attendee_application_no_available_workshops(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            add_attendee()
            self.assertEqual(output.getvalue(),'''Please enter your name: 

There are currently no workshops available.''')

    @patch('sys.stdin', sio('Natasha\nJSON\n'))
    def test_updated_text_file_1(self):
        
        initial = read_file()
        add_attendee()
        current = read_file()
        
        self.assertNotEqual(initial, current)

    @patch('sys.stdin', sio('Jeff\nTDD\n10:00\nBeanbag Area\n'))
    def test_updated_text_file_2(self):
        
        initial = read_file()
        add_host()
        current = read_file()
        
        self.assertNotEqual(initial, current)

    @patch('sys.stdin', sio('Jeff\nTDD\n10:00\nBeanbag Area\n'))
    def test_add_host(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            add_host()
            self.assertEqual(output.getvalue(),'''Please enter your name: 
What is your workshop topic?: 
What time would you like to host it (hh:mm)?: 
Where would you like to host your workshop?: ''')

    @patch('sys.stdin', sio('Sam\nFunctions\n11h00\n11:00\nBeanbag Area\n'))
    def test_add_host_incorrect_time(self):
        
        with patch ('sys.stdout', new = sio()) as output:
            add_host()
            self.assertEqual(output.getvalue(),'''Please enter your name: 
What is your workshop topic?: 
What time would you like to host it (hh:mm)?: 
Incorrect time format!
What time would you like to host it (hh:mm)?: 
Where would you like to host your workshop?: ''')








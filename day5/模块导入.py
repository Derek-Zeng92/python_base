# from os import system
# system('df -h')

# from django.contrib.auto import authenticate as auth
# auth()

import sys
import os

print(__file__)
print(os.path.dirname(__file__))

import my_first_mod

my_first_mod.sayhi()

base_path = os.path.dirname(os.path.abspath(__file__)) + '/test'
sys.path.append(base_path)
import my_first_mod_test

my_first_mod_test.sayhi()

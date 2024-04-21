# 1. Write a Python program to import a built-in array module and display the namespace of the said module.

import array

for _ in array.__dict__:
    print(_)

# Simple
#!/usr/bin/env python

# https://python-essentials.readthedocs.io/en/latest/echo.html

while True:
  user_input = input("Enter some text: ")

  try:
    is_user_input_of_type_int = int(user_input)
    print("You entered an integer " + user_input)
    continue
  except ValueError:
    if user_input == 'quit':
      print("You entered quit. So quitting...")
      break
    else:
      print("You entered the string: " + user_input)


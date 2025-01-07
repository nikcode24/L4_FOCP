"""
4.	Write a program that takes a URL as a command-line argument and 
  reports whether or not there is a working website at that address. 
  Hint: You need to get the HTTP response code. Another 
  Hint: StackOverflow is your friend.
"""

import requests, sys
url = sys.argv[1:][0]


try:
  response = requests.get(url)
  print("The Status code is " ,response.status_code)
  if response.status_code == 200:
    print("The server response is Ok !")
except:
  print('The URL in Not Accessible !')
#!/usr/bin/env python3
import cgi
import os
from templates import login_page
from templates import secret_page
import secret

def get_cookie(_match): 
  if 'HTTP_COOKIE' in os.environ:
    cookies = os.environ['HTTP_COOKIE']
    cookies = cookies.split('; ')

    for cookie in cookies:
      if ('=' in cookie):
          (_key, _value) = cookie.split('=')
          if (_match == _key):
            return _value
  return('')


form = cgi.FieldStorage()

username = form.getfirst("username")
password = form.getfirst("password")


header = ""
header += "Content-Type: text/html\r\n"    # HTML is following


body = ""

if (get_cookie('Logged') == 'True'):
    body += secret_page(secret.username, secret.password)
    body += "<h1>A terrible secret</h1>"
elif (username is not None and password is not None):
    body += secret_page(username, password)
    header += "Set-Cookie: Logged=True" + "\r\n"
    body += "<h1>A terrible secret</h1>"
else:
    body += login_page()

print(header)
print()
print(body)

#!/usr/bin/env python 

"""
Author          :   Rahul Patil<http://www.linuxian.com>
Purpose         :   Send free sms using www.indyarocks.com
Date            :   Thu Jan  2 21:36:00 IST 2014
Dependencies    :   1. Your number MUST be register with  indyarocks
                    2. Python 2.7.3 Modules can be install using :
                         - pip install requests
                         - pip install docopt
Reports Bugs	:   https://github.com/rahulinux/sendsms/issues
"""
from __future__ import print_function
from docopt import docopt
import requests

usage = """
Usage:
        sendsms.py -u <username> -p <password> -to <send_to> -m	<msg>
        sendsms.py (-h | --help)
        sendsms.py --version

Note: if your password or message have special character then use double quotes 
"""


class	Sms(object):
		"""for login and send sms and logout """
		def __init__(self,username,password,send_to):
			self.username = username
			self.password = password
			self.send_to = send_to
			self.session = requests.session()
			self.session.headers.pop('User-Agent')
			self.session.headers['User-Agent'] = 'Mozilla/5.0 Firefox/0.8'
			
		def login(self):
			url = 'http://www.indyarocks.com/login'
			login_form = {
				'LoginForm[username]' : self.username,
				'LoginForm[password]' : self.password,
				'yt0':  'Login',
				}
			self.login_status = self.session.post(url, data=login_form)
			return self.login_status.text
			
		def send(self,sms_content):
			compose_sms_link = 'http://www.indyarocks.com/send-free-sms'
			send_sms_form = {
				'freeSmschkmemberVal' : 'NM',
				'FreeSms[mobile]' : self.send_to,
				'FreeSms[post_message]' : sms_content,
				'yt0' : 'SEND',
			}
			self.sent_status = self.session.post(compose_sms_link, data=send_sms_form)
                        return self.sent_status

		def logout(self):
			logout_link = 'http://www.indyarocks.com/logout'
			self.session.post(logout_link)
			

def main():
	sms = Sms(username,password,send_to)
	login_status = sms.login()
	if 'Logout' in login_status:
		print("Successfully Login with UserID: {}".format(username))
	else:	
		print("Incorrect Username/Passoword")
		raise SystemExit(1)
        sms_status = sms.send(text)
	msg = 'Your Message has been sent successfully'
	sms_error = 'Error! Too many SMS-es sent'
        if msg in sms_status.text:
                print("{} [ {} ]".format(msg,send_to))
	else:
		print(sms_error if sms_error in sms_status.text else "" )
		print('Somethng is bad\nPer Day only 100 SMS-es allowed')
	sms.logout()
			
	
if __name__ == '__main__':
	args = docopt(usage,version='sendsms.py version 0.1 by Rahul Patil<http://linuxian.com>')
	username, password, send_to = args['<username>'], args['<password>'], args['<send_to>']
	text = args['<msg>']
	main()

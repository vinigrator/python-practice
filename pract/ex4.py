
import re

def preg_match_email(email):
    return False if re.match(r'\w{5,}@[a-zA-Z-]+\.ru',email) is None else True
	
print preg_match_email("w.ow@hey.com")
print preg_match_email("wowemail@hey-you.ru")
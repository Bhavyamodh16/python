import re
email="""email received june 2 from user1@gmail.com
         email received june 2 from user1@gmail.com
         email rejected june 2 from invalid_email@email.com"""
print(re.findall(r"\w+@\w+\.\w+", email))
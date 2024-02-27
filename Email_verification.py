import re

def email_val(email):
    formato_val = r"^([a-z0-9]+[-_.])*[a-z0-9]+@[a-z0-9]+(\.[a-z]{2,})+$"
    if re.match(formato_val, email, re.IGNORECASE):
        return True
    return False

email = email_val("juan@gmail.com")
print(email)
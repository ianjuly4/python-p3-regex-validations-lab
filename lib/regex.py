import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"John Cena|Anya Taylor-Joy|D'Angelo" 
name_regex = re.compile(name)

phone_number = r"[5]{10}|[5]{3}\S[5]{3}\S[5]{4}|\S[5]{3}\S [5]{3}\S[5]{4}"
phone_regex = re.compile(phone_number)

email_address = r"^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$|^[a-zA-Z]+\.[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$|^[a-zA-Z]+\.[a-zA-z]+[0-9]+@[a-zA-Z]+\.[a-zA-z]+$"
email_regex = re.compile(email_address)

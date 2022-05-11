phoneRegex = re.compile(r'(\d{3}-)? \d{3}-d{4}')
mo1 = phoneRegex.search('My number is 415-555-4888')
mo1.group()
print(mo1)
#! /home/viniciusbraga/.pyenv/shims/python
# phoneAndEmail.py - Encontrar números de telefone e endereços de email no clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # (?) grupo opcional, correspondendo a textos que contém ou não o padrão.
# código de área
(\s|-|\.)? #(s) caracteres de espaço
# separador (-) (.)
(\d{4} |\s |\. )
# primeiros 3 dígitos
(\s|-|\.)
# separador
(\d{4})
# últimos 4 dígitos
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extensão
)''', re.VERBOSE)

#Regex para email.
emailRegex = re.compile(r'''(
[a-zA-z0-9._%+-]+ #nome do usuário
@ #simbolo
[a-zA-Z0-9.-]+
# nome do domínio-
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

#Econtra as correspondências no texto do clipboard.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if __name__== "__main__":
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to Clipboard: ')
        print('\n'.join(matches))
    else:
        print('No phone numbers or emaill addresses found ')



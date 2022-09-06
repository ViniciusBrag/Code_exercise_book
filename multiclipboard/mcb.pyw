# mcb.pyw – Salva e carrega porções de texto no clipboard.
# Usage: py.exe mcb.pyw save <palavra-chave> – Salva clipboard na palavra-chave.
#py.exe mcb.pyw <palavra-chave> - Carrega palavra-chave no clipboard.
#py.exe mcb.pyw list – Carrega todas as palavras-chave no clipboard.

import shelve, sys
import pyperclip

mcb_shelf = shelve.open('mcb')


if len(sys.argv) == 3 and sys.argv[1].lower == 'save':
    mcb_shelf[sys.argv[2]] == pyperclip.paste()

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()           
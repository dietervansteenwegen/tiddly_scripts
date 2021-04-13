"""
Get user input and format it for use in my Tiddlywiki consumbles table

Tiddlywiki: https://tiddlywiki.com/
"""

import sys  # to check python version
# for easy access to clipboard use tkinter, but package name differs between python v2 and v3. First check.
if sys.version_info.major == 3:
    from tkinter import Tk
else:
    from Tkinter import Tk


def get_line():
    what = input("What:").strip()
    product = input("Product:").strip() or ''
    supplier = input("Supplier:").strip() or ''
    part_no = input("Part no: ").strip() or ''
    url = input('URL (enter for none): ').strip() or None
    price = input('Price: ').strip() or ''
    currency = input('Currency (enter for Euro): ') or None
    quantity = input('Quantity (enter for single): ').strip() or 1
    if url:
        part_no = '[[{}|{}]]'.format(part_no, url)
    price = '{} {}'.format(price,
                           currency) if currency else '€{}'.format(price)
    if not quantity == 1:
        price = '{}/{}'.format(price, quantity)
    rtn = '| {} |{} | {} | {} | {} |\n\r'.format(what, product, supplier, part_no,
                                             price)
    another = input('Another product? (y for another, enter to get result)')
    return rtn, another


def print_and_clipboard(result):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(result)
    r.update()
    r.destroy()
    print(result)


def main():
    result = ''
    another = True

    while another:
        line, another = get_line()
        result += line

    print_and_clipboard(result)
    # exit
    input('Data copied to clipboard, press enter to exit...')


if __name__ == '__main__':
    main()
else:
    print('not to be used as a module. Exiting...')

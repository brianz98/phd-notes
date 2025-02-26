#!/bin/python

import subprocess as sp

def parse_bib(filename):
    """
    Parse a bib file and return a list of entries, i.e.,
    @type1{...}
    @type2{...}
    -> ['@type1{...}', '@type2{...}']
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        strings = []
        entries = []
        for line in lines:
            if line.strip() == '':
                continue
            if '@string' in line:
                strings.append(line)
            elif '@' in line:
                temp = [line]
            elif line.strip() == '}':
                temp.append(line)
                entries.append(''.join(temp))
            else:
                temp.append(line)
    d = {}
    for i in entries:
        key = i.split('{')[1].split(',')[0]
        d[key] = i
    return strings, dict(sorted(d.items()))

def generate_bib(strings, d, filename):
    """
    Generate a bib file from a list of strings and a dictionary of entries.
    """
    with open(filename, 'w') as f:
        for i in strings:
            f.write(i)
        for i in d.values():
            f.write(i)
    return

if __name__ == "__main__":
    sp.call('cp main.bib main.bib.bak', shell=True)
    strings, d = parse_bib('main.bib')
    generate_bib(strings, d, 'main.bib')
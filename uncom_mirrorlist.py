ml = 'mirrors.txt'
out = 'mirrorlist'

with open(ml, 'r', encoding='UTF-8') as ifile, \
        open(out, 'w', encoding='UTF-8') as ofile:
    lines = ifile.readlines()

    for line in lines[:6]:
        ofile.write(line.strip() + '\n')

    for line in lines[6:]:
        line = line.strip()
        if line:
            assert line[0] == '#'
        ofile.write(line[1:] + '\n')


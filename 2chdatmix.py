# coding: UTF-8
import codecs
import sys
import re


def datmix():
    f_out = codecs.open(args[1], 'w', 'shift_jis')
    anchorreg = re.compile(r'&gt;&gt;(\d+)')
    namereg = re.compile(r'^(\d+)<')
    lessnum = 0
    margin = 0

    for i, arg in enumerate(args):
        # skip args 0 1
        if i == 0 or i == 1:
            continue

        f_in = codecs.open(arg, 'r', 'shift_jis', "ignore")
        lines = f_in.readlines()
        f_in.close()

        lessnum = 0
        for line in lines:
            lessnum += 1

            # replace name
            name = namereg.match(line)
            if name is not None:
                name = int(name.groups()[0]) + margin
                line = re.sub(namereg, str(name) + '<', line)

            # replace anchor
            anchor = anchorreg.findall(line)
            if anchor:
                for a in anchor:
                    a = int(a) + margin
                    line = re.sub(anchorreg, "&gt;&gt;" + str(a), line)

            f_out.write(line)

        margin += lessnum

    f_out.close()


if __name__ == '__main__':
    args = sys.argv
    if 1 == len(args) or 2 == len(args):
        print('datmix.py [outputdat] [inputdats]')
    else:
        datmix()
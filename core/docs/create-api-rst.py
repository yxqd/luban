#!/usr/bin/env python


starttoken = '%{'
endtoken = '%}'


class Block:

    def __init__(self, startlineno, endlineno):
        self.startlineno = startlineno
        self.endlineno = endlineno
        return


    def __str__(self):
        return 'Block(%s, %s)' % (self.startlineno, self.endlineno)


def convert(lines):
    starts = []; ends = []
    for i, line in enumerate(lines):
        if line == starttoken: starts.append(i)
        elif line == endtoken: ends.append(i)
        continue
    assert len(starts) == len(ends), 'number of block starts do not match number of block ends'
    for start, end in zip(starts, ends):
        assert start < end, 'block mismatch: start: %s, end: %s' % (start, end)
        continue

    for i in range(len(starts)-1):
        assert ends[i] < starts[i+1], 'block overlap: end of block %d: %s, start of block %d: %s' % (
            i, ends[i], i+1, starts[i+1])
        continue
    
    blocks = [Block(start, end) for start, end in zip(starts, ends)]

    ret = []
    from api_doc_generator import widget_doc
    env = {'widget_doc': widget_doc}
    prev = 0
    for block in blocks:
        ret += lines[prev: block.startlineno]
        ret += eval(lines[block.startlineno+1], env)
        prev = block.endlineno+1
        continue
    if blocks:
        ret += lines[blocks[-1].endlineno+1:]
    else:
        ret = lines
    return ret


def main():
    import sys
    filename = sys.argv[1]
    lines = open(filename).read().splitlines()
    lines = convert(lines)
    open('API.rst', 'w').write('\n'.join(lines))
    return


if __name__ == '__main__': main()

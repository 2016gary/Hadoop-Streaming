import sys

for line in sys.stdin:
    line = line.strip()
    values = line.split('\t')
    for i in range(len(values)):
        if i > 1:
            print('%s\t%s' % (values[0], values[i]))
            vote = float(values[1]) / (len(values) - 2)
            print('%s\t%s' % (values[i], vote))

sys.exit(0)

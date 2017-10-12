import sys

for line in sys.stdin:
    line = line.strip()
    key, count = line.split("\t", 1)
    key1, key2 = key.split("-", 1)
    print('%s\t%s\t%s' % (key1, key2, count))
    print('%s\t%s\t%s' % (key2, key1, count))

sys.exit(0)

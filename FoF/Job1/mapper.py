import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split("\t")
    key1 = words[0]
    for key2 in words[1:]:
        if key1 > key2:
            print('%s-%s\t%s' % (key2, key1, 0))
        else:
            print('%s-%s\t%s' % (key1, key2, 0))
    i = 1
    for key_1 in words[1:]:
        for key_2 in words[i + 1:]:
            if key_1 > key_2:
                print('%s-%s\t%s' % (key_2, key_1, 1))
            else:
                print('%s-%s\t%s' % (key_1, key_2, 1))
        i = i + 1

sys.exit(0)

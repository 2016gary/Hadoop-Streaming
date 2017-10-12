import sys

current_key = None
key = None
current_count = []
for line in sys.stdin:
    line = line.strip()
    key, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_key == key:
        current_count.append(count)
    else:
        if current_key:
            current_count.sort()
            if current_count[0] > 0:
                print('%s\t%s' % (current_key, sum(current_count)))
            current_count = [count]
        else:
            current_count.append(count)
        current_key = key

current_count.sort()
if current_count[0] > 0:
    print('%s\t%s' % (current_key, sum(current_count)))

sys.exit(0)

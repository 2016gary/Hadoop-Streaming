import sys

current_key = None
current_value = []
result = ''


def get_count(c):
    return c[1]


for line in sys.stdin:
    line = line.strip()
    key1, key2, count = line.split('\t', 2)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_key == key1:
        current_value.append((key2, count))
    else:
        if current_key:
            current_value = sorted(current_value, key=get_count, reverse=True)
            for tuple_str in current_value:
                result += tuple_str[0] + ':' + str(tuple_str[1]) + ','
            print('%s\t%s' % (current_key, result))
            result = ''
        current_key = key1
        current_value = [(key2, count)]

if current_key:
    current_value = sorted(current_value, key=get_count, reverse=True)
    for tuple_str in current_value:
        result += tuple_str[0] + ':' + str(tuple_str[1]) + ','
    print('%s\t%s' % (current_key, result))

sys.exit(0)

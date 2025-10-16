from collections import Counter

def repeting_num(sequence):
    num_counts = Counter(sequence)
    most_common_num = num_counts.most_common(3)
    for key, value in sorted (most_common_num, key = lambda x: x[0]):
        print(key, 'встречается', value, 'раз(а)')

sequence = '123456789876543'
repeting_num(sequence)
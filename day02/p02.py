from itertools import combinations

input_file = 'day02/p01_input.txt'

def get_input(filename):
    with open(filename) as f:
        return f.readlines()

def get_one_letter_difference(data):
    tmp = combinations(data, 2)
    for combi in tmp:
        zipped = zip(combi[0].strip(), combi[1].strip())
        if len([(left, right) for (left, right) in zipped if left.strip() != right.strip()]) == 1:
            return (combi[0].strip(), combi[1].strip())

if __name__ == "__main__":

    test_data = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

    assert get_one_letter_difference(test_data) == ('fghij', 'fguij')

    data = get_input(input_file)
    two_ids = get_one_letter_difference(data)

    result = ''.join([x for (x, y) in zip(two_ids[0], two_ids[1]) if x == y ])

    print('2 IDs:', two_ids)
    print('Difference removed:', result)

from collections import Counter

input_file = 'day02/p01_input.txt'

def get_input(filename):
    with open(filename) as f:
        return f.readlines()

def get_multiples(data, count):
    return sum([1 for entry in data if count in Counter(entry).values()])

if __name__ == "__main__":

    test_data = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

    assert get_multiples(test_data, 2) == 4
    assert get_multiples(test_data, 3) == 3

    data = get_input(input_file)
    doubles = get_multiples(data, 2)
    triples = get_multiples(data, 3)

    print('Doubles:', doubles)
    print('Triples:', triples)
    print('Checksum:', doubles * triples)

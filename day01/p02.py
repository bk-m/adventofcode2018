def input_generator(starting_value):
    with open('day01/p01_input.txt') as f:
        for line in f.readlines():
            if line[0] == '+':
                starting_value += int(line[1:])
            else:
                starting_value -= int(line[1:])
            yield starting_value

if __name__ == "__main__":

    result = 0
    result_set = set()
    generator = input_generator(result)

    while result not in result_set:
        try:
            if result is not None:
                print(result)
                result_set.add(result)
            result = next(generator)
        except StopIteration:
            print("*** StopIteration")
            generator = input_generator(result)
            result = None

    print('--------')
    print(result)

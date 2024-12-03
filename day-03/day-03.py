if __name__ == '__main__':
    total = 0
    with open('mul.txt') as infile:
        do = True
        lines = infile.readlines()
        for line in lines:
            parts = line.split('mul(')
            for part in parts:
                if ')' not in part:
                    continue
                input_str = part.split(')')[0]
                if ',' not in input_str:
                    continue
                try:
                    a, b = input_str.split(',')
                    result = int(a) * int(b)
                    if do:
                        total += result
                except:
                    a = 1
                if "do()" in part:
                    do = True
                if "don't()" in part:
                    do =  False

    print(total)


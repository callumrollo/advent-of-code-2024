import numpy as np

def count_xmas(arr, i, j, total):
    if ''.join(arr[i, j:j+4]) == 'XMAS':
        total+=1
    if ''.join(arr[i, j-4:j]) == 'SAMX':
        total+=1
    if ''.join(arr[i:i+4, j]) == 'XMAS':
        total+=1
    if ''.join(arr[i-4:i, j]) == 'SAMX':
        total+=1
    if i<=136 and j<=136:
        if ''.join((arr[i, j], arr[i+1, j+1], arr[i+2, j+2], arr[i+3, j+3])) == 'XMAS':
            total+=1
    if i>=3 and j>=3:
        if ''.join((arr[i-3, j-3], arr[i-2, j-2], arr[i-1, j-1], arr[i, j])) == 'SAMX':
            total+=1
    if i>=3 and j<=136:
        if ''.join((arr[i, j], arr[i-1, j+1], arr[i-2, j+2], arr[i-3, j+3])) == 'XMAS':
            total+=1
    if i<=136 and j>=2:
        if ''.join((arr[i+3, j-3], arr[i+2, j-2], arr[i+1, j-1], arr[i, j])) == 'SAMX':
            total+=1
    return total
    

if __name__ == '__main__':
    total = 0

    with open('wordsearch.txt') as infile:
        in_lines = []
        lines = infile.readlines()
        for line in lines:
            in_lines.append(list(line)[:-1])
    arr = np.array(in_lines)
    print(np.shape(arr))
    for i in range(np.shape(arr)[0]):
        for j in range(np.shape(arr)[1]):
            if arr[i,j] == 'X':
                total = count_xmas(arr, i, j, total)
    print("total: ", total)

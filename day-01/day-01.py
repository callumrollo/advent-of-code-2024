import pandas  as pd
import numpy as np
from collections import Counter

if __name__ == "__main__":
    df = pd.read_csv("locations_ids.txt", sep='   ', names=['a', 'b'])
    a = np.sort(df.a.values)
    b = np.sort(df.b.values)
    difference = np.abs(a - b)
    print(sum(difference))
    left_ids = Counter(a)
    right_ids = Counter(b)
    score = 0
    for id in a:
        if id in right_ids.keys():
            score += id * right_ids[id]
    print(score)


    

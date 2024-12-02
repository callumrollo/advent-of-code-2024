import pandas  as pd
import numpy as np
from collections import Counter
good = 0


def safety(nums):
    diffs = np.diff(nums)
    if (diffs > 0).all() or (diffs < 0 ).all():
        steps = np.abs(diffs)
        if (steps <=3).all():
            return True
    return False



if __name__ == "__main__":
    df = pd.read_csv("levels.txt", sep=',', names=['a'])
    good = 0
    for i, row in df.iterrows():
        nums = np.array(row.a.split(' ')).astype(int)
        if safety(nums):
            good+=1
            continue
        num_list = list(nums)
        safe_cut = False
        for j in range(len(nums)):
            sub_list = num_list.copy()
            sub_list.pop(j)
            if safety(np.array(sub_list)):
                safe_cut = True
                continue
        if safe_cut:
            good+=1

    print(good)

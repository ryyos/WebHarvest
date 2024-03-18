
from typing import List

def split_list(datas: List[any], length_each: int):
    results: List[any] = []
    for i in range(0, len(datas), length_each):
        results.append(datas[i:i+length_each])
    return results

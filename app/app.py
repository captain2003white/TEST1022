from collections import defaultdict
from typing import List

def dedupe_header(columns: List[str]) -> List[str]:
    """
    通过向重复项附加数字后缀，使标题列名唯一。
    """
    seen_counts = defaultdict(int)
    result: List[str] = []

    for col in columns:
        count = seen_counts[col]
        if count == 0:
            result.append(col)
        else:
            result.append(f"{col}.{count}")
        seen_counts[col] += 1

    return result

def add_numbers(a: int, b: int) -> int:
    """
    新功能：两个数字相加
    """
    return a + b

def filter_even_numbers(numbers: List[int]) -> List[int]:
    """
    新功能：过滤出列表中的偶数
    """
    return [num for num in numbers if num % 2 == 0]

def capitalize_words(words: List[str]) -> List[str]:
    """
    新功能：将字符串列表中的每个单词首字母大写
    """
    return [word.capitalize() for word in words]
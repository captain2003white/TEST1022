from app.app import dedupe_header, add_numbers, filter_even_numbers, capitalize_words

def test_unique_columns():
    assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"]

def test_duplicate_columns():
    assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"]

def test_mixed_columns():
    cols = ["id", "name", "id", "name", "name"]
    expected = ["id", "name", "id.1", "name.1", "name.2"]
    assert dedupe_header(cols) == expected

def test_add_numbers():
    """测试加法功能"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_filter_even_numbers():
    """测试过滤偶数功能"""
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filter_even_numbers([1, 3, 5]) == []
    assert filter_even_numbers([2, 4, 6]) == [2, 4, 6]

def test_capitalize_words():
    """测试单词首字母大写功能"""
    assert capitalize_words(["hello", "world"]) == ["Hello", "World"]
    assert capitalize_words(["python", "git", "github"]) == ["Python", "Git", "Github"]
    assert capitalize_words([]) == []
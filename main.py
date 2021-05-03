if __name__ == '__main__':
    # Task 1
    """
    Make a program that has some sentence (a string) on input and returns a dict containing 
    all unique words as keys and the number of occurrences as values. 
    """

    sentence = "It was a bright cold day in April and the clocks were striking thirteen"

    words_in_sentence = sentence.split()
    a_dict = {i: words_in_sentence.count(i) for i in set(words_in_sentence)}
    print(a_dict)

    # Task 2
    """
    Input data:
    
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    Create a function which takes as input two dicts with structure mentioned above, 
    then computes and returns the total price of stock.
    """
    sum = 0
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }

    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    for key, values in stock.items():
        if prices.get(key):
            sum += values * prices.get(key)
    print(sum)

    # Task 3
    """
    List comprehension exercise
    
    Use a list comprehension to make a list containing tuples (i, j) 
    where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
    """

    res = [(i, i * i) for i in range(1, 11)]
    print(res)

    # Task STAR

    week_dict = dict(Monday=1, Tuesday=2, Wednesday=3, Thursday=4, Friday=5, Saturday=6, Sunday=7)
    reverse_week_dict = {value: key for key, value in week_dict.items()}
    print(reverse_week_dict)

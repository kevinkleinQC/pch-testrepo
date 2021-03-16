x = "this is a super super long long long line this is really not cool asdf asdf asdf asdfa asdf asdfa it makes many things overflow"

l = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

d = {'asdf':1,
     'asdf':2}

def function_with_docstring(argument):
    """Integer argument
    """
    if argument % 15 == 0:
        print("FIZZBUZZ")
    elif argument % 5 == 0:
        print("FIZZ")
    elif argument % 3 == 0:
        print("BUZZ")

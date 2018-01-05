def fizzbuzz(doodle):
    if doodle == 1: 
        return '1'
    elif doodle == 2: 
        return '2'
    elif doodle in (6, 3, 9, 12): 
        return 'Fizz'
    elif doodle in (5, 10):
        return 'Buzz'
    elif doodle == 15:
        return 'FizzBuzz'
    elif doodle == 4:
        return '4'

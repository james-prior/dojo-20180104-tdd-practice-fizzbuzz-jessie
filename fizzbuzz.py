def fizzbuzz(doodle):
    if doodle == 1: 
        return '1'
    elif doodle == 2: 
        return '2'
    elif doodle % 3 == 0 and doodle % 5 == 0:
        return 'FizzBuzz'
    elif doodle % 5 == 0:
        return 'Buzz'
    elif doodle % 3 == 0: 
        return 'Fizz'
    return str(doodle)

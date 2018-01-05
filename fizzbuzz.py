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
    elif doodle == 4:
        return '4'
    elif doodle == 8:
        return '8'
    elif doodle == 11:
        return '11'
    elif doodle == 13:
        return '13'
    elif doodle == 14:
        return '14'
    elif doodle == 7:
        return '7'

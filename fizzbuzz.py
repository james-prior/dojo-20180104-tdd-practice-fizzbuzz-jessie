def fizzbuzz(doodle):
    output = ''
    if doodle % 3 == 0:
        output += 'Fizz'
    if doodle % 5 == 0:
        output += 'Buzz'
    if not output:
        output = str(doodle)
    return output

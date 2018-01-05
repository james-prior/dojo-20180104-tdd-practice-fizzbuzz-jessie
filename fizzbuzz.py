def fizzbuzz(doodle):
    words = ''
    if doodle % 3 == 0:
        words += 'Fizz'
    if doodle % 5 == 0:
        words += 'Buzz'
    if not words:
        words = str(doodle)
    return words

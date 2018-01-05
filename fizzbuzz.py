def fizzbuzz(input_number):
    words = ''
    if input_number % 3 == 0:
        words += 'Fizz'
    if input_number % 5 == 0:
        words += 'Buzz'
    if not words:
        words = str(input_number)
    return words

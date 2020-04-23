# URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.


def urlify(s, num_char):
    new_string = '' # answer
    for i in range(num_char):
        if s[i] == ' ':
            new_string += '%20'
        elif s[i] != ' ':
            new_string += s[i]
    return new_string


if __name__ == "__main__":

    # s, num_char = input().split(',')

    s = "Mr John Smith      "
    num_char = 13

    if len(s) <= 1:
        print(s)

    else:
        # If the chars argument is not provided, all whitespaces on the right are removed from the string
        #s.rstrip(' ')
        print(urlify(s, num_char))

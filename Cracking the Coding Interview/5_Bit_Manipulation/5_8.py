# Draw Line: A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in one byte.
# The screen has width w, where w is divisible by 8 (that is, no byte will be split across rows).
# The height of the screen, of course, can be derived from the length of the array and the width.
# Implement a function that draws a horizontal line from (xl, y) to ( x2, y)
# The method signature should look something like:
# drawLine(byte[] screen, int width, int xl, int x2, int y)


def drawLine(screen, width, x1, x2, y):
    # bit numbers
    x_start = y * width + x1
    x_end = y * width + x2
    # indexes
    ind_start = x_start // 8
    ind_end = x_end // 8

    for i in range(ind_start + 1, ind_end):
        screen[i] = 0xff       # 0xff = 11111111 (binary representation)

    start_mask = 0xff >> (x1 % 8)
    screen[ind_start] |= start_mask

    end_mask = 0xff >> ((x2 % 8) + 1)
    if screen[ind_end]:
        screen[ind_end] -= end_mask
    else:
        screen[ind_end] = 0xff - end_mask


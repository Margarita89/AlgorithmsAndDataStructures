# Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
# fill in the surrounding area until the color changes from the original color.


def paint_fill(screen, init_color, color, pc, pr):
    if pc >= len(screen[0]) or pc < 0 or pr >= len(screen) or pr < 0:
        return
    # if not already painted in other color or our color
    if screen[pr][pc] == init_color and screen[pr][pc] != color:
        screen[pr][pc] = color
        paint_fill(screen, init_color, color, pc-1, pr)
        paint_fill(screen, init_color, color, pc+1, pr)
        paint_fill(screen, init_color, color, pc, pr-1)
        paint_fill(screen, init_color, color, pc, pr+1)
    return screen


if __name__ == "__main__":
    size_r = 3
    size_c = 4
    # initial screen with 0 color
    screen = [[0 for _ in range(size_c)] for _ in range(size_r)]
    # insert points of another color
    screen[0][1] = 1
    screen[0][2] = 1
    screen[0][3] = 1
    screen[1][2] = 1
    screen[2][1] = 1
    screen[2][2] = 1
    # choose color and starting point to paint screen
    color = 2
    r, c = 1, 2
    init_color = screen[r][c]
    print('Screen to paint: ', screen)
    print('Painted screen: ', paint_fill(screen, init_color, color, r, c))

    screen = [[0 for _ in range(size_c)] for _ in range(size_r)]
    # insert points of another color
    screen[0][1] = 1
    screen[0][2] = 1
    screen[0][3] = 1
    screen[1][2] = 1
    screen[2][1] = 1
    screen[2][2] = 1
    r, c = 0, 0
    init_color = screen[r][c]
    print('Screen to paint: ', screen)
    print('Painted screen: ', paint_fill(screen, init_color, color, c, r))


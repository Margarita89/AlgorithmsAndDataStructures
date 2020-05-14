# Stack of Boxes: You have a stack of n boxes, with widths w1, heights hi, and depths di.
# The boxes cannot be rotated and can only be stacked on top of one another
# if each box in the stack is strictly larger than the box above it in width, height, and depth.
# Implement a method to compute the height of the tallest possible stack.
# The height of a stack is the sum of the heights of each box.


# compares last boxes in stack and ith box
def compare_boxes(boxes_dims, stack, index):
    if not stack:
        return True
    last_box = stack[-1]
    if last_box[1] < boxes_dims[index][1] or last_box[2] < boxes_dims[index][2]:
        return False
    return True


# recursively find max stack length of boxes with descending dimensions
def stack_of_boxes(boxes_dims, stack, last_num):
    max_cur_height = 0
    for i in range(last_num, len(boxes_dims)):
        if compare_boxes(boxes_dims, stack, i):
            stack.append(boxes_dims[i])     # add to stack
            height = stack_of_boxes(boxes_dims, stack, i+1)
            max_cur_height = max(max_cur_height, height + boxes_dims[i][0])
            stack.pop()
    return max_cur_height


def tower_boxes(boxes_dims):
    if len(boxes_dims) == 1:
        return boxes_dims[0][0]
    stack = []      # current stack of boxes
    last_num = 0    # last number in boxes_dimensions added
    return stack_of_boxes(boxes_dims, stack, last_num)


if __name__ == "__main__":
    num_boxes = 3
    # height, width, depth
    boxes_dimensions = [[] for _ in range(num_boxes)]
    const = 0
    for i in range(num_boxes):
        for j in range(3):
            boxes_dimensions[i].append(const)
            const += 1
    boxes_dimensions.sort(key=lambda x: x[0], reverse=True)

    boxes_dimensions[2][0] = 1
    boxes_dimensions[2][1] = 5

    print('Boxes dimensions:', boxes_dimensions)
    print('The height of the tallest possible stack:', tower_boxes(boxes_dimensions))

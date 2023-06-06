def rectangle_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    overlapped_area = 0

    # area1 = (abs(ax1) + abs(ax2)) * (abs(ay1) + abs(ay2))
    # area2 = (abs(bx1) + abs(bx2)) * (abs(by1) + abs(by2))
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    max_left = max(ax1, bx1)
    min_right = min(ax2, bx2)
    width = min_right - max_left

    max_up = max(ay1, by1)
    min_down = min(ay2, by2)
    height = min_down - max_up

    if width > 0 and height > 0:
        overlapped_area = height * width

    total_area = (area1 + area2) - overlapped_area

    return total_area


ax1 = -2
ay1 = -2
ax2 = 2
ay2 = 2
bx1 = 3
by1 = 3
bx2 = 4
by2 = 4
totall_area = rectangle_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
print("Total area:", totall_area)

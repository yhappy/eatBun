import cv2
import numpy as np
import pytesseract
from rectangle_finder import find_rectangle_with_sum

image = cv2.imread('1.jpg')


# 指定裁剪区域的坐标和尺寸
x, y, width, height = 30, 460, 1020, 1600  # 根据需要调整这些值
# 划分图像成16行10列
rows, cols = 16, 10

# 裁剪图像
cropped_image = image[y:y+height, x:x+width]

# 二值化
gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

# 指定一个适当的阈值，使较暗的部分变为白色，而较亮的部分变为黑色
threshold_value = 100  # 根据需要调整阈值
_, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)


cv2.imwrite('dark_areas_image.png', binary)

row_height, col_width = height // rows, width // cols

# 识别数字并填充到二维数组
two_dimensional_array = []

for row in range(rows):
    row_numbers = []
    for col in range(cols):
        x = col * col_width
        y = row * row_height
        roi = binary[y:y + row_height, x:x + col_width]
        custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
        text = pytesseract.image_to_string(roi, config=custom_config)
        number = int(text.strip()) if text.strip() else 0
        row_numbers.append(number)
    two_dimensional_array.append(row_numbers)

# 打印二维数组
for row in two_dimensional_array:
    print(row)


target_sum = 10
matrix = two_dimensional_array

while True:
    result = find_rectangle_with_sum(matrix, 10)

    if result:
        row1, col1, row2, col2 = result
        print(f"第{row1 + 1}行,第{col1 + 1}个 - 第{row2 + 1}行,第{col2 + 1}个")
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                print(matrix[r][c], end=' ')
                matrix[r][c] = 0  # 将长方形内的数字设置为0
            print()
    else:
        print("No more rectangles with sum 10 found.")
        # 打印二维数组
        for row in matrix:
          print(row)
        break
    
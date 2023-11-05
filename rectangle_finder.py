def find_rectangle_with_sum(matrix, target_sum):
    rows, cols = len(matrix), len(matrix[0])

    for r1 in range(rows):
        for r2 in range(r1 + 1, rows + 1):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols + 1):
                    current_sum = 0
                    for r in range(r1, r2):
                        for c in range(c1, c2):
                            current_sum += matrix[r][c]

                    if current_sum == target_sum:
                      return (r1, c1, r2 - 1, c2 - 1)

    return None
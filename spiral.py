class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # Get matrix dimensions

        num_rows, num_cols = len(matrix), len(matrix[0])

      

        # Direction vectors: right(0,1), down(1,0), left(0,-1), up(-1,0)

        # Stored as (dx1, dy1, dx2, dy2, dx3, dy3, dx4, dy4) in compressed form

        directions = (0, 1, 0, -1, 0)

      

        # Track visited cells to know when to turn

        visited = [[False] * num_cols for _ in range(num_rows)]

      

        # Initialize position (row, col) and direction index

        row = col = direction_idx = 0

        result = []

      

        # Traverse all cells in the matrix

        for _ in range(num_rows * num_cols):

            # Add current cell value to result

            result.append(matrix[row][col])

            visited[row][col] = True

          

            # Calculate next position based on current direction

            next_row = row + directions[direction_idx]

            next_col = col + directions[direction_idx + 1]

          

            # Check if we need to change direction (hit boundary or visited cell)

            if (next_row < 0 or next_row >= num_rows or 

                next_col < 0 or next_col >= num_cols or 

                visited[next_row][next_col]):

                # Turn clockwise (right -> down -> left -> up -> right)

                direction_idx = (direction_idx + 1) % 4

          

            # Move to next position using current (possibly updated) direction

            row += directions[direction_idx]

            col += directions[direction_idx + 1]

      

        return result


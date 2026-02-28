class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        """
        Determines if four given points form a valid square.
        A valid square has four equal sides and four right angles.
      
        Args:
            p1, p2, p3, p4: Four points represented as [x, y] coordinates
          
        Returns:
            True if the four points form a valid square, False otherwise
        """
      
        def is_right_isosceles_triangle(point_a: List[int], point_b: List[int], point_c: List[int]) -> bool:
            """
            Checks if three points form a right isosceles triangle.
            This occurs when two sides have equal length and the third side
            satisfies the Pythagorean theorem.
          
            Args:
                point_a, point_b, point_c: Three points as [x, y] coordinates
              
            Returns:
                True if points form a right isosceles triangle with non-zero sides
            """
            # Extract coordinates for readability
            x1, y1 = point_a[0], point_a[1]
            x2, y2 = point_b[0], point_b[1]
            x3, y3 = point_c[0], point_c[1]
          
            # Calculate squared distances between each pair of points
            # Using squared distances to avoid floating point operations
            dist_squared_ab = (x1 - x2) ** 2 + (y1 - y2) ** 2
            dist_squared_ac = (x1 - x3) ** 2 + (y1 - y3) ** 2
            dist_squared_bc = (x2 - x3) ** 2 + (y2 - y3) ** 2
          
            # Check if any configuration forms a right isosceles triangle:
            # Two sides must be equal (isosceles) and satisfy Pythagorean theorem (right angle)
            # Also ensure sides have non-zero length (last condition in each case)
            return any([
                # Case 1: AB == AC, and AB² + AC² == BC² (right angle at A)
                dist_squared_ab == dist_squared_ac and 
                dist_squared_ab + dist_squared_ac == dist_squared_bc and 
                dist_squared_ab > 0,
              
                # Case 2: AC == BC, and AC² + BC² == AB² (right angle at C)
                dist_squared_ac == dist_squared_bc and 
                dist_squared_ac + dist_squared_bc == dist_squared_ab and 
                dist_squared_ac > 0,
              
                # Case 3: AB == BC, and AB² + BC² == AC² (right angle at B)
                dist_squared_ab == dist_squared_bc and 
                dist_squared_ab + dist_squared_bc == dist_squared_ac and 
                dist_squared_ab > 0,
            ])
      
        # For four points to form a square, every combination of three points
        # must form a right isosceles triangle (the fourth point being the opposite corner)
        return (
            is_right_isosceles_triangle(p1, p2, p3) and
            is_right_isosceles_triangle(p2, p3, p4) and
            is_right_isosceles_triangle(p1, p3, p4) and
            is_right_isosceles_triangle(p1, p2, p4)
        )
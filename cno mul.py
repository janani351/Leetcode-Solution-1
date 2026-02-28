class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """
        Multiply two complex numbers given as strings in the format "a+bi".
      
        Complex number multiplication formula: (a1 + b1i) * (a2 + b2i) = (a1*a2 - b1*b2) + (a1*b2 + a2*b1)i
      
        Args:
            num1: First complex number as string (e.g., "1+2i")
            num2: Second complex number as string (e.g., "3+4i")
      
        Returns:
            Product of the two complex numbers as string in format "a+bi"
        """
        # Parse the real and imaginary parts from the first complex number
        # Remove the trailing 'i' and split by '+' to get both parts
        real_part_1, imaginary_part_1 = map(int, num1[:-1].split("+"))
      
        # Parse the real and imaginary parts from the second complex number
        real_part_2, imaginary_part_2 = map(int, num2[:-1].split("+"))
      
        # Calculate the real part of the product: a1*a2 - b1*b2
        result_real = real_part_1 * real_part_2 - imaginary_part_1 * imaginary_part_2
      
        # Calculate the imaginary part of the product: a1*b2 + a2*b1
        result_imaginary = real_part_1 * imaginary_part_2 + real_part_2 * imaginary_part_1
      
        # Format and return the result as "a+bi"
        return f"{result_real}+{result_imaginary}i"

from typing import List, Union


class NumberRangesSolution:
    """
    A class to process a sorted array of integers and return ranges of consecutive numbers.
    
    This class takes a sorted array of integers and returns a list of strings representing
    ranges of consecutive numbers. For example, [1,2,3,4,6,7,9,10] would return
    ["1->4", "6->7", "9->10"].
    
    Attributes:
        result (List[str]): The processed ranges as a list of strings.
    """

    def __init__(self, array: List[int]) -> None:
        """
        Initialize the NumberRangesSolution with the input array.

        Args:
            array (List[int]): A sorted list of integers to process.
        """
        self.result: List[str] = self.process(array)

    def __call__(self) -> List[str]:
        """
        Return the processed ranges when the class instance is called.

        Returns:
            List[str]: The list of range strings.
        """
        return self.result
    
    def process(self, array: List[int]) -> List[str]:
        """
        Process the input array and return ranges of consecutive numbers.

        Args:
            array (List[int]): A sorted list of integers to process.

        Returns:
            List[str]: A list of strings representing ranges of consecutive numbers.
                      Single numbers are represented as "n", ranges as "n->m".
        """
        # Handle empty arrays
        if not array:
            return []
        
        # Handle single element array
        if len(array) == 1:
            return [str(array[0])]
        
        # Initialize variables
        start: int = 0
        res: List[int] = [0, 1]
        output: List[str] = []

        for j in range(1, len(array)):
            if abs(array[j] - array[j-1]) in res:
                continue

            if start == j-1:
                output.append(str(array[start]))
            else:
                output.append(f"{array[start]}->{array[j-1]}")

            # Update start
            start = j

        # Handle remaining cases
        if start == j:
            output.append(str(array[start]))
        elif start == 0:
            output.append(f"{array[0]}->{array[-1]}")
        else:
            output.append(f"{array[start]}->{array[j]}")

        return output


def main() -> None:
    """Run the main program with a sample array."""
    array: List[int] = [1, 2, 3, 4, 6, 7, 9, 10]
    result: NumberRangesSolution = NumberRangesSolution(array)
    print(result())


if __name__ == "__main__":
    main()

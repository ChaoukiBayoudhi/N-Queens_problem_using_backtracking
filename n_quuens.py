class NQueensBacktracking:
    def __init__(self,n_queens=4) -> None:
        self.n=n_queens
        self.result=list()
    
    def isSafe(self,possible_solution:list[int])->bool:
        row=len(possible_solution)-1
        col=possible_solution[-1]
        #or
        #col=possible_solution[row]
        i=0
        safe=True
        while i<row and safe:
            diff=abs(possible_solution[i]-col)
            if diff==0 or diff==abs(row-i):
                safe=False
            i+=1
        return safe
    def isSafe_v2(self, possible_solution: list[int]) -> bool:
            # Get the position of the last placed queen
            row = possible_solution[-1]  # Row of candidate queen
            col = len(possible_solution) - 1  # Column of candidate queen

            # Check with all previously placed queens
            for i in range(col):
                prev_row = possible_solution[i]

                # 1. Same diagonal (top-left to bottom-right)
                if row - prev_row == col - i:
                    return False

                # 2. Same diagonal (top-right to bottom-left)
                if row - prev_row == -(col - i):
                    return False
            return True
        #this version of isSafe uses list comprehension and any() function
        #it uses the enumerate() function to get the index of the previous queen
        def isSafe_v3(self, possible_solution: list[int]) -> bool:
            # Get candidate queen position (last in list)
            candidate_queen_col = len(possible_solution) - 1
            candidate_queen_row = possible_solution[candidate_queen_col]

            # Check all previous queens using list comprehension and any()
            # The any() function returns True if at least one element of an iterable is true.
            # Here, we use it to check if any of the previous queens
            # are in the same row or diagonal as the candidate queen.
            # The enumerate() function adds a counter to an iterable and returns it
            # in a form of enumerate object.
            # It allows us to loop over a list and have an automatic counter/index with it.
            safe = not any(
                prev_row == candidate_queen_row or                     # Check if the previous queen is in the same row
                abs(prev_row - candidate_queen_row) == abs(i - candidate_queen_col)  # Check if the previous queen is in the same diagonal
                for i, prev_row in enumerate(possible_solution[:-1])  # Iterate over the previous queens with their indices,
            )

            return safe

        def isSafe_v4(self, possible_solution: list[int]) -> bool:
            # Check if the last placed queen is in the same column as any previous queen
            same_column = possible_solution[-1] in possible_solution[:-1]

            # Calculate the absolute differences between the last placed queen's column and all previous queens' columns
            # This is to check for diagonal attacks. If all differences are unique, it means no diagonal attack.
            # Convert the differences to a set to remove duplicates and compare the length with the number of previous queens.
            # If the lengths are equal, it means all differences are unique, hence no diagonal attack.
            diagonal_attack = len(set(abs(possible_solution[-1] - prev_column) for prev_column in possible_solution[:-1])) != len(possible_solution) - 1

            # Return True if there's no same column or diagonal attack, otherwise return False
            return not (same_column or diagonal_attack)



    def solve(self, possible_solution:list[int])->None:
        if len(possible_solution)==self.n:
            self.result.append(possible_solution[:])
        else:
            for i in range(self.n):
                possible_solution.append(i)
                if self.isSafe(possible_solution):
                    self.solve(possible_solution)
                possible_solution.pop()
    def print_board(self)
#Test
if __name__ == "__main__":
    n=int(input('Enter an integer'))
    nqb=NQueensBacktracking(n)
    nqb.solve(list())
    print(f'There is {len(nqb.result)} possible solutions.')
    print('List of possible solutions :')
    print(nqb.result)
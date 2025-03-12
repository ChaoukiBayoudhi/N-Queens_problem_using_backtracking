class NQueensBacktracking:
    def __init__(self,n_queens=4) -> None:
        self.n=n_queens
        self.result=list()
    
    def isSafe(self,possible_solution:list[int])->bool:
        pass
    def solve(self, possible_solution:list[int])->None:
        if len(possible_solution)==self.n:
            self.result.append(possible_solution[:])
        else:
            for i in range(self.n):
                possible_solution.append(i)
                if self.isSafe(possible_solution):
                    self.solve(possible_solution)
                possible_solution.pop()
#Test
n=int(input('Enter an integer'))
nqb=NQueensBacktracking(n)
nqb.solve(list())
print(f'There is {len(nqb.result)} possible solutions.')
print('List of possible solutions :')
print(nqb.result)
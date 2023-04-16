import sys


class Dijkstra():

    # Node initialize
    def __init__(self, V, Array, SRC):
        self.v = V
        self.array = Array
        self.src = SRC # Starting Node 지정

    def printSolution(self, Weight):
        for node in range(self.v):
            print(Weight[node]) # 나중에 node로 변경

    def calculate(self, Found, Weight):
        min = float('INF')
        min_index = -1
        for i in range(self.v):
            if (Found[i] == False) and (Weight[i] < min):
                min = Weight[i]
                min_index = i

        return min_index

    # Starting Root Node => 0번 노드
    def dijkstra(self):
        # Array 선언
        Found = [float('INF') for i in range(5)]
        Weight = [float('INF') for i in range(5)]

        # Array initialize
        Found[self.src] = True
        Weight[self.src] = 0

        for j in range(self.v):
            Found[j] = False
            Weight[j] = self.array[self.src][j]

        # Greedy Algorithm
        for i in range(self.v):
            x = self.calculate(Found, Weight) # 현재 가장 최소의 Weight을 가지는 노드의 Array index 반환
            Found[x] = True
            for j in range(self.v):
                if (Weight[x] + self.array[x][j] < Weight[j]):
                    Weight[j] = Weight[x] + self.array[x][j]

        self.printSolution(Weight)


# main function
if __name__ == "__main__":
    # Array 5x5 Size
    Array = [[0, 2, 3, float('INF'), float('INF')],
             [float('INF'), 0, 4, 5, float('INF')],
             [float('INF'), float('INF'), 0, 6, float('INF')],
             [float('INF'), float('INF'), float('INF'), 0, float('INF')],
             [1, float('INF'), float('INF'), float('INF'), 0]]

    V, E = map(int, sys.stdin.readline().split())
    src = int(input())
    edge_list = [list(map(int, input().split())) for num in range(E)] # input Edge Information
    test_array = [[float('INF') for j in range(V)] for i in range(V)]

    for idx in range(V):
        test_array[idx-1][idx-1] = 0
    for value in edge_list:
        test_array[value[0]-1][value[1]-1] = value[2]

    d = Dijkstra(V, test_array, src-1)
    d.dijkstra()



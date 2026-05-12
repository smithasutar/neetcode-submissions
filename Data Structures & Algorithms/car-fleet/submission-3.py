class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        array = []
        count = 0
        cars = sorted(zip(position, speed), reverse=True)
        print(cars)
        for i in range(len(cars)):
            y = target-cars[i][0]
            x = y/cars[i][1]
            array.append(x)
        max_time = 0
        for i in range(len(array)):
            if array[i] > max_time:
                count+=1
                max_time = array[i]


        return count
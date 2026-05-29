"""
U: 
    input: "n" cars, 2 int arrays "position" and "speed" (both len = n)
        position[i] = starting mile of ith car
        speed[i] = speed of ith car in miles/hr

        a car cannot pass another car but it can catch up and tra
    output: return the # of car fleets that will arrive at the desitination 

    traveling to reach the mile target

M: use a list of pairs, first val = position, second val = speed 
   
P:  sort it with postion (decreasing order)
    calulate the time taken to reach the target, time taken = (target - position) / speed
    store the result in a list 
    iterate the list 
    hold the max_time 
    if the val is <= max_time = the same car fleet 
    if the val is > max_time = new car fleet, update the max_time 
"""

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        pairs.sort(key=lambda pair : pair[0], reverse=True)

        time_takens = []

        for pair in pairs: 
            time_takens.append( (target-pair[0]) / float(pair[1]))

        max_time = 0
        car_fleet = 0

        for time_taken in time_takens: 
            if time_taken <= max_time: 
                continue
            else:
                car_fleet += 1 
                max_time = time_taken

        return car_fleet
        
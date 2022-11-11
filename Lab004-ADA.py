def knapSack(maxCapacity, sortedWeights, sortedValues):
    max_profit = 0
    size = len(sortedWeights)

    if size == 0:
        return max_profit
    
    for i in range(0, size):
        # Exit condition
        if(maxCapacity == 0):
            break

        if(sortedWeights[i] <= maxCapacity):
            max_profit += sortedValues[i]
            maxCapacity -= sortedWeights[i]

    return max_profit

val = [120, 100, 60, 80, 40, 20, 5]
wt = [55, 42, 38, 31, 30, 20, 10]
maxCapacity = 90
print (knapSack(maxCapacity, wt, val))

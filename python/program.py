'''
1,2000,5,1;1,2030,15,2;1,2000,10,1:2,2050,15,5;1,2067,8,6;2,2050,5,7
1: 2000.0 1: 2022.5 2: 2050.0 1: 2035.21 2: 2050.0
'''

# input and seperate trades using semi-colon
trades = input().split(";")
# store prev weighted averages for all keys
weightedAvg = {}
# store prev sequence number
prevS = 0

for val in trades:
    # seperate all values from a trade
    trade = val.split(",")
    key = int(trade[0])
    value = int(trade[1])
    quantity = int(trade[2])
    sequence = int(trade[3])
    # avoid if current # is less than prev #
    if sequence < prevS:
        continue
    prevS = sequence
    if key in weightedAvg:
        # use previous weighted avg and total quantity
        prevM = weightedAvg[key][0]
        prevQ = weightedAvg[key][1]
    else:
        prevM=0
        prevQ=0
    # calculate weighted average
    avg = ((prevM*prevQ) + (value*quantity)) / (prevQ + quantity)
    avg = round(avg, 2)
    # store weighted average and total quantity for key
    weightedAvg[key] = [avg,prevQ + quantity]
    print(key, end="")
    print(":", avg, end = " ")


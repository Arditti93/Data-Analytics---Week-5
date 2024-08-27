dataset = [34,67,5,81,2,45,9,23,55,41,42,84,109, 109, 109]

def find_mean(data):
    # sum() method adds up all the values and returns the result
    total = sum(data)
    # finds the length of the data set
    count = len(data)
    mean = total / count
    return mean
    
print("The mean of the dataset is:", find_mean(dataset))






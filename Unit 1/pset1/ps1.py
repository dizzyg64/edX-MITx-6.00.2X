###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    def solveTripsByWeight():
        """solve problem with just int values from cow weights"""
        
        #sorted list of cow weights
        cowWeight = sorted(cows.values())
        cowWeight.reverse()

        #copy list to avoid side effects
        copyWeight = cowWeight[:]
        results = []

        #overall loop to hold all the trips
        while len(copyWeight) > 0:

            #variable resets after each trip
            trip = []
            weight = 0
            cowWeight = copyWeight[:]

            #inner loop for each trip
            for i in range(len(cowWeight)):
                if weight + cowWeight[i] <= limit:
                    weight += cowWeight[i]
                    trip.append(cowWeight[i])
                    copyWeight.remove(cowWeight[i])
                    
            #final results         
            results.append(trip)
            
        return results

    def findValue(dic, val):
        """Used this code from StackOverflow to search dict value"""
        return [k for k, v in iter(dic.items()) if v == val][0]

    def replaceNumWithName():
        """replaces float with dictionary cow name"""
        
        results = solveTripsByWeight()

        #create a dict copy to remove cows that already went on trip
        cows2 = cows.copy()
        while len(cows2) > 0:
            for i in range(len(results)):
                for j in range(len(results[i])):
                    #since cow name doesn't matter
                    #just search dictionary for correct weight
                    #replace weight with first found cow name
                    #delete that cow
                    replace = findValue(cows2, results[i][j])
                    cows2.pop(replace)
                    results[i][j] = replace

        return results

    return replaceNumWithName()


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    def addCowWeight(list, cows):
        #adds a list of cows, with value coming from dict
        sum = 0.0
        for key in list:
            sum += cows[key]
        return sum
    #list of cows
    cowName = (cows.keys())
    #cowName = ['Maggie', 'Lola', 'Oreo'] list to store all partitions and useful ones
    allPart = []
    usePart = []    
    for part in get_partitions(cowName):
        allPart.append(part)
    #make a test that checks each trip list if their sum <= limit adds each partition that passes all tests to usePart
    for part in allPart:
        test = []
        for trip in part:
            if addCowWeight(trip, cows) <= limit:
                test.append(trip)    
        if len(test) == len(part):
            usePart.append(part)

    #find all the lengths of each option, and search for smallest
    lenIndex = []
    for part in usePart:
        lenIndex.append(len(part))    
    find = min(lenIndex)
    for part in usePart:
        if len(part) == find:
            return part

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))



import random
import math
import time

# Function to calculate the distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Function to calculate the total cost of a tour
def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    total_cost += calculate_distance(cities[tour[-1]], cities[tour[0]])  # Return to the starting city
    return total_cost

# Randomized Hill Climbing Algorithm
def randomized_hill_climbing(no_cities, cost_func, MEB, seed):
    random.seed(seed)  # Seed for reproducibility
    current_tour = list(range(no_cities))  # Initial tour as a list of city indices
    random.shuffle(current_tour)  # Randomly shuffle the initial tour

    current_cost = cost_func(current_tour)  # Calculate the cost of the initial tour
    num_evaluations = 0  # Counter for the number of evaluations

    while num_evaluations < MEB:
        neighbor_tour = current_tour.copy()
        i, j = random.sample(range(no_cities), 2)  # Randomly select two distinct cities
        neighbor_tour[i], neighbor_tour[j] = neighbor_tour[j], neighbor_tour[i]  # Swap cities

        neighbor_cost = cost_func(neighbor_tour)  # Calculate the cost of the neighbor tour
        num_evaluations += 1

        if neighbor_cost < current_cost:
            current_tour = neighbor_tour
            current_cost = neighbor_cost

    return current_tour, current_cost, num_evaluations

# Simulated Annealing Algorithm
def simulated_annealing(no_cities, cost_func, MEB, seed):
    random.seed(seed)  # Seed for reproducibility
    current_tour = list(range(no_cities))  # Initial tour as a list of city indices
    random.shuffle(current_tour)  # Randomly shuffle the initial tour

    current_cost = cost_func(current_tour)  # Calculate the cost of the initial tour
    num_evaluations = 0  # Counter for the number of evaluations

    temperature = 1000.0  # Initial temperature
    cooling_rate = 0.995  # Cooling rate

    while temperature > 1 and num_evaluations < MEB:
        i, j = random.sample(range(no_cities), 2)  # Randomly select two distinct cities
        neighbor_tour = current_tour.copy()
        neighbor_tour[i], neighbor_tour[j] = neighbor_tour[j], neighbor_tour[i]  # Swap cities

        neighbor_cost = cost_func(neighbor_tour)  # Calculate the cost of the neighbor tour
        num_evaluations += 1

        cost_difference = neighbor_cost - current_cost

        if cost_difference < 0 or random.random() < math.exp(-cost_difference / temperature):
            current_tour = neighbor_tour
            current_cost = neighbor_cost

        temperature *= cooling_rate  # Decrease the temperature

    return current_tour, current_cost, num_evaluations

# Main program
keeprunning = True  # Initialize a variable to control program execution

while keeprunning:
    start_time = time.time()  # Start measuring execution time

    no_cities = int(input("Enter the number of cities: "))
    cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(no_cities)]  # Generate random cities

    # Define the cost function for the TSP
    def cost_func(tour):
        return calculate_total_cost(tour, cities)

    MEB = int(input("Enter the maximum number of evaluations: "))
    seed1 = int(input("Enter a seed for random number generation: "))

    search_strat = int(input("Choose a search strategy (1 for Randomized Hill Climbing, 2 for Simulated Annealing): "))

    if search_strat == 1:
        print("This is the output of randomized hill climbing - Simple Search", file=open("2runs.txt", "a"))
        best_path, best_cost, num_evaluations = randomized_hill_climbing(no_cities, cost_func, MEB, seed1)
    elif search_strat == 2:
        print("This is the output of simulated annealing - Sophisticated Search", file=open("2runs.txt", "a"))
        best_path, best_cost, num_evaluations = simulated_annealing(no_cities, cost_func, MEB, seed1)
    else:
        print("Please enter a valid option either 1 or 2 !!")
        continue  # Go back to the beginning of the loop to get a valid input

    # Print the results
    print("The cost of the best solution:", best_cost)
    print("The path of the best solution:", best_path)
    print("The value of MEB count is:", num_evaluations)
    print("********** %s seconds *********" % (time.time() - start_time))

    # Append the results to the file
    with open("2runs.txt", "a") as file:
        print("The cost of the best solution:", best_cost, file=file)
        print("The path of the best solution:", best_path, file=file)
        print("Value of MEB count is:", num_evaluations, file=file)
        print("********** %s seconds *********" % (time.time() - start_time), file=file)

    stop = input("Do you want to run this program again? (yes or no): ")
    if stop.lower() == "no":
        keeprunning = False  # Exit the loop if the user enters 'no'


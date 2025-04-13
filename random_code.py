import random
import time

def generate_random_number(min_val=1, max_val=100):
    """Generate a random number between min_val and max_val."""
    return random.randint(min_val, max_val)

def generate_random_list(length=10, min_val=1, max_val=100):
    """Generate a list of random numbers."""
    return [random.randint(min_val, max_val) for _ in range(length)]

def random_choice(items):
    """Choose a random item from a list."""
    return random.choice(items)

def shuffle_list(items):
    """Shuffle a list in place."""
    random.shuffle(items)
    return items

def main():
    print("Welcome to the Random Generator!")
    print(f"Current time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Random number between 1 and 100: {generate_random_number()}")
    
    random_list = generate_random_list()
    print(f"Random list: {random_list}")
    print(f"Random choice from list: {random_choice(random_list)}")
    
    shuffled = shuffle_list(random_list.copy())
    print(f"Shuffled list: {shuffled}")

if __name__ == "__main__":
    main()

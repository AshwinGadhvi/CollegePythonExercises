#Write a python program to calculate simple interest.
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

if __name__ == "__main__":
    principal = float(input())
    rate = float(input())
    time = float(input())

    simple_interest = calculate_simple_interest(principal, rate, time)
    print(simple_interest)

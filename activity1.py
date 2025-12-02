def voter_eligibility():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))

    if age >= 18:
        print(f"{name}, you are eligible to vote.")
    else:
        print(f"{name}, you are not eligible to vote yet.")

    print(f"Printing your name times:")
    for i in range(1):
        print(name)

voter_eligibility()

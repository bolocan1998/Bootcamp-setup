def sum_of_weight(char_weight, inv_weight):
    return char_weight + inv_weight

def avg_of_weight(char_weight, inv_weight):
    total = sum_of_weight(char_weight, inv_weight)
    return total/2

def run():
    char_weight = float(input("Enter your character weight: "))
    inv_weight = float(input("Enter your inversion weight: "))
    calculation_type=input("What you would like to calculate(sum or weight?): )")

    if calculation_type.lower()=="sum":
        result = sum_of_weight(char_weight, inv_weight)
        print(f" The sum of the weight is {result}")

    elif calculation_type.lower()=="avg":
        result = avg_of_weight(char_weight, inv_weight)
        print(f" The average of the weight is {result}")
    else:
        print("Please enter a valid option")
run()
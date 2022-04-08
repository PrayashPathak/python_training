# def compute_factors(number):
#     factors = []
#     while number % 2 == 0:
#         factors.append(2)
#         number //= 2
#     for i in range(3, number, 2):
#         factors.append(i)
#         number //= i
#     return factors


# def compute_lcm(factors1, factors2):
#     max_factor = 1
#     for fac1 in factors1:
#         for fac2 in factors2:
#             if fac1 == fac2:
#                 if max_factor < fac1:
#                     max_factor = fac1
#             else:
#                 max_factor = fac1 * fac2

#     return max_factor


# print("Please enter two numbers to compute their LCM.")
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter second number: "))

# factors_of_num1 = compute_factors(num1)
# factors_of_num2 = compute_factors(num2)

# print(factors_of_num1)
# print(factors_of_num2)

# lcm = compute_lcm(factors_of_num1, factors_of_num2)
# print(lcm)


def get_prime_number(num):
    factors = []
    i = 2

    while num % 2 == 0:
        factors.append(2)
        num //= 2
    for i in range(3, num+1, 2):
        if num % i == 0:
            factors.append(i)
            num //= i
    print(factors)
    # print(num)
    return factors


num1 = int(input("Enter a number: "))
fact_of_num1 = get_prime_number(num1)
num2 = int(input("Enter second number: "))
fact_of_num2 = get_prime_number(num2)

large = fact_of_num1
small = fact_of_num2

if len(large) < len(small):
    large = fact_of_num2
    small = fact_of_num1

lcm = []
for i in small:
    lcm.append(i)
    if i in large:
        large.remove(i)
lcm += large
print(lcm)
prod = 1
for i in lcm:
    prod *= i
print(prod)

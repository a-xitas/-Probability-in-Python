## 1. The Rule of Product ##

n_outcomes = 6**2

p_six_six = 1/n_outcomes

p_not_five_five = 1-p_six_six

## 2. Extended Rule of Product ##

total_outcomes = 6*6*6*52

p_666_ace_diamonds = 1/total_outcomes

p_no_666_ace_diamonds = 1-p_666_ace_diamonds

## 3. Example Walkthrough ##

p_crack_4 = 1/(10**4)

p_crack_6 = 1/(10**6)

## 4. Permutations ##

import numpy as np



def factorial(permu):
    permutations = []
    
    for n in np.arange(1,permu+1):
              permutations.append(n)
    permutations = np.array(permutations, dtype=np.float64)
    return np.prod(permutations)
              

permutations_1 = factorial(6)
              
permutations_2 = factorial(52)


## 5. More About Permutations ##

perm_3_52 = 52*(52-1)*(52-3+1)

perm_4_20 = 20*(20-1)*(20-2)*(20-4+1)

perm_4_27 = 27*(27-1)*(27-2)*(27-4+1)

## 6. Permutations Formulas ##

def permutation(n, k):
    final_product = 1
    denominator = 1
    for i in range(n, 0, -1):
        final_product *= i
    for i in range(n-k, 0, -1):
        denominator *= i
    return final_product / denominator




p_crack_pass = 1/permutation(127,16)

#N = 9
#K = 3
#res = 1

#for i in range(N-K, 0, -1):
 #       res *= i


## 7. Unique Arrangements ##

def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product

def permutation(n, k):
    numerator = factorial(n)
    denominator = factorial(n-k)
    return numerator/denominator


c = permutation(52,5) / factorial(5)

p_aces_7 = 1 / c

c_lottery = permutation(49,6) / factorial(6)

p_big_prize = 1/c_lottery

print(p_big_prize)

## 8. Combinations ##

def combinations(n, k):
    final_product = 1
    denominator = 1
    kay = 1
    for i in range(n, 0, -1):
        final_product *= i
    for i in range(n-k, 0, -1):
        denominator *= i
    for i in range(k, 0, -1):
        kay *= i
    return final_product / (kay*denominator)



c_18 = combinations(34, 18)

p_non_Y = 1-(1/c_18)
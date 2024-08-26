## 1. Sample Space ##

coin_toss_omega = ['HT','TH','HH','TT']

## 2. Probability of Events ##

a = 6**2

p_sum_6 = 5/36

p_lower_15 = 36/36

p_greater_13 = 0

## 3. Certain and Impossible Events ##

p_2_or_4 = (4/36)

# OU
# prob d obter 2 MAIS a prob d obter 4:
p_2_OU_4 = 1/36+3/36

p_12_or_13 = (1/36)

print(p_2_OU_4==p_2_or_4)

## 4. The Addition Rule ##

p_5_or_9 = (4/36) + (4/36)

p_even_or_less_2 = (18/36) + 0

p_4_or_3_multiple = (3/36) + (12/36)

## 5. Venn Diagrams ##

#Probabilidade de obter um nmr par num lançamento d um dado:
p_c = 3/6
#Probabilidade de obter um nmr maior do q 3 num lançamento d um dado:
p_d = 3/6

p_c_d_addition = p_c + p_d

p_c_d_formula = 4/6

print(p_c_d_addition)

print(p_c_d_formula)

## 6. Exceptions to the Addition Rule ##

p_f_or_t = 0.26+0.11-0.03

## 7. Mutually Exclusive Events ##

p_h_and_c = 0.08+0.11-0.17

## 8. Set Notation ##

operation_1 = False
operation_2 = True
operation_3 = False
operation_4 = True
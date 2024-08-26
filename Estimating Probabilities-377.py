## 2. The Empirical Probability ##

p_tail = 1 - (56/100)

p_six = 28/200

p_odd = 102/200

print(p_tail, p_six, p_odd)

## 3. Probability as Relative Frequency ##

p_heads_1 = 1 - (162/300)
percentage_1 = p_heads_1*100

p_heads_2 = 1 - (2450/5000)
percentage_2 = p_heads_2*100

## 4. Repeating an Experiment ##

# INITIAL CODE
from numpy.random import seed, randint

seed(1)

def coin_toss():
    if randint(0,2) == 1:
        return 'HEAD'
    else:
        return 'TAIL'
    
probabilities = []
heads = 0

for n in range(1, 10001):
    outcome = coin_toss()
    if outcome == 'HEAD':
        heads +=1
    current_probability = heads/n
    probabilities.append(current_probability)

print('first 10 digits from all the probabilities: \n', probabilities[:10],
      '\n'
      '\n'
      'last 10 digits from all the probabilities: \n', probabilities[9990:]
     )


## 5. The True Probability Value ##

p_l = 87/200

p_l_and_c = 40/200

p_h = 63/200

p_no = 1-(160/200)

## 6. The Theoretical Probability ##

# Probabilidade teórica de sacar um 5 num lançamento de dado:
p_5 = 1/6
# Probabilidade teórica de sacar cara e coroa em 2 lançamentos da mm moeda:
p_ht = (1/2)**2
# Probabilidade teórica de sacar coroa e coroa em 2 lançamentos da mm moeda:
p_tt = (1/2)**2

## 7. Events vs. Outcomes ##

p_even = 3/6
p_odd_no_3 = 2/6
p_odd_greater_5 = 0/6

## 8. A Biased Die ##

p_blue = 10/100
p_red = 90/100
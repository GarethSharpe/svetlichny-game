Summary: Svetlichny Game

I won't go into the rules but here is a summary of the theoretical outcome's of the game
so that we can interpret the data.

If we average over a large sample (n=100), and the inputs are randomly distributed 
(inputs = {000, 001, 010, 011, 100, 101, 110, 111}), then the probability of winning the 
game using a classical strategy is 6/8 or = 0.75. However, if we look at the quantum strategy,
it provides us with a probability of winning as (2√2 + 4)/8 = 0.8535. This is simply due to 
the fact that the maximal violation of the Svetlichny inequality is 4√2. As you can see from the two
probabilites, the quantum strategy is superior to the classical strategy. But is this true when 
utalizing a real quantum computer?

--------------------
FINAL CLASSICAL RESULTS
--------------------
Rounds: 100
Wins:  70
Losses: 30
P(win): 0.7

The above result is very close to the predicted mean of 0.75. 

--------------------
FINAL SIMULATED RESULTS
--------------------
Rounds: 100
Wins:  84
Losses: 16
P(win): 0.84

The above result is even closer to the predicted mean of 0.85.

--------------------
FINAL COMPUTED RESULTS
--------------------
Rounds: 100
Wins:  77
Losses: 23
P(win): 0.77

The above result shows that a real quantum computer does not perform near as well as its simulated
self. Due to errors, the computed results deviate approx. 8% away form the expected mean (but still
better than the classical strategy).

Now that we know the results, are these results enough to say that the quantum strategy is "statistically"
superior to its classical cousin?  

A one sample t-test of the results derived from the quantum strategy provided
the following output in R:

        One Sample t-test

data:  result[101:200]
t = 18.205, df = 99, p-value < 2.2e-16
alternative hypothesis: true mean is not equal to 0
95 percent confidence interval:
 0.686077 0.853923
sample estimates:
mean of x 
     0.77 
     
Conclusion: We can be 95% certain that that true mean of the computed quantum strategy lies within
(0.69, 0.85) at a p-value < 0.0001.

A proportion table between the computed classical/quantum solution produced
the folloing output in R:

		type
result  class comp
  FALSE    30   23
  TRUE     70   77
  
This talbe was used to perform Fisher's exact test was used to test whether the difference between 
70% and 77% is statisticall significant.
  
		Fisher's Exact Test for Count Data

data:  table(result, type)
p-value = 0.3364
alternative hypothesis: true odds ratio is not equal to 1
95 percent confidence interval:
 0.7276895 2.8468678
sample estimates:
odds ratio 
  1.432171 
  
Conclusion: Given a p-value of 0.3364, there is is little to no evidence to suggest that the proportions
of wins between the classical strategy and the quantum strategy is not equal to 1. As a result, we cannot 
reject the null hypothesis and conclude that there is no significant difference between these proportions. 
  
This table was used to perform a two sided test for equality of proportions provided the folloing output in R:

        2-sample test for equality of proportions with continuity correction

data:  table(result, type)
X-squared = 0.92414, df = 1, p-value = 0.3364
alternative hypothesis: two.sided
95 percent confidence interval:
 -0.07894409  0.25863861
sample estimates:
   prop 1    prop 2 
0.5660377 0.4761905 

Conclusion: We can be 95% certain that the true difference between the classical proportion of won games and
the computed quantum proportions of won games is between -7.9% and 25.9%.
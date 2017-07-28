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

Two sided t-test provided the folloing output in R:

        Welch Two Sample t-test

data:  result by type
t = -1.1194, df = 196.58, p-value = 0.2643
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
 -0.19331731  0.05331731
sample estimates:
mean in group class  mean in group comp 
               0.70                0.77 

Conclusion: There is little to no evidence to suggest that the difference in means
is greater than 0. As such, we cannot reject the null hypothesis with a 
p-value of 0.2643 and a 95% confidence interval of (-0.19, 0.05).
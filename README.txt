Svetlichny Game

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
     
We can be 95% certain that that true mean of the quantum strategy lies within
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


There is little to no evidence to suggest that the difference in means
is grater than 0. As such, we cannot reject the null hypothesis with a 
p-value of 0.2643 and a 95% confidence interval of (-0.19, 0.05).
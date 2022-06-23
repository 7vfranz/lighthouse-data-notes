* Conditional probability - probability given probability of other event
* P(A|B) and P(B) > 0
* P(A|B) = P(A intersect B) / P(B)
* probablity of in reduced sample space 
* P(A intersect B) is values in common..
<br>
<br>

* don't always assume independence
* P(A intersect B) = P(A) + P(B) - P(A union(U) B)
* P(A union B) = P(A) + P(B) - P(A inter B)
* P(union) is the whole circle of venn diagram for that condition
* P(intersect) is the overlapping
* P(total) everything
* draw venn diagram if necessary
<br>
<br>

*  P(A compliment) - means compliment/'not' probability not A or A overlapping with others. or not containing A

* if independent = p(A|B) = P(A)
* if dependent P(A|B) > P(A) or < 
<br>
<br>

#### Bayes Theorem
* see videos 
#### Hypothesis testing
* probability of seeing a difference between two populations or equal something. 
* done on population parameters not statistics (statistics used to estimate parameters) 

#### p-value
* p-value: probability of getting observed value of the test statistic or greater - if/assuming the null is true. 
* smaller = more evidence against the null
* if null is true - pvalue ranges from 0 to 1 - average 0.5
* distribution of p value changes as mu gets further from the hypothesis - more likely to get a lower p-value when null is false
* depends on std dev, sample, actual u
* < 0.01 - very strong evidence
* < 0.05 - strong evidence
* < 0.10 - some evidence
* > 0.10 little to no evidence

#### hypothesis testing
* one-way t-test
* chi-squared test
* one-way ANOVA

* one-sided: lower or greater 
* two sided: either - usually used

* z-test really only when SD known - very rare

* t-test - approximates SD based on sample 
    * standard error of mean - estimated SD of sample
    * based on t distribution with n-1 dof
    * higher df = closer to standard normal
    * more sample = closer to normal
    * p value is what we get on both sides
    * test whether - difference from sample and population mean is different 
    * normal quantile-quantile plot - should be straight - know that it's a normal distribution
    * M - u0 / SEM = t 
    * compare t with, t distribution 

* Chi-squared test
    * two categorical variables are related
    * similar to correlation for continuous vars
    * frequency of number observed significantly different?
    * does result match expected counts from null
    * get an chi stat- chi2 = sum of ((observed-exepcted)^2 / expected)
    * dof = # of cells/categories - 1 
    * observed-expected is large - chi will be large - evidence against null
    * chi for that df, and compare to standard chi distribution with 3 DF

* ANOVA
    * population means are all equal
    * tests different in k means, comparing variability between vs within groups
    * F test statistic to get p-value
    * F = mean square variance between or treatment / mean square sum variance within (i.e. error)
    * assumes: independent simple random samples, pops are normally distributed, population variances are equal 


* Central limit theorem [moreCLM](https://machinelearningmastery.com/a-gentle-introduction-to-the-central-limit-theorem-for-machine-learning/)
    * __as more samples -  distribution of mean accross samples will approximate a normal/gaussian distribution__
    * obs - one trial, sample - group of results, population - all possible observation 
    * each trial/observation is independent, same way of sampling "independent and identically" distributed 
    * distribution of errors when estimating population mean will fit a normal distribution
    * estimate of normal distribution more accurate as you do more samples
    * important for sig tests and confidence interval 

* Law of large numbers
    * greater the sample size - the better approximate of population mean

* if population mean is known - sampling distribution mean = population mean 
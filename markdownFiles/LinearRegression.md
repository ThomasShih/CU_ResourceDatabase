## Simple Linear Regression

Linear Regression are studies in the relationship between 2 or more variables, and Single Linear Regression (herein referred to as SLR) in particular is the study in the relationship of two variables. There are two variables, x & y, which are named as follows:

* x is the independent/explanatory/predictor variable
* y is the dependent (or response) variable

The variables x & y are either quantitative (numerical), or qualitative (categorical). The linear relationship is written as follows:
$$
y=\beta_0+\beta_1 x
$$
The element $\beta_0$ is the y-intercept, and $\beta_1$ is the slope of the line of best fit. Sure looks a lot like $y=mx+b$, right? In real statistics, we will nearly always see the probabilistic model, because pretty much nothing in real life follows perfect lines.


$$
y=\beta_0+\beta_1+\epsilon
$$
$\epsilon$ is the error, which represents factors that weren't included in the original relationship. We assume that the errors are normally distributed, with mean 0, and variance $\sigma^2$. This means that the expected value of the errors is 0.
$$
\epsilon \sim N(0,\sigma^2), \forall x
$$
Since the expected value of the errors is 0, $E(y)=E(\beta_0+\beta_1 x + \epsilon) = E(\beta_0+\beta_1 x) + E(\epsilon) = E(\beta_0+\beta_1 x) + 0 = E(\beta_0+\beta_1 x)$

### Assumptions

SLR requires 4 assumptions:

1. x's are observed without error. 
2. y's are independently distributed, with mean $E(y) = \beta_0 +\beta_1 x$
3. y's have constant variance $\sigma^2, \forall x$ 
4. y ~ $N(E(y), \sigma^2)$

### Least Squares Method

The Least Squares Method is important, because it minimizes $e_i's$, and chooses a "best-fitting line", which minimizes the Sum of Squared Errors (SSE), and maximizes the Sum of Squares due to Regression (SSR). Since we don't know the actual values of $\beta_1$ and $\beta_0$, we use estimators, denoted $\hat\beta_1$ and $\hat\beta_0$ respectively. 
$$
\hat\beta_1 = \frac{\sum x_iy_i-\frac{(\sum x_i)(\sum y_i)}n}{\sum x_i^2-\frac{(\sum x_i)^2}{n}} = \frac{S_{xy}}{S_{xx}}
$$

$$
\hat\beta_0=\bar y-\hat\beta_1\bar x
$$

Note: $\bar y=\frac{\sum y_i}{n}$ and $\bar x=\frac{\sum x_i}{n}$ . Needed for other equations is the following equation, which defines SSE as:
$$
SSE=S_{yy}-\frac{(S_{xy})^2}{S_{xx}}
$$


#### Estimation of $\sigma^2$

Since $\beta_0$ and $\beta_1$ are unknow, the population variance $\sigma^2$ is also unknown. We estimate this using $s^2$, called the sample variance.
$$
s^2=\frac{S_{yy}-\frac{(S_{xy})^2}{S_{xx}}}{n-2}=\frac{SSE}{n-2}
$$
SSE is divided by $n-2$ , as there are two parameter estimates, $\hat\beta_0$ and $\hat\beta_1$.  In general, $s^2$ will be $\frac{SSE}{n-\text{number of parameter estimates}}$. This is more applicable in Multiple Linear Regression, where there are more parameter estimates.

### Testing for a significant linear relationship

If we look at the model, $y=\beta_0+\beta_1x+\epsilon$, to tell whether there is a linear relationship, we need to know whether $\beta_1=0, \text{or }\beta_1\ne0$. If $\beta_1=0$, then there is no linear relationship, since if $y=\beta_0+\beta_1x$, and $\beta_1=0$, then $y=\beta_0+0(x)=\beta_0$. How do we tell if $\beta_1 = 0$? In SLR, we use either the t-test or the F-test.

#### T-test

For the t-test, we use hypothesis testing that was taught in STAT2507. If you need a refresher, watch this video by Khan Academy.

<iframe width="560" height="315" src="https://www.youtube.com/watch?v=-FtlH4svqx4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

There are three possible hypotheses, displayed below.
$$
\text{1. }H_0:\beta_1=0 \text{ (no linear relation)}, H_A:\beta_1\ne0 \text{ (linear relation)}; \alpha
$$

$$
\text{2. }H_0:\beta_1\le0, H_A:\beta_1>0 \text{ (positive linear relation)}; \alpha
$$

$$
\text{3. }H_0:\beta_1\ge0, H_A:\beta_1<0 \text{ (negative linear relation)}; \alpha
$$

The test stat for t-tests is: $t=\frac{\hat\beta_1}{\sqrt{\frac{s^2}{S_{xx}}}}\sim t_{(n-2)}$. Each of the hypotheses has different requirements to reject $H_0$.
$$
\text{1. }RR: \text{We reject }H_0 \text{ if: } t>t_{\frac{\alpha}{2};n-2} \text{ or if }t<-t_{\frac{\alpha}{2}; n-2}
$$

$$
\text{2. }RR: \text{We reject }H_0 \text{ if: } t>t_{\frac{\alpha}{2};n-2}
$$

$$
\text{3. }RR: \text{We reject }H_0 \text{ if: } t<-t_{\frac{\alpha}{2};n-2}
$$

One important thing to note is that you never say that you accept $H_0$. You either reject $H_0$, and say that there is evidence to show that $H_A$ is True, or you do not reject $H_0$, and say there is not enough evidence to support $H_A$. Even if we do not reject $H_0$, it does not necessarily mean that $x \text{ & } y$ are not related, but it means that they are just not linearly related. They may however be related in another way. If we reject $H_0$, **we do not conclude** that the relationship is linear, however it means that a linear relationship is reasonable. $y$ may depend on other $x$'s as well. We also do not conclude that $x$ *causes* $y$, as correlation does not equal causation.

### Confidence Intervals for $\beta_1 \text{ and } \beta_0$

$$
\beta_1\in(\hat\beta_1\pm t_{\frac{\alpha}{2};n-2}\sqrt\frac{s^2}{S_{xx}})
$$

$$
\beta_0\in(\hat\beta_0\pm t_{\frac{\alpha}{2};n-2}\sqrt\frac{s^2\sum x^2}{n*S_{xx}})
$$

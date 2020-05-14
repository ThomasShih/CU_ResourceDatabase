# Differentiation

------

## Prerequisites:

- Limits

------

**Note: ** For the purposes of this document, derivative functions will be notated by a  $^|$ notation, such as  $f^|(x)$

------

In limits, we discussed how to find the exact slope at a given point using a version of the classic formula for [slope](https://www.mathsisfun.com/algebra/line-equation-point-slope.html). Differentiation is simply the function$^1$ we apply to a given equation $f(x)$ in order to find the slope of that equation $f^|(x)$, we will discuss how this function$^1$ is represented in math later.

Consider the function $f(x) = x^3$ found in the limits chapter, in order to determine the instantaneous slope at $x=2$ we found that this instantaneous function suffice;
$$
\lim_{l \to 0} \frac{f(2 + l)-f(2 - l)}{(2 + l) - (2 - l)} = \lim_{l \to 0} \frac{ (2+l)^3-(2-l)^3}{2 + l - 2 -(-l)}
$$

To recap, the limits equation represents the slope formula for a "spirit level" of length 0, in other words; it is the instantaneous slope of $f(x)$ at 2. What if we replaced the 2 with the original variable $x$? This would give us a formula to find the instantaneous slope at $x$:
$$
f^|(x) = \lim_{l \to 0} \frac{f(x + l)-f(x - l)}{(x + l) - (x - l)}
$$
Using algebra, we find that: (visit symbolab.com to verify)
$$
\frac{f(x + l)-f(x - l)}{(x + l) - (x - l)} = \frac{ (x+l)^3-(x-l)^3}{x + l - x -(-l)} = 3x^2+l^2
$$
Therefore:
$$
\lim_{l \to 0} \frac{f(x + l)-f(x - l)}{(x + l) - (x - l)} = \lim_{l \to 0} 3x^2+l^2
$$
Notice how $l^2$ can be simplified?
$$
\lim_{l \to 0} 3x^2+l^2 =  3x^2+0^2 = 3x^2
$$
Congratulations! You just found the formula for calculating the instantaneous slope of $f(x)$.
$$
f^|(x) = \lim_{l \to 0} \frac{f(x + l)-f(x - l)}{(x + l) - (x - l)} = 3x^2
$$
You can call $f^|(x)$ a slope function, you can call it anything you want. But in math, we call  $f^|(x)$ the ***derivative*** of $f(x)$. This is what derivative essentially means, it means a function for calculation the instantaneous slope of a function.

------

Now to the main point of this chapter, what is differentiation? The act of differentiation is simply to convert a function to its derivative. This process is called the differential. We can rewrite our original equation like this:
$$
f^|(x) = \lim_{l \to 0} \frac{f(x + l)-f(x - l)}{(x + l) - (x - l)} = \frac{\partial(f(x))}{\partial(x)}
$$
In differential terms, we are taking the derivative of $f(x)$ with respect to $x$. You can apply this derivative process to any equation you find. 

However the algebra is complex, just like how I skipped over the algebra portion above. There is an extremely high chance for you to mess up. Graduate students back in the days literally write theses (plural of thesis) on these (pun intended) topics. This is why the math community has created differentiation tables to assist you in generating differentials easily, sort of like a black box. This is the reason why when you look up a differential equation formula sheet, you can find that $x^3 \to 3x^2$. This is also the reason why I will simply refer you over to an external source to find the derivatives of most functions.

------

***This is the point where I recommend people stop.*** I personally recommend taking what I said above at face level, this is because you can understand the material enough that you have working capacity of calculus. To fully understand why we have a $\partial()$ term on the bottom, you need to work with formulas with more than one variable, or more simply put; vector calculus...

Still here? Let's continue.

Why is $\frac{\partial(f(x))}{\partial(x)}$ structured the way it is? Let's represent the original formula in terms of $y$ and $x$:
$$
f(x) = y = x^3
$$
Lets apply a $\partial$ wrapper to $x^3$. Remember how in algebra you are told that what you do to one side you must do to another? Just like how dividing the left by 2 means you need to divide the right by 2? Well this is still the case with applying a function to a side of a equation.
$$
y = x^3 \to \partial(y) = \partial(x^3)
$$
Consider this, in this immediate equation, y is unknown, x is also unknown. This means that we cannot take the partial ($\partial$) of these equations. So what do we do?

Recall in algebra:
$$
\sqrt{4x} = 2\sqrt{x}
$$
We cannot resolve what the square root of x is, however we worked around that and simplified the function by applying the square root to only the 4 in order to remove it from the square root. This is what we do to differentials as well. We will resolve the cubic exponential in order to simplify the equation:
$$
\partial(y) = \partial(x^3) -> \partial(y) = 3x^2\partial(x)
$$
Let's isolate the $3x^3$:
$$
\frac{\partial(y)}{\partial(x)} = \frac{3x^2\partial(x)}{\partial(x)} = 3x^2
$$
Great! You found the slope function again!

But what does this mean? Lets not forget that:
$$
\frac{\partial(y)}{\partial(x)} = \frac{3x^2\partial(x)}{\partial(x)} = \frac{\partial(f(x))}{\partial(x)} = f^|(x)
$$
This is the reason why we write differentiations like this. Let it sink it.

Still following? If so, great, your fast at learning. If not? This is okay, most people don't understand why this works. The author (me) writing this only figured out this relationship after taking Vector Calculus in my second year, and I was considered qualified enough to teach normal Calculus before knowing this.
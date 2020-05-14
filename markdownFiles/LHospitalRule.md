# L' Hospital's Rule

------

## Prerequisites:

- Derivatives
- Basic understanding of limits

------

Hereon referred to as LH's rule, LH's rule is primarily a quick method of determining the limits of [indeterminate forms](https://brilliant.org/wiki/indeterminate-forms/) (hereon referred to as just limit). LH's rule is simply an algorithm performed on an in these steps:

While the limit is still indeterminate:

1. Split the limit into an numerator and denominator:
   $$
   \lim_{x \to a} f(x) \to \lim_{x \to a} \frac{f_1(x)}{f_2(x)}
   $$
   
2. Take the derivative of both the numerator and denominator:
$$
\frac{\partial(f_1(x))}{dx} \to f^1_1(x)
$$


$$
\frac{\partial(f_2(x))}{dx} \to f^1_2(x)
$$

3. Reconstruct the limit as:
$$
\lim_{x \to a} \frac{f^1_1(x)}{f^1_2(x)}
$$
4. Check to see if limit is indeterminate, repeat process if limit is still indeterminate

As a TA, this is as far as I recommend students go. However, if you want to understand why it works, [visit this qoura page.](https://www.quora.com/What-is-an-intuitive-explanation-of-lHopitals-Rule)


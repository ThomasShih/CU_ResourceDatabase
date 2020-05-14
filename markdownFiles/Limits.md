# Limits

------

If we are dealing with a simple formula such as:
$$
f(x) = x^3
$$
And we need to find what $l$ is at 2, this is pretty easy, you just plug in the number:
$$
f(2) = 2^3 = 16
$$
Congrats! You solved a limit!, what i mean is you found what $f(l)$ results in as $l$ approaches 
$$
\lim_{x \to 2} f(x) = f(2) = 2^3 = 16
$$
But what if you need to figure out the slope?

Say your playing [line rider](https://www.linerider.com/):

![https://www.linerider.com/_v1818.0/social.png](https://www.linerider.com/_v1818.0/social.png)

You want to figure out what is the degree of the slope is at any given moment, you need a method of calculating this. For a straight line, this is pretty simple. You simply take the the first point of that line, and the last point of the line, to [figure out the slope](https://www.mathopenref.com/coordslope.html). This is a bit more complicated when dealing with curved lines, however the theory still stays the same.

Say you want to calculate the slope, your first instinct may probally be to use a [spirit level](https://www.homedepot.com/b/Tools-Hand-Tools-Measuring-Tools-Levels/N-5yc1vZc1zh) to measure the inclination. 

![https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Tool-level.jpg/330px-Tool-level.jpg](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Tool-level.jpg/330px-Tool-level.jpg)

This is good. But what if your asked to be more accurate?

A good assumption is to take a shorter level, hence you can get closer to the physical point your measuring the slope from. This gives your a "higher definition" of what your measuring, hence lowering your error. However its still not perfect. 

This raises a good point, as your level gets shorter and shorter, you can achieve a more and more accurate reading of the actual slope. But what is the reading of this level as the two ends approach your point? Or in other words, what is the limit as your level ends approach the point?

Most of the time, you can just plug in very small number increments just before and just after the point in question to calculate the curve. This is completely reasonable. In fact, this is how computers estimate slopes. 

However...

In Math, we deal with exacts and absolutes. And hence, we need to figure out clever ways of rearranging formulas such that we can resolve this exact slope. 

Consider the equation we dealt with at the start. The slope for the point at 2 can be approximated as
$$
\frac{f(3)-f(1)}{3-1} = \frac{27-1}{2} = 13
$$
You basically done a limit, that looks like, where $l$ is equal to half the length of the level:
$$
\lim_{l=1} \frac{f(2 + l)-f(2-l)}{(2+l) - (2-l)} = \frac{f(3)-f(1)}{3-1} = \frac{27-1}{2} = 13
$$
Our current spirit level has a length of 2, because we are measuring from 1 to 3, a difference of 2. What if we take a spirit level with a length of 1? 
$$
\lim_{l=.5} \frac{f(2 + l)-f(2-l)}{(2+l) - (2-l)} = \frac{f(2.5)-f(1.5)}{2.5-1.5} = \frac{15.63-3.38}{1} = 12.25
$$
Or length of .5?
$$
\lim_{l=.25} \frac{f(2 + l)-f(2-l)}{(2+l) - (2-l)} = \frac{f(2.25)-f(1.75)}{2.25-1.75} = \frac{11.39-5.36}{.5} = 12.06
$$
We can shrink our spirit level smaller and smaller, but it can never be elact...



Or can it? What if our spirit level has a length of 0? **This is the question math asks**.
$$
\lim_{l = 0} \frac{f(2 + l)-f(2-l)}{(2+l) - (2-l)}
$$
Now obviously, this cant happen. because if l 0, then your output would be undefined:
$$
\lim_{l=0} \frac{f(2)-f(2)}{(2) - (2)} = \lim_{l=0} \frac{0}{0} = \lim_{l=0} undefined
$$
But lets step back, what if we say that its the limit as l approaches zero? l would still be a variable, and so we can do algebra on it.
$$
\lim_{l \to 0} \frac{f(2 + l)-f(2 - l)}{(2 + l) - (2 - l)}
$$
All these functions are getting a bit confusing, lets rearrange them with the help of wolfram alpha:
$$
\frac{f(2 + l)-f(2 - l)}{(2 + l) - (2 - l)} = \frac{ (2+l)^3-(2-l)^3}{2 + l - 2 -(-l)} = \frac{2l^3 + 24l}{2l}
$$
Lets plug this back into the limits equation
$$
\lim_{l \to 0} \frac{f(2 + l)-f(2 - l)}{(2 + l) - (2 - l)} = \lim_{l \to 0} \frac{2l^3 + 24l}{2l} = \lim_{l \to 0} \frac{2l^2 + 24}{2} = \lim_{l \to 0} \frac{l^2 + 12}{1}
$$
Suddenly, we can now plug in $l=0$ to find that the limit is equals to 12. Remember how l was proportional to the length of the spirit level? Well, if $l$ is zero, we have just created an impossible spirit level of length zero! This number 12 represents the elact slope of the $f(l)$ curve at 2!



For a different approach at explaining this, visit Paul's math notes:

http://tutorial.math.lamar.edu/Classes/CalcI/TheLimit.aspl
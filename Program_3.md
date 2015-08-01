## NOT DONE

## Elliptical Curve Encryption

### Background

A `trapdoor` function is one that is easy to compute one way, and extremely difficult to reverse. This is the backbone behind public key cryptogrophy. However the authors of [this](http://arstechnica.com/security/2013/10/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/2/) article (very good overview of Elliptical Curve Crypto) point out: 

>"Many experts are concerned that the mathematical algorithms behind RSA and Diffie-Hellman could be broken within as little as five years. With the clock ticking that fast, ECC may be left as the only reasonable alternative." 

So we may want to investigate some alternatives to our current public key cryptography standards, and this is why we are going to play with elliptical curves. 

### Overview

You saw the math in class. Given `y^2 = x^3 + ax + b`, we want to find two values `a` and `b` that generate a good elliptical curve. Then (for this program) given two points: `(x1,y1),(x2,y2)` find a third point: `(x3,y3)` that is (hopefully) on the curve as well. In class we stated that integer math was required (answers in the form of a nice fraction, no decimals), but we changed our mind. Decimal values are acceptible.

### Visualization

To add a little learning to the program, we also want to visualize our curves and points. Your math should work for any input, however for visualizing the data we will keep the values for all inputs reasonable. Below is some helper code to get your visualizations started. It's remarkably easy in python.

```python
import numpy as np
import matplotlib.pyplot as plt

#Values defining our curve
a = 1
b = -1

#Determines width and height of plot
w = 10
h = 12

# This creates a mesh grid with values determined by width and height (w,h)
# of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
y, x = np.ogrid[-h:h:1000j, -w:w:1000j]

# Plot the curve (using matplotlib's countour function)
# This drawing function applies a "function" described in the
# 3rd parameter:  pow(y, 2) - ( pow(x, 3) - x + 1 ) to all the
# values in x and y.
# The .ravel method turns the x and y grids into single dimensional arrays
plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) - x + 1 ), [0])

# Create two points
x1 = 0
y1 = -1
x2 = 5
y2 = -11

#Get the slope of the line
m = (y1-y2)/(x1-x2)

# Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
plt.plot(x1, y1,'ro')
plt.plot(x2, y2,'ro')

# Use a contour plot to draw the line (in pink) connecting our point.
plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))

# I hard coded the third point, YOU will use good ol mathematics to find
# the third point
plt.plot(-1, 1,'yo')

# Show a grid background on our plot
plt.grid()

# Show the plot
plt.show()
```

#### Passing in Parameters



##### Driver Snippet:
```python
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1", help="")
    parser.add_argument("-y1",dest="y1", help="")
    parser.add_argument("-x2",dest="x2", help="")
    parser.add_argument("-y2",dest="y2", help="")

    args = parser.parse_args()

    # Example:
    # python3 program_name.py -x1 2 -y1 3 -x2 -1 -y2 -1 -a 2 -b 1

    print("a=",args.a," b=",args.b,"x1=",args.x1," y1=",args.y1," x2=",args.x2," y2=",args.y2)


if __name__ == '__main__':
    main()
```

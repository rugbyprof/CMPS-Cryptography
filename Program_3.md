## Elliptical Curve Encryption

### Background

A `trapdoor` function is one that is easy to compute one way, and extremely difficult to reverse. This is the backbone behind public key cryptogrophy. However the authors of [this](http://arstechnica.com/security/2013/10/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/2/) article (very good overview of Elliptical Curve Crypto) point out: 

>"Many experts are concerned that the mathematical algorithms behind RSA and Diffie-Hellman could be broken within as little as five years. With the clock ticking that fast, ECC may be left as the only reasonable alternative." 

So we may want to investigate some alternatives to our current public key cryptography standards, and this is why we are going to play with elliptical curves. 

### Overview

You saw the math in class. Given `y^2 = x^3 + ax + b`, we want to find two values `a` and `b` that generate a good elliptical curve. Then (for this program) given two points: `(x1,y1),(x2,y2)` find a third point: `(x3,y3)` that is (hopefully) on the curve as well. In class we stated that integer math was required (answers in the form of a nice fraction, no decimals), but we changed our mind. Decimal values are acceptible.

### Requirements:

- Create a folder called `First.Last.Elliptical` where YourName is actually your name: (e.g. Reyansh.Jones.Vigenere). Notice the dots, those are critical (letter grade off if not named correctly).
- Remainder of files goes in your folder.
- Create a file called `main.py`.
- `main.py` will be similar to the driver snippet except you will adjust the arguments accordingly.
- Here are some examples for you to base your code on: 
     - `python3 main.py -x1 2 -y1 3 -x2 -1 -y2 -1 -a 2 -b 1`

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

# Annotate the plot with your name using width (w) and height (h) as your reference points.
an1 = plt.annotate("Terry Griffin", xy=(-w+2 , h-2), xycoords="data",
              va="center", ha="center",
              bbox=dict(boxstyle="round", fc="w"))

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

# Annotate point 1
plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )

plt.plot(x2, y2,'ro')

# Annotate point 2
plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )
        
# Use a contour plot to draw the line (in pink) connecting our point.
plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))

# I hard coded the third point, YOU will use good ol mathematics to find
# the third point
plt.plot(-1, 1,'yo')

# Annotate point 3
plt.annotate('-1,1', xy=(-1, 1), xytext=(-1+1,1+1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )

# Show a grid background on our plot
plt.grid()

# Show the plot
plt.show()
```

#### Passing in Parameters

Each parameter must be passed in from the command line using something similar to the following. By similar, I mean the parameters must be named ***exactly*** as below.

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
### Output

Your output should look like the image below. Your scale can differ depending on the minimum and maximum x and y values.
After you calculate the 3rd point, you need to then determine the max and min out of all the values to size your plot area.
Remember your plot size is determined by how many points you plot in the curve:

```python
y, x = np.ogrid[-h:h:1000j, -w:w:1000j]
```

Therefore you need to determine the location of point 3 (x3,y3) before you create and populate the plot.

![](http://f.cl.ly/items/2J2u1q2F1c0A1p21220S/ecurve.png)

#### What to Turn In
- All of your files need to be uploaded to github by ***Tuesday 4 Aug 2:30 p.m.*** 
- All work needs to done on an individual basis, and suspected cheating will result in appropriate action.
- All code needs to commented at a level appropriate upper level and graduate work.
- A name block will be at the top of all your programs just like the requirements in program 1. 
- Late programs will be reduced by 15 / 100 points the first day, and 10 points for each subsequent day until a 50 / 100 is reached. This way late programs can still get half credit. 
- No late programs will be accepted after a subsequent program is assigned.

#!/usr/bin/env python
"""Module providing functionality surrounding gaussian function.
"""
SVN_REVISION = '$LastChangedRevision: 16541 $'

import sys
import numpy

def gaussian2(size, sigma):
    """Returns a normalized circularly symmetric 2D gauss kernel array
    
    f(x,y) = A.e^{-(x^2/2*sigma^2 + y^2/2*sigma^2)} where
    
    A = 1/(2*pi*sigma^2)
    
    as define by Wolfram Mathworld 
    http://mathworld.wolfram.com/GaussianFunction.html
    """
    A = 1/(2.0*numpy.pi*sigma**2)
    x, y = numpy.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]
    g = A*numpy.exp(-((x**2/(2.0*sigma**2))+(y**2/(2.0*sigma**2))))
    return g

def fspecial_gauss(size, sigma):
    """Function to mimic the 'fspecial' gaussian MATLAB function
    """
    x, y = numpy.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]
    g = numpy.exp(-((x**2 + y**2)/(2.0*sigma**2)))
    return g/g.sum()



if __name__ == '__main__':
    sys.exit(main())
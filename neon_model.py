import numpy as np


'''
Goal is to recreate neon isotope plot 
fig 13 page 21
from HELIX proposal (?)

for given ratio of Neon isotopes to Neon
1. make histogram of expected counts for a given total
2. using peak, create gaussian to get a smear of values
given the resolution of HELIX
note: peaks may not be centered
idea is to simulate what we would see given enough data
I htink this is what best case scenario would be
3. then we will use our distrbution smearing for a given
number of events thrown and bin it
We then fit a new fit to these histograms
4. then we compare how far off the simulation is and the
fitted gaussian
to compare we can do residuals etc. 
'''
N = 1000


Ne21_ratio = 0.5
Ne22_ratio = 0.5

Ne20 = (1 + Ne21_ratio + Ne22_ratio) * N
Ne21 = Ne21_ratio * Ne20
Ne22 = Ne22_ratio * Ne20

Total = Ne20 + Ne21 + Ne22

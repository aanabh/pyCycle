"""CO2, CO, O2 reactants, used for testing and development, a subset of the janaf thermo fit set"""

import numpy as np
from collections import OrderedDict


products = OrderedDict([
    ('CO',{
      'coeffs': [
            [ 1.489045326e+04, -2.922285939e+02,  5.724527170e+00, -8.176235030e-03, # 200 - 1000
              1.456903469e-05, -1.087746302e-08,  3.027941827e-12,  -1.303131878e+04, -7.859241350e+00],
            [ 4.619197250e+05, -1.944704863e+03,5.916714180e+00,-5.664282830e-04, # 1000 - 6000
              1.398814540e-07, -1.787680361e-11,9.620935570e-16,-2.466261084e+03, -1.387413108e+01],
            [ 8.868662960e+08, -7.500377840e+05,  2.495474979e+02, -3.956351100e-02, # 6000 - 20000
              3.297772080e-06, -1.318409933e-10,  1.998937948e-15,  5.701421130e+06, -2.060704786e+03],
      ],
      'ranges': [200,1000,6000,20000],
      'wt': 28.01,
      'elements': OrderedDict([('C',1), ('O',1)]),
    }),
    ('CO2',{
      'coeffs': [
            [ 4.943650540e+04, -6.264116010e+02,  5.301725240e+00,  2.503813816e-03, # 200 - 1000
              -2.127308728e-07, -7.689988780e-10,  2.849677801e-13, -4.528198460e+04, -7.048279440e+00, ],
            [ 1.176962419e+05, -1.788791477e+03,8.291523190e+00,-9.223156780e-05, # 1000 - 6000
              4.863676880e-09, -1.891053312e-12,6.330036590e-16,-3.908350590e+04, -2.652669281e+01],
            [ -1.544423287e+09, 1.016847056e+06, -2.561405230e+02,  3.369401080e-02, # 6000 - 20000
              -2.181184337e-06, 6.991420840e-11, -8.842351500e-16, -8.043214510e+06,  2.254177493e+03]
      ],
      'ranges': [201,1000,6000,20000],
      'wt': 44.01,
      'elements': OrderedDict([('C',1), ('O',2)]),
    }),
    ('O2',{
      'coeffs':[
            [ -3.425563420e+04, 4.847000970e+02, 1.119010961e+00, 4.293889240e-03, # 200 - 1000
              -6.836300520e-07, -2.023372700e-09, 1.039040018e-12, -3.391454870e+03, 1.849699470e+01],
            [ -1.037939022e+06,2.344830282e+03,1.819732036e+00,1.267847582e-03, # 1000 - 6000
              -2.188067988e-07,2.053719572e-11,-8.193467050e-16,-1.689010929e+04, 1.738716506e+01],
            [ 4.975294300e+08, -2.866106874e+05,  6.690352250e+01, -6.169959020e-03,  # 6000 - 20000
              3.016396027e-07, -7.421416600e-12,  7.278175770e-17, 2.293554027e+06, -5.530621610e+02]
      ],
      'ranges': [200,999,6000,20000],
      'wt': 32,
      'elements': {'O':2},
    })
])

init_prod_amounts = OrderedDict([ # initial value used to set the atomic fractions in the mixture
    ('CO', 0),
    ('CO2', 1),
    ('O2', 0),
])

element_wts = {
  'C':12.01, 'O': 16.0,
}

import numpy as np

from pycycle.maps.map_data import MapData


"""Python version of CFM56 LPC map from NPSS"""
LPCMap = MapData()

# Map design point values
LPCMap.defaults = {}
LPCMap.defaults['alphaMap'] = 0.0
LPCMap.defaults['NcMap'] = 1.100
LPCMap.defaults['PR'] = 1.800
LPCMap.defaults['RlineMap'] = 2.200
LPCMap.RlineStall = 1.0

LPCMap.alphaMap = np.array([0.000, 1.000])
LPCMap.NcMap = np.array([0.300, 0.400, 0.500, 0.600, 0.700, 0.800, 0.900, 1.000, 1.100, 1.200, 1.250])
LPCMap.RlineMap = np.array([1.000, 1.200, 1.400, 1.600, 1.800, 2.000, 2.200, 2.400, 2.600, 2.800, 3.000, 3.200]) 

LPCMap.WcMap = np.array([[[ 38.0744,  42.9399,  47.7510,  52.5016,  57.1863,  61.7994, 66.3359,  70.7905,  75.1584,  76.5663,  76.5663,  76.5663],
  [ 54.0383,  60.0388,  65.9233,  71.6816,  77.3038,  82.7808, 88.1038,  93.2648,  98.2565, 101.0545, 101.0545, 101.0545],
  [ 70.3200,  77.5153,  84.4949,  91.2421,  97.7419, 103.9805, 109.9459, 115.6273, 121.0156, 124.6409, 124.6409, 124.6409],
  [ 87.4860,  95.6896, 103.5393, 111.0128, 118.0907, 124.7566, 130.9971, 136.8019, 142.1633, 146.2312, 146.2312, 146.2312],
  [105.8588, 114.8071, 123.2285, 131.0978, 138.3948, 145.1045, 151.2169, 156.7268, 161.6340, 165.7319, 165.7319, 165.7319],
  [125.1164, 134.6062, 143.3572, 151.3454, 158.5548, 164.9773, 170.6127, 175.4677, 179.5554, 182.8951, 183.0717, 183.0717],
  [144.4910, 154.5703, 163.6243, 171.6346, 178.5959, 184.5149, 189.4099, 193.3090, 196.2491, 198.2745, 198.4155, 198.4155],
  [165.9141, 176.2228, 185.1849, 192.7986, 199.0806, 204.0644, 207.7979, 210.3410, 211.7638, 212.1506, 212.1506, 212.1506],
  [188.5677, 198.3532, 206.6834, 213.5745, 219.0613, 223.1942, 226.0370, 227.6647, 228.1611, 228.1611, 228.1611, 228.1611],
  [214.1402, 222.1943, 228.9021, 234.2963, 238.4220, 241.3359, 243.1030, 243.7959, 243.8124, 243.8124, 243.8124, 243.8124],
  [227.8569, 234.5820, 240.1193, 244.5040, 247.7802, 250.0000, 251.2213, 251.5216, 251.5216, 251.5216, 251.5216, 251.5216]],
  [[ 38.0744,  42.9399,  47.7510,  52.5016,  57.1863,  61.7994, 66.3359,  70.7905,  75.1584,  76.5663,  76.5663,  76.5663],
  [ 54.0383,  60.0388,  65.9233,  71.6816,  77.3038,  82.7808, 88.1038,  93.2648,  98.2565, 101.0545, 101.0545, 101.0545],
  [ 70.3200,  77.5153,  84.4949,  91.2421,  97.7419, 103.9805, 109.9459, 115.6273, 121.0156, 124.6409, 124.6409, 124.6409],
  [ 87.4860,  95.6896, 103.5393, 111.0128, 118.0907, 124.7566, 130.9971, 136.8019, 142.1633, 146.2312, 146.2312, 146.2312],
  [105.8588, 114.8071, 123.2285, 131.0978, 138.3948, 145.1045, 151.2169, 156.7268, 161.6340, 165.7319, 165.7319, 165.7319],
  [125.1164, 134.6062, 143.3572, 151.3454, 158.5548, 164.9773, 170.6127, 175.4677, 179.5554, 182.8951, 183.0717, 183.0717],
  [144.4910, 154.5703, 163.6243, 171.6346, 178.5959, 184.5149, 189.4099, 193.3090, 196.2491, 198.2745, 198.4155, 198.4155],
  [165.9141, 176.2228, 185.1849, 192.7986, 199.0806, 204.0644, 207.7979, 210.3410, 211.7638, 212.1506, 212.1506, 212.1506],
  [188.5677, 198.3532, 206.6834, 213.5745, 219.0613, 223.1942, 226.0370, 227.6647, 228.1611, 228.1611, 228.1611, 228.1611],
  [214.1402, 222.1943, 228.9021, 234.2963, 238.4220, 241.3359, 243.1030, 243.7959, 243.8124, 243.8124, 243.8124, 243.8124],
  [227.8569, 234.5820, 240.1193, 244.5040, 247.7802, 250.0000, 251.2213, 251.5216, 251.5216, 251.5216, 251.5216, 251.5216]]])

LPCMap.effMap = np.array([[[.7256, .7656, .7978, .8195, .8274, .8164, .7494, .5651, .1931, .0000, .0000, .0000],
  [.7474, .7848, .8147, .8351, .8430, .8339, .7757, .6161, .3003, .0000, .0000, .0000],
  [.7610, .7984, .8286, .8496, .8586, .8516, .7977, .6479, .3526, .0000, .0000, .0000],
  [.7744, .8117, .8421, .8637, .8738, .8685, .8183, .6765, .3970, .0000, .0000, .0000],
  [.7872, .8240, .8542, .8759, .8866, .8827, .8360, .7028, .4407, .0000, .0000, .0000],
  [.7965, .8329, .8627, .8843, .8953, .8924, .8485, .7222, .4748, .0391, .0000, .0000],
  [.7997, .8368, .8673, .8896, .9013, .8991, .8561, .7310, .4858, .0551, .0000, .0000],
  [.8034, .8405, .8712, .8937, .9058, .9042, .8628, .7420, .5068, .0979, .0000, .0000],
  [.8214, .8533, .8793, .8981, .9079, .9062, .8724, .7766, .5961, .2955, .0000, .0000],
  [.8425, .8663, .8853, .8985, .9047, .9025, .8778, .8117, .6929, .5052, .2255, .0000],
  [.8540, .8731, .8880, .8981, .9024, .9000, .8800, .8286, .7386, .6003, .4004, .1206]],
  [[.7256, .7656, .7978, .8195, .8274, .8164, .7494, .5651, .1931, .0000, .0000, .0000],
  [.7474, .7848, .8147, .8351, .8430, .8339, .7757, .6161, .3003, .0000, .0000, .0000],
  [.7610, .7984, .8286, .8496, .8586, .8516, .7977, .6479, .3526, .0000, .0000, .0000],
  [.7744, .8117, .8421, .8637, .8738, .8685, .8183, .6765, .3970, .0000, .0000, .0000],
  [.7872, .8240, .8542, .8759, .8866, .8827, .8360, .7028, .4407, .0000, .0000, .0000],
  [.7965, .8329, .8627, .8843, .8953, .8924, .8485, .7222, .4748, .0391, .0000, .0000],
  [.7997, .8368, .8673, .8896, .9013, .8991, .8561, .7310, .4858, .0551, .0000, .0000],
  [.8034, .8405, .8712, .8937, .9058, .9042, .8628, .7420, .5068, .0979, .0000, .0000],
  [.8214, .8533, .8793, .8981, .9079, .9062, .8724, .7766, .5961, .2955, .0000, .0000],
  [.8425, .8663, .8853, .8985, .9047, .9025, .8778, .8117, .6929, .5052, .2255, .0000],
  [.8540, .8731, .8880, .8981, .9024, .9000, .8800, .8286, .7386, .6003, .4004, .1206]]])

LPCMap.PRmap = np.array([[[1.0423, 1.0412, 1.0393, 1.0367, 1.0333, 1.0292, 1.0234, 1.0151, 1.0043, 1.0000, 1.0000, 1.0000],
  [1.0760, 1.0738, 1.0704, 1.0658, 1.0600, 1.0530, 1.0434, 1.0297, 1.0122, 1.0000, 1.0000, 1.0000],
  [1.1215, 1.1180, 1.1127, 1.1055, 1.0965, 1.0856, 1.0707, 1.0497, 1.0228, 1.0000, 1.0000, 1.0000],
  [1.1789, 1.1738, 1.1660, 1.1555, 1.1423, 1.1266, 1.1052, 1.0753, 1.0374, 1.0000, 1.0000, 1.0000],
  [1.2494, 1.2422, 1.2312, 1.2167, 1.1986, 1.1771, 1.1481, 1.1078, 1.0572, 1.0000, 1.0000, 1.0000],
  [1.3353, 1.3253, 1.3105, 1.2910, 1.2669, 1.2384, 1.2002, 1.1476, 1.0822, 1.0056, 1.0000, 1.0000],
  [1.4411, 1.4282, 1.4088, 1.3830, 1.3512, 1.3136, 1.2632, 1.1942, 1.1088, 1.0101, 1.0000, 1.0000],
  [1.5724, 1.5561, 1.5313, 1.4982, 1.4572, 1.4088, 1.3440, 1.2556, 1.1472, 1.0233, 1.0000, 1.0000],
  [1.7323, 1.7101, 1.6785, 1.6379, 1.5888, 1.5318, 1.4572, 1.3572, 1.2358, 1.0982, 1.0000, 1.0000],
  [1.9360, 1.9056, 1.8662, 1.8184, 1.7625, 1.6991, 1.6190, 1.5142, 1.3887, 1.2471, 1.0944, 1.0000],
  [2.0507, 2.0158, 1.9729, 1.9223, 1.8645, 1.8000, 1.7201, 1.6176, 1.4958, 1.3584, 1.2098, 1.0546]],
  [[1.0423, 1.0412, 1.0393, 1.0367, 1.0333, 1.0292, 1.0234, 1.0151, 1.0043, 1.0000, 1.0000, 1.0000],
  [1.0760, 1.0738, 1.0704, 1.0658, 1.0600, 1.0530, 1.0434, 1.0297, 1.0122, 1.0000, 1.0000, 1.0000],
  [1.1215, 1.1180, 1.1127, 1.1055, 1.0965, 1.0856, 1.0707, 1.0497, 1.0228, 1.0000, 1.0000, 1.0000],
  [1.1789, 1.1738, 1.1660, 1.1555, 1.1423, 1.1266, 1.1052, 1.0753, 1.0374, 1.0000, 1.0000, 1.0000],
  [1.2494, 1.2422, 1.2312, 1.2167, 1.1986, 1.1771, 1.1481, 1.1078, 1.0572, 1.0000, 1.0000, 1.0000],
  [1.3353, 1.3253, 1.3105, 1.2910, 1.2669, 1.2384, 1.2002, 1.1476, 1.0822, 1.0056, 1.0000, 1.0000],
  [1.4411, 1.4282, 1.4088, 1.3830, 1.3512, 1.3136, 1.2632, 1.1942, 1.1088, 1.0101, 1.0000, 1.0000],
  [1.5724, 1.5561, 1.5313, 1.4982, 1.4572, 1.4088, 1.3440, 1.2556, 1.1472, 1.0233, 1.0000, 1.0000],
  [1.7323, 1.7101, 1.6785, 1.6379, 1.5888, 1.5318, 1.4572, 1.3572, 1.2358, 1.0982, 1.0000, 1.0000],
  [1.9360, 1.9056, 1.8662, 1.8184, 1.7625, 1.6991, 1.6190, 1.5142, 1.3887, 1.2471, 1.0944, 1.0000],
  [2.0507, 2.0158, 1.9729, 1.9223, 1.8645, 1.8000, 1.7201, 1.6176, 1.4958, 1.3584, 1.2098, 1.0546]]])

#LPCMap.Nc_data, LPCMap.alpha_data, LPCMap.Rline_data = np.meshgrid(LPCMap.Nc_vals, LPCMap.alpha_vals, LPCMap.Rline_vals, sparse=False)
LPCMap.Npts = LPCMap.NcMap.size

LPCMap.units = {}
LPCMap.units['NcMap'] = 'rpm'
LPCMap.units['WcMap'] = 'lbm/s'

# format for new regular grid interpolator:

LPCMap.param_data = []
LPCMap.output_data = []

LPCMap.param_data.append({'name': 'alphaMap', 'values': LPCMap.alphaMap,
                          'default': 0, 'units': None})
LPCMap.param_data.append({'name': 'NcMap', 'values': LPCMap.NcMap,
                          'default': 1.1, 'units': 'rpm'})
LPCMap.param_data.append({'name': 'RlineMap', 'values': LPCMap.RlineMap,
                          'default': 2.2, 'units': None})

LPCMap.output_data.append({'name': 'WcMap', 'values': LPCMap.WcMap,
                           'default': np.mean(LPCMap.WcMap), 'units': 'lbm/s'})
LPCMap.output_data.append({'name': 'effMap', 'values': LPCMap.effMap,
                           'default': np.mean(LPCMap.effMap), 'units': None})
LPCMap.output_data.append({'name': 'PRmap', 'values': LPCMap.PRmap,
                           'default': 1.8, 'units': None})

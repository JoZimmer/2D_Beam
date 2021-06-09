import numpy as np 
from scipy import linalg
# import utilities
# from  postprocess import Postprocess
# import os.path
import global_definitions as GD
import matplotlib.pyplot as plt
from plot_settings import plot_settings

node4 = np.load('inputs\\dynamic_force_4_nodes.npy')
node61 = np.load('inputs\\dynamic_force_61_nodes.npy')
configs =[node4,node61]
nodes = [4,61]

# load_vector = np.zeros(self.n_nodes*self.n_dofs_node)
# dyn_load = np.load(self.parameters['dynamic_load_file'])
for direction in GD.dof_lables['3D']:
    sums = []
    sumsum = []
    fig = plt.figure(figsize=(4,3))
    for i, config in enumerate(configs):
        id_n = GD.dof_lables['3D'].index(direction)
        load_vector = config[id_n::GD.n_dofs_node['3D']]
        mean_load = np.apply_along_axis(np.mean, 1, load_vector)
        sum_load = np.apply_along_axis(sum, 1, load_vector)
        sum_mean = sum(mean_load)
        sumsum.append(sum(sum_load))
        sums.append(sum_mean)
        plt.plot(mean_load, np.linspace(0,180,len(mean_load)), label = direction + ' config' + str(i) + ' sum mean: '+ str(round(sum_mean)))
    plt.plot(0,0,linestyle='None', label = 'sum of means: '+ str(sums[1] - sums[0]))
    plt.plot(0,0,linestyle='None', label = 'sum of sums: ' + str(sumsum[1] - sumsum[0]))
    plt.legend()
    plt.show()


# load_vector = np.apply_along_axis(np.mean, 1, dyn_load)
# else:
#     dir_id = 
#     mean_load = np.apply_along_axis(np.mean, 1, dyn_load)]
#     load_vector[dir_id::GD.n_dofs_node['3D']] = mean_load

# for i in range(6):GD.n_dofs_node['3D']*self.n_nodes
#     plt.plot(mean_load[i:len(mean_load):6], np.arange(len(mean_load)/6), label= GD.dof_lables['3D'][i])
# plt.plot(mean_load, np.arange(len(mean_load)))
# plt.legend()
# plt.show()
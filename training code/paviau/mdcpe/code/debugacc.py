import numpy as np
import scipy.io as sio
# unlabeled_sets = np.load('/home/asdf/Documents/juyan/paper/data/salinas/rnn/unlabeled_index.npy')
# labeled_sets = np.load('/home/asdf/Documents/juyan/paper/data/salinas/rnn/labeled_index.npy')
# # # mat_gt = sio.loadmat('/home/asdf/Documents/juyan/paper/data/salinas/cnn/Salinas_gt.mat')
# # GT = mat_gt['salinas_gt']
# print("ok")
#
# a = np.load("/home/asdf/Documents/juyan/paper/salinas/mdcpe_result/newmdcpe/cnn10.npy")
# b = np.load("/home/asdf/Documents/juyan/paper/salinas/mdcpe_result/newmdcpe/rnn10.npy")
a = np.load("/home/asdf/Documents/juyan/paper/paviau/mdcpe/newmdcpe/model/10_rnn/zhibiao0514.npz")
oa = a["every_class"]
print("ok")
from kurma.structure_order import pdf
import importlib
importlib.reload(pdf)
import numpy as np
import importlib
import matplotlib.pyplot as plt

P = pdf.PDF('./examples/0.1_300.dump', dim=2, fn=[1])

P.make_pdf(atoms=[[1], [2]])
P.make_pdf(atoms=[None, None])

leg_prop = {'loc': 1, 'bbox_to_anchor': [0.9, 0.9]}
fig, ax = plt.subplots(1,1)
P.plot('1-2', 'PDF', 'b-', label='1-2', leg_prop=leg_prop, ax=ax, mean=True, shift=5)
P.plot('all-all', 'PDF', 'r-', label='all', leg_prop=leg_prop, ax=ax, mean=True,)

plt.xlabel('Distance, r ($\AA$)')
plt.ylabel('Pair distribution function (PDF)')
plt.legend()
plt.show()


leg_prop = {'loc': 1, 'bbox_to_anchor': [0.9, 0.9]}
fig, ax = plt.subplots(1,1)
P.plot('1-2', 'TCF', 'b-', label='1-2', leg_prop=leg_prop, ax=ax, mean=True, shift=5)
P.plot('all-all', 'TCF', 'r-', label='all', leg_prop=leg_prop, ax=ax, mean=True,)

plt.xlabel('Distance, r ($\AA$)')
plt.ylabel('Total correlation function (TCF)')
plt.legend()
plt.show()


leg_prop = {'loc': 1, 'bbox_to_anchor': [0.9, 0.9]}
fig, ax = plt.subplots(1,1)
P.plot('1-2', 'SQ', 'b-', label='1-2', leg_prop=leg_prop, ax=ax, mean=True, shift=5)
P.plot('all-all', 'SQ', 'r-', label='all', leg_prop=leg_prop, ax=ax, mean=True,)

plt.xlabel('Wave-vector, k ($\AA^{-1})$')
plt.ylabel('Structure factor (SQ)')
plt.legend()
plt.show()



cutoff={'1-2':1.8}
c = P.CN(cutoff, frame_index=[0], default=1.8)

leg_prop = {'loc': 1, 'bbox_to_anchor': [0.9, 0.9]}
fig, ax = plt.subplots(1,1)
P.plot_bond_angles([[1,2,1],[2,1,2]], ax=ax, label=r'1-2-1')
plt.xticks(range(0,190,30))
plt.xlabel('Bond angle, ($\AA$)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

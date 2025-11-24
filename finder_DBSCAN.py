# github: https://github.com/verzep/finder_code

# python3 --version
# pip3 --version
# pip3 install --upgrade pip
# pip3 install glob2
# pip install numpy==1.22.4
# pip install pandas
# pip install finder_smlm
#

from finder import Finder
import numpy as np
import pandas as pd
import csv
import glob


'''
threshold: int, default = 10. The default value for the `threshold` value, also called `minPts`
points_per_dimension: the number of values for each of the two axis  (`threshold` and `sigma`) of the phase space.
algo: str, default="DbscanLoop" the algorithm to be used. Can be either "dbscan" or "Dbscanloop" todo: fix the capital D
minmax_threshold: list, default = [3,30], The minimum and maximum values for the "threshold" parameter.
log_thresholds: Bool, default = 'False'
log_sigmas: Bool, default = 'True'
decay: float, default = 0.5, The value used to select the selected parameters.

'''

path = "/Users/feizhao/Downloads/test/*.csv"
filename_result = []
for fname in glob.glob(path):
    print(fname)
    export_particles = pd.read_csv(fname, sep = ',', header = 0)
    #print (export_particles)
    loc_xyz = export_particles[['x', 'y', 'z']]
    FD = Finder(algo="dbscan", minmax_threshold=[3,30], log_sigmas=True, log_thresholds=False)
    labels = FD.fit(loc_xyz)
    result = FD.selected_parameters
    print(result)
    Finder.plotPhaseSpace(FD)
    eps_minPts = pd.DataFrame(result, index=[0])
    eps_minPts['filename'] = fname
    filename_result.append(eps_minPts)
filename_result = pd.concat(filename_result)
filename_result.to_csv("/Users/feizhao/Downloads/fname_eps_minPts_test.csv")





    
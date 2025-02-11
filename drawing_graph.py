import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time

base_path = "./runs/detect/"
case_list = [name for name in os.listdir(base_path) if 'RE' in name]

for case in case_list:
    temp_csv = pd.read_csv(f"{base_path}{case}/predictions.csv")
    ins2 = []
    p4p = []
    frame = {}
    temp_csv.columns = ['frame_num', 'video_name', 'drone', 'confidence']
    length = temp_csv.loc[len(temp_csv)-1, 'frame_num']

    for i in range(length):
        temp_slicing = temp_csv[temp_csv['frame_num']==i]
        if temp_slicing.empty:
            ins2.append(0)
            p4p.append(0)
        else:
            ins2_slicing = temp_slicing[temp_slicing['drone']=='Ins2']
            p4p_slicing = temp_slicing[temp_slicing['drone']=='P4P']
            
            if len(ins2_slicing) == 1:
                ins2.append(float(ins2_slicing.iloc[0, 3]))
            else:
                ins2.append(0)
            
            if len(p4p_slicing) == 1:
                p4p.append(float(p4p_slicing.iloc[0, 3]))
            else:
                p4p.append(0)

    ax = np.linspace(0, len(ins2), len(ins2))
    ins2_zero = []
    p4p_zero = []
    ins2_zero_ax = []
    p4p_zero_ax = []
   
    ins2_non_zero = []
    ins2_non_zero_ax = []
    p4p_non_zero = []
    p4p_non_zero_ax = []

    for i in range(len(ins2)):
        if ins2[i] == 0:
            ins2_zero.append(0)
            ins2_zero_ax.append(i)
            ins2_non_zero.append(np.nan)
            ins2_non_zero_ax.append(i)
        else:
            ins2_non_zero.append(ins2[i])
            ins2_non_zero_ax.append(i)
        if p4p[i] == 0:
            p4p_zero.append(0)
            p4p_zero_ax.append(i)
            p4p_non_zero.append(np.nan)
            p4p_non_zero_ax.append(i)
        else:
            p4p_non_zero.append(p4p[i])
            p4p_non_zero_ax.append(i)
    
    

    plt.figure(figsize=(25,9))
    plt.plot(ins2_non_zero_ax, ins2_non_zero, label="confidence")
    plt.scatter(ins2_zero_ax, ins2_zero, label="Not found", c='r', s=1)
    plt.title("Ins2 confidence plot")
    plt.legend()
    plt.savefig(f"{base_path}{case}/Ins2_figure.png")
    plt.close()

    plt.figure(figsize=(25,9))
    plt.plot(p4p_non_zero_ax, p4p_non_zero, label="confidence")
    plt.scatter(p4p_zero_ax, p4p_zero, label="Not found", c='r', s=1)
    plt.legend()
    plt.title("P4P confidence plot")
    plt.savefig(f"{base_path}{case}/P4P_figure.png")
    plt.close()

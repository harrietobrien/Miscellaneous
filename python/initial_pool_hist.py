#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:58:47 2018

@author: harrietobrien
"""
import matplotlib
import matplotlib.pyplot as plt
import os
import json

def load_dict(filename):
    with open(filename,'r') as f:
        loaded_dict = json.load(f)
    return(loaded_dict)
    
def prepare_value_from_dict(input_dict, key):
    '''
    Returns a list of all values from the key of each member in the input_dict 
    '''
    value = []
    for member in input_dict:
        value.append(input_dict[member][key])
    return(value)

def plot_hist(value, bins='auto', density=False, 
              ylabel=None, xlabel=None,  
              font_size=18, figure_size=(12,8)):
    '''
    Args:
        bins: bins+1 bin edges are calculated and plotted
        density: If True, the histogram will be normalized
    '''    
    plt.figure(figsize=figure_size)
    plt.hist(value, bins=bins, density=density)
    if ylabel != None:
        plt.ylabel(ylabel)
    if xlabel != None:
        plt.xlabel(xlabel)
    
    font = {'family' : 'normal',
            'weight' : 'normal',
            'size'   : font_size}
    matplotlib.rc('font', **font)
    
    plt.show()
    
def vol(value):
    pass
    
def plot_hist_all_possible(initial_pool, all_possible,
                           bins='auto', density=False, 
                           ylabel=None, xlabel=None, fig_name=None, 
                           font_size=24, figure_size=(16,12)):
    '''
    Args:
        bins: bins+1 bin edges are calculated and plotted
        density: If True, the histogram will be normalized
        all_possible: List of all possible space groups 
    '''    
    font = {'family' : 'normal',
            'weight' : 'normal',
            'size'   : font_size}
    matplotlib.rc('font', **font)
    
    fig = plt.figure(figsize=figure_size)
    ax1 = fig.add_subplot(111)
    bins = max(all_possible) - min(all_possible)+1
    hist2 = plt.hist(all_possible, bins=bins, density=density, alpha=0.33,
                     color='palevioletred')
    ax1.yaxis.tick_right()
    ax1.yaxis.set_label_position('right')
    plt.yticks([0,1])
    plt.ylabel('All Possible Space Groups')
    plt.xlabel('Space Group')
    
    (plt.text(37.5,0.5,'Missing Space Groups: \
        [5, 10, 11, 16, 17, 18,\n 19, 25, 26, 27, 28, 30, 75, 76, 77, 78]',
              style='italic', fontsize=10,
        bbox={'facecolor':'red', 'alpha':0.25, 'pad':10}))
    
    ax2 = fig.add_subplot(111, sharex=ax1, frameon=False)
    bins = max(initial_pool) - min(initial_pool) + 1
    hist1 = plt.hist(initial_pool, bins=bins, density=density,color='mediumvioletred')
    plt.ylabel(ylabel)

    if fig_name != None:
        fig.savefig(fig_name)
        
    plt.title('γ-glycine (46 Physical Structures)')
    plt.show()
    
def check_all_possible(space_groups, all_possible):
    missing = []
    for sg in all_possible:
        if sg in space_groups:
            continue
        else:
            missing.append(sg)
    return(missing)

if __name__ == '__main__':
    four_mpc_all_possible = [5, 8, 9, 10, 11, 13, 14, 16, 17, 18, 
                             19, 25, 26, 27, 28, 29, 30, 31, 32, 33, 
                             34, 75, 76, 77, 78, 81]
    filename = '/Users/harrietobrien/Desktop/g_gly_initial_pool_phys_vol.dict'
    key = 'space_group'
    fig_name = 'test.pdf'
    struct_dict = load_dict(filename)
    space_groups = prepare_value_from_dict(struct_dict, key)
    plot_hist_all_possible(space_groups, four_mpc_all_possible, bins=100, 
              density=False, xlabel='Space Group', ylabel='Number of Structures',
              font_size=16, fig_name=fig_name, figure_size=(10,6))
    missing = check_all_possible(space_groups, four_mpc_all_possible)
    print('Missing Space Groups: {}' .format(missing))

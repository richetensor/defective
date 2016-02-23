#!/usr/bin/env python
'''Functions to read stress tensor from output files of various atomistic
(ab initio and MM-FF) programs.

Currently supported:
1. Quantum Espresso (PWscf)
2. GULP 
'''
from __future__ import print_function

import re
import numpy as np

def stress_qe(qe_file):
    '''Extracts final stress tensor from a QE calculation.
    '''
    
    return

def stress_gulp(gulp_file):
    '''Extracts stress tensor from a GULP .gout file.
    '''
    
    # read in the entire contents of a GULP output file
    with open(gulp_file, 'r') as f:
        gulp_lines = f.read()
    
    # Extract components of the stress tensor \sigma_{ij}. Note that the GULP output file
    # does not print the full stress tensor, but rather its six unique components
    # (ie. xx, yy, zz, xy, xz, yz).
    stress_form = re.compile('\s+xx\s+(?P<xx>-?\d+\.\d+)\s+yz\s+(?P<yz>-?\d+\.\d+)\s*\n'+
                             '\s+yy\s+(?P<yy>-?\d+\.\d+)\s+xz\s+(?P<xz>-?\d+\.\d+)\s*\n'+
                             '\s+zz\s+(?P<zz>-?\d+)\.\d+\s+xy\s+(?P<xy>-?\d+\.\d+)')
    components = stress_form.search(gulp_lines)
    if not components:
        raise Exception("GULP did not compute the stress tensor.")
    
    # Form the full 3x3 stress tensor
    stress_tensor = np.zeros((3,3))
    
    
    return stress_tensor

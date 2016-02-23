#!/usr/bin/env python
'''Removes the contribution to the ab initio calculated energy due to interactions
between the defect and the stress fields produced by its periodic images. Requires
the <greens_function> and <read_stress> modules.
'''
from __future__ import print_function

import numpy as np

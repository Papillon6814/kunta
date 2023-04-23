"""Main file for exercise"""

import os

from learntools.core import binder

if not os.path.exists("./input/train.csv"):
    os.symlink("./input/home-data-for-ml-course/train.csv", "./input/train.csv")
    os.symlink("./input/home-data-for-ml-course/test.csv", "./input/test.csv")


binder.bind(globals())

from learntools.ml_intermediate.ex1 import *

print("Setup Complete")

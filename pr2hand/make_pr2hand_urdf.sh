#!/bin/bash

rosrun xacro xacro robots/pr2hand.urdf.xacro >pr2hand_for_check.urdf
python3 replace.py pr2hand_for_check.urdf
urdf_to_graphiz pr2hand.urdf
mv pr2hand.pdf pr2hand.gv pdf/

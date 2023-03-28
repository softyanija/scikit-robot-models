#!/bin/bash

rosrun xacro xacro robots/pr2hand.urdf.xacro >pr2hand.urdf
python3 replace.py pr2hand.urdf

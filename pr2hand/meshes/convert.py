import os
import sys
import glob
import bpy


with open('./convertfiles') as f:
    targets = []
    for line in f.readlines():
        targets.append(str(line[:-1]))


for infile in targets:
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    bpy.ops.wm.collada_import(filepath=infile)
    dirname = os.path.dirname(infile)
    filename, ext = os.path.splitext(os.path.basename(infile))
    outfilename = os.path.join(dirname, filename + ".obj")
    bpy.ops.export_scene.obj(filepath=outfilename)

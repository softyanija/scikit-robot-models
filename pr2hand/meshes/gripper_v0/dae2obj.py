import os
import sys
import glob
import bpy

# blender --background --python dae2obj.py -- input_dir output_dir

print(sys.argv, len(sys.argv))
if len(sys.argv) != 9 - 2:
    print("Must provide input and output path")
else:
    for infile in glob.glob(os.path.join(sys.argv[7 - 2], '*.dae')):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        bpy.ops.wm.collada_import(filepath=infile)
        outfilename = os.path.splitext(os.path.split(infile)[1])[0] + ".obj"
        bpy.ops.export_scene.obj(filepath=os.path.join(sys.argv[8 - 2], outfilename))

import bpy 
import mathutils 
import math 
 
# create a cube 
bpy.ops.mesh.primitive_cube_add(size=2) 
 
# get the cube object 
cube_obj = bpy.context.active_object 
 
# set the initial rotation (in radians) 
initial_rotation = (0.0, 0.0, 0.0) 
 
# set the quaternion rotation 
quat_rotation = mathutils.Quaternion((0.707, 0.0, 0.0, 0.707)) 
 
# apply the rotation to the cube object 
cube_obj.rotation_mode = 'QUATERNION' 
cube_obj.rotation_quaternion = quat_rotation 
 
# animate the rotation 
for i in range(1, 61): 
    angle = i * 6 
    quat_rotation = mathutils.Quaternion((0.707, math.sin(math.radians(angle/2)), 0.0, math.cos(math.radians(angle/2)))) 
    cube_obj.rotation_quaternion = quat_rotation 
    cube_obj.keyframe_insert(data_path="rotation_quaternion", frame=i) 

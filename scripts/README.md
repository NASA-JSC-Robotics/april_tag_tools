The scripts were quickly generated to create mujoco friendly apriltag meshes.
They require source images found in the following repo:
https://github.com/AprilRobotics/apriltag-imgs

Expects the source low-res input images for texture creation to be 20% white border and 80% tag on any given row. The format generally of 1px(border) + 8px(tag) + 1px(border).

For the dae creation, we have a source model that is then copied and rewritten with reference to the new texture. Some paths might need updating

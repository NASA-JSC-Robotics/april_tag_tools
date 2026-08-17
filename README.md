# April Tag Tools

This project contains a collection of simple meshes and respective textures for each of the tags in the 36h11 family. 

To add to an urdf, replace the following parent link with the desired link:

```
  <joint name="apriltag_joint" type="fixed">
    <parent link="desired_parent_link"/>
    <child link="apriltag_link"/>
    <origin xyz="0 0 0" rpy="0 0 0"/>
  </joint>

  <link name="apriltag_link">
    <visual>
      <geometry>
        <mesh filename="package://april_tag_tools/36h11/tag36_11_00026.dae"/>
      </geometry>
    </visual>
    <collision>
      <geometry>
        <mesh filename="package://april_tag_tools/36h11/tag36_11_00026.dae"/>
      </geometry>
    </collision>
  </link>
```

## Citation

This project falls under the purview of the iMETRO project.
If you use this in your own work, please cite the following paper:

```bibtex
@INPROCEEDINGS{imetro-facility-2025,
  author={Dunkelberger, Nathan and Sheetz, Emily and Rainen, Connor and Graf, Jodi and Hart, Nikki and Zemler, Emma and Azimi, Shaun},
  booktitle={2025 22nd International Conference on Ubiquitous Robots (UR)},
  title={Design of the iMETRO Facility: A Platform for Intravehicular Space Robotics Research},
  year={2025},
  volume={},
  number={},
  pages={390-397},
  keywords={NASA;Moon;Seals;Maintenance engineering;Maintenance;Robots;Standards;Open source software;Testing;Logistics},
  doi={10.1109/UR65550.2025.11077983}}
```

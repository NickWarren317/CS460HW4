<h1> How to run....</h1>
<p> 1. clone this repo with <strong>git clone https://github.com/NickWarren317/CS460HW4</strong> </p>
<p> 2. run <strong> cd CS460HW4 </strong> <strong> colcon build </strong>
<p> 3. <strong>source /opt/ros/humble/setup.bash </strong></p>
<p> 4. <strong>source install/setup.bash </strong></p>
<p> 5. <strong>ros2 launch CS460HW4 launch.py </strong></p>
<p> 6. open another terminal and run <strong> cd CS460HW4 </strong> <strong> source install/setup.bash </strong> <strong> ros2 run CS460HW4 CS460HW4 </strong></p>


<h1> Algorithm 1.0 </h1>
<p> Simple movement to keep a wall to the turtlebot's right side. This allows it to follow walls where april tags are most likely to be placed.
However, the camera is front facing, therefore not a good angle to scan the tags. Therefore, the bot will periodically stop and do a full rotation to
scan its surroundings for a tag. When one is detected, it is added to a list of found tags if not in the list already, then resumes wall following </p>



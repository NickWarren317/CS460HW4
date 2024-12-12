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

<h1> Maze Starting Positions </h1>
<h3> Tag Pos: translation 1.3761 -4.74474 0.1 rotation 0 0 1 1.57159</h3>
<h2> Pos1 </h2>
<p> Translation 4.89169 2.15746 0.0233213 Rotation 0 0 1 -1.19112</p>
<p> Found tag at 4:02 </p>
<p> Covered 104.41 m^2 41764 open cells</p>

<h2>Pos2</h2>
<p> Translation -2.71765 2.36318 -0.0117626 Rotation 0 0 1 2.21228 </p>
<p>Detected at 1:17</p>
<p>Covered 101.34 m^2 40536 open cells</p>

<h2>Pos3</h2>
<p> Translation 6.56239 -1.62301 0.0335482 Rotation 0 0 1 1.42688</p>
<p>Detected at 5:32</p>
<p>Covered 97.95 m^2, 39180</p>

<h1>Maze2 Positions</h1>
<h3> Tag Pos: Translation -3.36 -1.42 0.15  Rotation 0 0 1 0</h3>

<h2> Pos 1 </h2>
<p> Translation 1.70897 -1.13213 0.00552157  Rotation 0 7.5056 1 3.01561</p>
<p> Did not find :<</p>
<p> Covered: 39.18 m^2 15671 open cells</p>

<h2> Pos 2 </h2>
<p> Translation -0.656104 -1.25687 0.000142121  Rotation 0.0 0.0 1 -2.4920</p>
<p> Found: 3:51</p>
<p> Covered: 40.75 m^2 16303 open cells</p>

<h2> Pos 3 </h2>
<p> Translation 1.73544 1.13133 0.00491471 Rotation 0 0 -1 -0.659</p>
<p> Found </p>
<p> Covered: 38.72 m^2 15490 open cells</p>
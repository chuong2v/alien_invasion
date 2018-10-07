In Alien Invasion, the player controls a ship that appears at
the bottom center of the screen. The player can move the ship
right and left using the arrow keys and shoot bullets using the
spacebar. When the game begins, a fleet of aliens fills the sky
and moves across and down the screen. The player shoots and
destroys the aliens. If the player shoots all the aliens, a new fleet
appears that moves faster than the previous fleet. If any alien hits
the player’s ship or reaches the bottom of the screen, the player
loses a ship. If the player loses three ships, the game ends.

# Set up
~~~shell
python3 -m pip install -U pygame --user
~~~

Test
~~~shell
python
>>> import pygame
~~~

If error:
~~~shell
sudo apt-get install python3-dev mercurial
sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev
~~~

If you want to enable some more advanced functionality in Pygame, such as
the ability to add sounds, you can also add the following libraries:
~~~shell
sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcode-dev
sudo apt-get install python-numpy
~~~

Install Pygame
~~~shell
pip install --user hg+http://bitbucket.org/pygame/pygame
~~~
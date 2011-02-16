import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')



class Settings:
	screen_size = (800, 600) #initial screen size if not in fullscreen mode, but the window will be resizable
	map_size = screen_size
	fullscreen = False
	sounds = True
	show_fps = True
	turning_speed = 3 #how fast spaceship will turn
	spaceship_accel = 0.1

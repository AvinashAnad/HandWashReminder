import time
from appJar import gui
app = gui()

while True:
	app.infoBox("Hand Wash Reminder", "Time to wash your hands", parent=None)
	time.sleep(3600)
	
#!/usr/bin/python3
'''
'!/usr/bin/python3' we keep original python3, to kill all not found gcc folder. because gcc folder in ubuntu is set to /usr/lib/.. and we don't need to change it. 
## TODO find a way to kill this error when using #!/usr/bin/env python: Error: version `GLIBCXX_3.4.29' not found (required by /home/alireza/anaconda3/envs/robot-planner/bin/../lib/libmysqlclient.so.21)

'''
import sys

from PyQt5 import QtWidgets

from eyerobot_ws.src.ui.ui.main_ui import MainUI
from parse_images import parse_images
from splash_screen import SplashScreen


# Starts command and control UI
# Also displays our splash screen
def main():
    print("Medical Autonomy and Precision Surgery Laboratory - Robot Control UI")

    # parse_images()

    app = QtWidgets.QApplication(sys.argv)

    # Build splash screen and UI
    splash_screen = SplashScreen()
    ui = MainUI()
    splash_screen.show()
    app.processEvents()

    # Display splash screen while UI loads
    splash_screen.finish(ui.ui)

    # Display UI
    ui.show()

    # Enter main loop
    app.exec()


if __name__ == '__main__':
    main()

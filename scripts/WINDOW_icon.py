# This code defines a function that changes the application identifier of the current process in Windows

import ctypes

def window_icon() -> None:
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
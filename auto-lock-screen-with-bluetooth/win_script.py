import bluetooth
import ctypes

# Run in background with pythonw
my_device = "Jon Ander" # The name of your bluetooh device
duration = 1 # Time searching the bluetooth devices

def lock_screen():
    """Lock screen computer"""
    ctypes.windll.user32.LockWorkStation()


def is_my_device_in(nearby_devices):
    """ Check if your device is in the nearby_devices list.
        Returns True if the device is found. Return False for anything else """
    for addr, name in nearby_devices:
        if name == my_device:
            return True
        else:
            return False


def searching_my_device():
    """ Search the device """
    # In Windows if there is no nearby devices the function raises an exception
    # We handle the exception an return False like we would not found any device.
    try:
        nearby_devices = bluetooth.discover_devices(duration=duration, 
                                                    lookup_names=True,
                                                    lookup_class=False,
                                                    device_id=0)
        return is_my_device_in(nearby_devices)
    except Exception:
        return False


try: # DEBUG: Handling KEYBOARD INTERRUPT to break the loop
    while(True):
        print "BUCLE"
        if searching_my_device() == False:
            lock_screen()
except KeyboardInterrupt:
    pass
#multi threading e akstathe onno kaj korte parbe
import threading
import time

#indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

func(4)
func(2)
func(1)
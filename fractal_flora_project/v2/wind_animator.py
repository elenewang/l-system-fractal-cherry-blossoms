import math
import time
from threading import Thread

class WindAnimator:
    def __init__(self):
        # Initialize wind parameters
        self.wind_strength = 0
        self.wind_direction = 0
        self.is_animated = True

    def animate_wind(self):
        # Continuously update wind parameters for animation
        while self.is_animated:
            # Create naturally varying wind patterns
            self.wind_strength = 0.5 * math.sin(time.time() * 0.5) + \
                                 0.3 * math.sin(time.time() * 0.7) + \
                                 0.2 * math.sin(time.time() * 1.1)
            self.wind_direction = 20 * math.sin(time.time() * 0.3)
            ''' 
            pauses the execution of the method for 16 milliseconds, which ensures that 
            the wind parameters are updated at a consistent rate, creating a smooth animation.
            '''
            time.sleep(0.016)

    def start(self):
        # Start wind animation in a separate thread
        wind_thread = Thread(target=self.animate_wind)
        wind_thread.daemon = True
        wind_thread.start()

    def stop(self):
        # Stop wind animation
        self.is_animated = False
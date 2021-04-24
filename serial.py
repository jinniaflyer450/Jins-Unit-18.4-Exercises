"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Initializes a serial generator with a starting number (the number that the first increment results in) of start."""
        self.start=start
        self.current=start-1

    def generate(self):
        """Increments a serial generator's current value by one."""
        self.current+=1
        return self.current
    
    def reset(self):
        """Resets a serial generator's current value to one below its starting value (so that the number the first increment results in is its starting value)."""
        self.current=self.start-1
class Bird:
    def fly(self):
        print('Birds flies in the sky')
        
        
class Eagle(Bird):
    def fly(self):
        print('Eagle flies at a high altitude')
        
class   Sparrow(Bird):
    def fly(self):
        print('Sparrow flies at a low altitude')
        
def flight_test(bird):
    bird.fly()    
    
# Create instances of Eagle and Sparrow
eagle1 = Eagle()
sparrow1 = Sparrow()

# Test the flight method for both birds
flight_test(eagle1)    # Output: Eagle flies at a high altitude
flight_test(sparrow1)  # Output: Sparrow flies at a low altitude

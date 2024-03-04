import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM) 
segments = [4, 17, 18, 27, 22, 23, 24]
digits = [25, 21]
digit_code = [ [0, 0, 0, 0, 0, 0, 1],
	       [1, 0, 0, 1, 1, 1, 1],
	       [0, 0, 1, 0, 0, 1, 0],
	       [0, 0, 0, 0, 1, 1, 0],
	       [1, 0, 0, 1, 1, 0, 0],
	       [0, 1, 0, 0, 1, 0, 0],
	       [0, 1, 0, 0, 0, 0, 0],
	       [0, 0, 0, 1, 1, 1, 1],
	       [0, 0, 0, 0, 0 ,0, 0],
	       [0, 0, 0, 0, 1, 0, 0] ]

for segment in segments:
   GPIO.setup(segment, GPIO.OUT)
   GPIO.output(segment, GPIO.LOW)
for digit in digits:
   GPIO.setup(digit, GPIO.OUT)
   GPIO.output(digit, GPIO.LOW)
      

def display(number):
   for i in range(7):
      GPIO.output(segments[i], digit_code[number][i])
      #time.sleep(0.05)
   
 
def display_2(number):
   a = number//10
   b = i%10
   for i in range(50):
      if (i%2 == 1):
	 GPIO.output(digits[0], GPIO.HIGH)
	 GPIO.output(digits[1], GPIO.LOW)
	 display(a)
      else:
	 GPIO.output(digits[0], GPIO.LOW)
	 GPIO.output(digits[1], GPIO.HIGH)
	 display(b)
      
      
 
 
while True:
   for i in range(10, 100):
      display_2(i)

if __name__ == "__main__":
    main()
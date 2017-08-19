def main():
  import time
  from LED import LED_C as LED_NO
  Motor = LED_NO(11)
  
  while True:
    Motor.ON()
    time.sleep(2)
    Motor.OFF()
    time.sleep(2)
    
  
if __name__ == '__main__':
main()

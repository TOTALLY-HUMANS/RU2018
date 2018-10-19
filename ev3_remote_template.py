import rpyc
from rpyc.utils.server import ThreadedServer
from ev3dev2.led import Leds

class RobotService(rpyc.Service):
    def exposed_speak_message(self, msg):
        leds = Leds()
        led_colour_left = "AMBER"
        led_colour_right = "RED"

        leds.all_off() # Turn all LEDs off
        sleep(1)

        # Set both pairs of LEDs to amber
        leds.set_color('LEFT', led_colour_left)
        print("\nLED color set to " + led_colour_left)
        leds.set_color('RIGHT', led_colour_right)
        print("\nLED color set to " + led_colour_right)
        sleep(4)

if __name__ == '__main__':
    s = ThreadedServer(RobotService, port=18812)
    s.start()

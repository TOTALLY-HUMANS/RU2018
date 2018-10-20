from robot_behaviour_thread import RobotBehaviourThread
import time

class LineFollower(RobotBehaviourThread):
    turning = 0
    started_turning = time.time()

    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting line follower...")
        straight = 0
        left = -90
        right = 90
        
        turnTimer = 1
        turnSpeed = 30
        moveSpeed = 60

        first_turn = left

        while not self.stopped():
            if self.line_found():
                if self.turning == left:
                    first_turn = left
                elif self.turning == right:
                    first_turn = right

                self.move(straight, moveSpeed)
                self.set_turning_to(straight)
            elif self.red_found():
                time.sleep(1)
                self.move(0, -moveSpeed)
                time.sleep(3)
                self.move(left, turnSpeed)
                time.sleep(1)
            elif (not self.turning == -first_turn) and (self.turning == straight or (time.time() - self.started_turning) <= turnTimer):
                self.move(first_turn, turnSpeed)
                self.set_turning_to(first_turn)
            else:
                self.move(-first_turn, turnSpeed)
                self.set_turning_to(-first_turn)
        self.callback("Forest Crawler")

    def set_turning_to(self, turn):
        if self.turning != turn:
            self.turning = turn
            self.started_turning = time.time()
    
    def line_found(self):
        self.color_sensor.mode = 'COL-REFLECT'
        return self.color_sensor.reflected_light_intensity > 30
        
    def yellow_found(self):
        self.color_sensor.mode = 'COL-COLOR'
        return self.color_sensor.value() == 4
        
    def red_found(self):
        self.color_sensor.mode = 'COL-COLOR'
        return self.color_sensor.value() == 5

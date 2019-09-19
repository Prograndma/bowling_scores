import numpy as np


class Player():
    def __init__(self, name=None, frame_number=1, previous=None):
        self.points = []
        self.name = name
        self.frame_number = frame_number
        self.is_tenth = self.frame_number == 10
        self.previous = previous
        if self.frame_number < 11:
            self.next_frame = Player(name, frame_number + 1, previous=self)
        self.strike = False
        self.spare = False

    def is_turn_over(self, points):
        self.points.append(points)
        if self.is_tenth:
            return self.tenth_logic()
        else:
            return self.normal_logic()

    def get_first_frame(self):
        if self.frame_number != 1:
            return self.previous.get_first_frame()
        else:
            return self

    def print_scores(self):
        frame = self.get_first_frame()
        total_points = 0
        while frame.frame_number <= 10:
            points = frame.get_frame_points()
            if points is None:
                points = 0
            total_points += points
            print(f"Frame: {frame.frame_number}{frame.points}")
            print(total_points)
            frame = frame.next_frame

    def get_frame_points(self):
        if not self.points:
            return None
        sum_points = np.sum(self.points)

        if self.strike or self.spare:
            try:
                sum_points += self.get_second_point()
            except:
                return None

        if self.strike:
            try:
                sum_points += self.get_third_point()
            except:
                return None
        return sum_points

    def normal_logic(self):
        sum = np.sum(self.points)
        num_attempts = len(self.points)
        if sum == 10 and num_attempts == 1:
            self.strike = True
            return True
        if sum == 10:
            self.spare = True
            return True
        if num_attempts == 2:
            return True
        else:
            return False

    def tenth_logic(self):
        num_attempts = len(self.points)
        if num_attempts == 1:
            return False
        if num_attempts == 3:
            return True

        # num_attempts must be 2. If sum >= 10 => spare or Strike turn still goin
        if np.sum(self.points) >= 10:
            return False
        self.points.append(0)
        return True

    def get_first_point(self):
        return self.points[0]

    def get_second_point(self):
        if self.strike:
            return self.next_frame.get_first_point()
        return self.points[1]

    def get_third_point(self):
        if self.is_tenth:
            return self.points[2]
        if self.strike:
            return self.next_frame.get_second_point()
        else:
            return self.next_frame.get_first_point()

    def get_previous(self):
        return self.previous
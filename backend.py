import math
from datetime import datetime

class HealthTracker:
    def __init__(self):
        self.initialized = False
        self.name = ""
        self.age = ""
        self.gender = ""
        self.height = ""
        self.weight = ""
        self.calorie_target = ""
        
        self.calorie_count = 0
        self.calorie_intake = {}
        self.calorie_burnt = {}
        self.calorie_track = {}

        self.bp_track = {}
        self.sugar_track = {}

        self.BP_TRACK_LIST_NAME = "bp_track"
        self.SUGAR_TRACK_LIST_NAME = "sugar_track"
        self.CALORIE_TRACK_LIST_NAME = "calorie_track"
    
    def init_profile(self, name, age, gender, height, weight, calorie_target):
        self.name = name
        self.age = age
        assert type(age) is int
        self.gender = gender
        self.height = height
        assert type(height) is int
        self.weight = weight
        assert type(weight) is int
        self.calorie_target = calorie_target
        assert type(calorie_target) is int
        assert calorie_target > 0
        self.initialized = True

    def update_tracklist(self, list_name, value):
        time_now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not self.initialized:
            return
        if list_name == self.BP_TRACK_LIST_NAME:
            self.bp_track[time_now_str] = value
        elif list_name == self.SUGAR_TRACK_LIST_NAME:
            if value <= 0:
                return
            self.sugar_track[time_now_str] = value
        elif list_name == self.CALORIE_TRACK_LIST_NAME:
            if value == 0:
                return
            self.calorie_count += value
            self.calorie_track[time_now_str] = self.calorie_count

            if value < 0:
                self.calorie_burnt[time_now_str] = abs(value)
            else:
                self.calorie_intake[time_now_str] = value
        print(self.calorie_track, self.calorie_burnt, self.calorie_intake)

    def get_bmi(self):
        if not self.initialized:
            return
        bmi = self.weight / math.pow(self.height/100, 2)
        return bmi
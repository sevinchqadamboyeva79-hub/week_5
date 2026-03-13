class Running:
    def  calories_burned(self,minutes):
        return minutes*10
class Yoga:
    def calories_burned(self,minutes):
        return minutes*4
def workout_summary(workout, minutes):
    amount=workout.calories_burned(minutes)
    print  (f"Burned {amount} calories in {minutes} minutes.")
run = Running()
yoga = Yoga()

workout_summary(run, 30)
workout_summary(yoga, 45)
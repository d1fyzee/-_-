class Motion:
    def __init__(self, speed, time_minutes):
        self.speed = float(speed)
        self.time_minutes = int(time_minutes)

    @classmethod

    def copy(cls, drugie):
        return cls(drugie.speed, drugie.time_minutes)

    def zadnie(self):
        time_seconds = self.time_minutes * 60
        plo = self.speed * time_seconds
        return plo

    def __str__(self):
        plo = self.zadnie()
        return (f"Движение:\n"
                f"  Скорость: {self.speed} м/с\n"
                f"  Время: {self.time_minutes} мин\n"
                f"  Пройденное расстояние: {plo} м")

if __name__ == "__main__":
    motion1 = Motion(5.5, 10)
    print("Объект 1:")
    print(motion1)
    print()

    motion2 = Motion.copy(motion1)
    print("Копия объекта 1:")
    print(motion2)
    print()

    motion3 = Motion(2.0, 30)
    print("Объект 3:")
    print(motion3)
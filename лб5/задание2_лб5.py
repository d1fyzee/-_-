class Motion:
    def __init__(self, speed, time_minutes):
        self.speed = float(speed)
        self.time_minutes = float(time_minutes)

    @classmethod
    def copy(cls, other):
        return cls(other.speed, other.time_minutes)

    def calculate_distance(self):
        # s = v * t
        time_seconds = self.time_minutes * 60
        return self.speed * time_seconds

    def __str__(self):
        return (
            f"Движение:\n"
            f"  Скорость: {self.speed} м/с\n"
            f"  Время: {self.time_minutes} мин\n"
            f"  Пройденное расстояние: {self.calculate_distance()} м"
        )


class DynamicMotion(Motion):
    def __init__(self, speed, time_minutes, mass):
        super().__init__(speed, time_minutes)
        self.mass = float(mass)

    def calculate_force(self):
        # F = m * a, a = v / t (движение из состояния покоя)
        time_seconds = self.time_minutes * 60
        if time_seconds == 0:
            return 0.0
        acceleration = self.speed / time_seconds
        return self.mass * acceleration

    def calculate_work(self):
        # A = F * s
        return self.calculate_force() * self.calculate_distance()

    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"  Масса: {self.mass} кг\n"
            f"  Сила, приложенная к объекту: {self.calculate_force()} Н\n"
            f"  Количество выполненной работы: {self.calculate_work()} Дж"
        )


if __name__ == "__main__":
    obj = DynamicMotion(speed=12, time_minutes=2, mass=5)
    print(obj)

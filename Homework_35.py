from threading import Thread, Lock
import time

lock = Lock()


class Knight(Thread):

    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill
        self.day = 0
        self.enemies = 100

    def run(self):
        print(f'{self.name} на нас напали!')
        while self.enemies != 0:
            lock.acquire()
            self.day += 1
            self.enemies -= self.skill
            time.sleep(1)
            lock.release()
            print(f'{self.name} сражается {self.day} день(дня)..., осталось {self.enemies} войнов. ')

        print(f'{self.name} одержал победу спустя {self.day} дней!')


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения

knight1.start()
knight2.start()

knight1.join()
knight2.join()
print(f'Все битвы закончились!')

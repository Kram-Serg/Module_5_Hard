import time
import hashlib
class User:
    def __init__(self,nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def get_list_nickname(self):
        list_nicknames = []
        for users in self.users:
            list_nicknames.append(users.nickname)
        return list_nicknames

    def get_list_titles(self):
        list_titles = []
        for video in self.videos:
            list_titles.append(video.title)
        return list_titles
    def register(self, nickname, password, age):
        hash_password = hashlib.sha224(password.encode('utf-8')).digest()
        temp_us = User(nickname, hash_password, age)
        if nickname not in self.get_list_nickname():
            self.users.append(temp_us)
            self.log_out()
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_in(self, nickname, password):
        hash_password = hashlib.sha224(password.encode('utf-8')).digest()
        for user in self.users:
            if user.nickname == nickname and user.password == hash_password:
                self.current_user = user
    def log_out(self):
        self.current_user = None

    def add(self, *new_videos):
        for new_video in new_videos:
            if new_video.title not in self.get_list_titles():
                self.videos.append(new_video)

    def get_videos(self, search_word):
        found_videos = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                found_videos.append(video.title)
            return found_videos
    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if title == video.title:
                    if video.adult_mode and self.current_user.age<18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        for t in range(video.time_now+1, video.duration):
                            print(t)
                            video.time_now = t
                            time.sleep(1)
                        print('Конец видео')
                        video.time_now = 0


if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
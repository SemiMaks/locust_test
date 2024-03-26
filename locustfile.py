# Пример использования TaskSets/Вложенные наборы задач

from locust import HttpUser, TaskSet, task, between


class ForumThread(TaskSet):
    pass


class ForumPage(TaskSet):
    # диапазон времени может быть задан индивидуально в TaskSets
    wait_time = between(10, 300)

    # TaskSets может иметь несколько уровней вложенности
    tasks = {
        ForumThread: 3
    }

    @task(3)
    def forum_index(self):
        pass

    @task(1)
    def stop(self):
        self.interrupt()


class AboutPage(TaskSet):
    pass


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    # в подднаборах задач можно импользовать dict/словарь
    tasks = {
        ForumPage: 20,
        AboutPage: 10,
    }

    # Можно мсользовать @task декоратор а так же
    # задачи в словаре Locust/TaskSet
    @task(10)
    def index(self):
        pass
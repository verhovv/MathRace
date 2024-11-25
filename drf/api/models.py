from django.db import models


class Car(models.Model):
    mmr_bound = models.IntegerField()
    image_path = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.mmr_bound} - {self.image_path}'


class User(models.Model):
    username = models.CharField(max_length=18, unique=True)
    password_hash = models.CharField(max_length=255)
    mmr = models.IntegerField(default=0)

    task_index = models.IntegerField(default=1)

    def __str__(self):
        return self.username


class Room(models.Model):
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first_user')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='second_user')
    task_count = models.IntegerField()

    def __str__(self):
        return f'{self.first_user} - {self.second_user}'


class RoomTasks(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    number = models.IntegerField()

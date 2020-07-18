from django.db import models
from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import post_save


class Building(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Level(models.Model):
	name = models.CharField(max_length=200)
	building = models.ForeignKey(Building, on_delete=models.CASCADE)
	level_code = models.CharField(max_length=5)
	alias = models.CharField(max_length=10)

	def __str__(self):
		return f"{self.alias}{self.level_code}: {self.name}"


class Room(models.Model):
	user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
	name = models.CharField(max_length=200)
	level = models.ForeignKey(Level, on_delete=models.PROTECT)

	booking_type_choices = (
		('meeting', 'For a meeting'),
		('event', 'For an event'),
	)
	booking_type = models.CharField(max_length=20, choices=booking_type_choices,
		default=booking_type_choices[0])

	address = models.CharField(max_length=200)
	link = models.URLField()
	book_start_date = models.DateField()
	book_end_date = models.DateField()
	book_start_time = models.TimeField()
	book_end_time = models.TimeField()
	what_to_bring = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.name





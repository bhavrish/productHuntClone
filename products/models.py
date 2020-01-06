from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
	title = models.CharField(max_length=255)
	url = models.TextField()
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/')
	body = models.TextField()
	votes_total = models.IntegerField(default=1)
	hunter = models.ForeignKey(User, on_delete=models.CASCADE) # stores userID by using foreign key to user model. models.CASCADE deletes post if user is deleted


	def __str__(self): # in the admin panel, instead of saying Products(0), Products(1), it says the title of the blogs instead
		return self.title

	def summary(self):
		return self.body[:100]+'...'

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')
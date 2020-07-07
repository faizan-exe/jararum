from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class directMessage(models.Model):

	message_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	message_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

	date_posted = models.DateTimeField(default=timezone.now)

	text = models.TextField()

	template_name = 'directMessage/create_message.html'

	def __str__(self):
		return f'{self.message_from} -- {self.message_to}'

	def get_absolute_url(self):
	    return reverse('profile_view', kwargs={'name': self.message_to})

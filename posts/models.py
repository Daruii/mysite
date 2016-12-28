from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
	title=models.CharField (u'Заголовок', max_length=150)
	content=models.TextField (u'Текст сообщения')
	timestamp=models.DateTimeField(u'Дата создания', auto_now_add=True)
	updated=models.DateTimeField(u'Дата изменения', auto_now=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	class Meta:
		verbose_name=u'Запись'
		verbose_name_plural=u'Записи'


from datetime import date

from django.conf import settings
from django.db import models

STATUS = (
    ('RE','Requested'),
    ('PR','Enabled'),
    ('DD','Disabled'),
)


class CompsocUser(models.Model):
    nickname = models.CharField(max_length=50, blank=True, default='')

    website_url = models.CharField(max_length=50, blank=True, default='')
    website_title = models.CharField(max_length=50, blank=True, default='')

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def is_fresher(self):
        return self.user.username.startswith("%02d".format(date.today().year - 2000))

    def name(self):
        if self.nickname.strip():
            return self.nickname.strip()
        else:
            return self.user.get_full_name()


class ShellAccount(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=2, choices=STATUS)

    def __str__(self):
        return self.name


class DatabaseAccount(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=2, choices=STATUS)

    def __str__(self):
        return self.name


class ExecPosition(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class ExecPlacement(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    position = models.ForeignKey(ExecPosition)
    start = models.DateField()
    end = models.DateField()

    class Meta:
        ordering = ['start']

    def __str__(self):
        return "{start}/{end} - {pos}".format(start=self.start.year, end=self.end.year,
                                              pos=self.position)
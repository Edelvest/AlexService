from django.contrib.auth.models import User
from django.db import models

VIRTUAL = 'VM'
DEDICATED = 'DS'
SERVER_TYPE = (
    (VIRTUAL, 'Virtual'),
    (DEDICATED, 'Dedicated'),
)


class Server(models.Model):
    name = models.CharField(max_length=100, verbose_name='Server name')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(verbose_name='Server description')
    create_dt = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    server_type = models.CharField(max_length=2, choices=SERVER_TYPE, verbose_name='Server type')

    def __str__(self):
        return self.name


class ServerIP(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, verbose_name='Server')
    ip = models.CharField(max_length=50, verbose_name='ip address', unique=True)

    def __str__(self):
        return self.ip

from django.db import models


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(
        'List', on_delete=models.CASCADE, related_name='item_list')


class List(models.Model):
    pass

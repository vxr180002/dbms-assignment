from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Contacts(models.Model):
    def __str__(self):
        return self.first_name

    contact_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200)
    home_phone = models.CharField(max_length=200, null=True, blank=True)
    cell_phone = models.CharField(max_length=200, null=True, blank=True)
    home_address = models.CharField(max_length=200, null=True, blank=True)
    home_city = models.CharField(max_length=200, null=True, blank=True)
    home_state = models.CharField(max_length=200, null=True, blank=True)
    home_zip = models.CharField(max_length=200, null=True, blank=True)
    work_phone = models.CharField(max_length=200, null=True, blank=True)
    work_address = models.CharField(max_length=200, null=True, blank=True)
    work_city = models.CharField(max_length=200, null=True, blank=True)
    work_state = models.CharField(max_length=200, null=True, blank=True)
    work_zip = models.CharField(max_length=200, null=True, blank=True)
    birth_date = models.CharField(max_length=200, null=True, blank=True)

class address(models.Model):
    def __str__(self):
        return self.address_id

    address_id = models.AutoField(primary_key=True)
    contact_id = models.ForeignKey(
        'Contacts',
        on_delete=models.CASCADE,
    )
    address_type = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zip = models.CharField(max_length=200, null=True, blank=True)

import django_tables2 as tables

class SimpleTable(tables.Table):
    class Meta:
        model = address

class phone(models.Model):
    def __str__(self):
        return self.phone_id

    phone_id = models.AutoField(primary_key=True)
    contact_id = models.ForeignKey(
        'Contacts',
        on_delete=models.CASCADE,
    )
    phone_type = models.CharField(max_length=200, null=True, blank=True)
    area_code = models.CharField(max_length=200, null=True, blank=True)
    number = models.CharField(max_length=200, null=True, blank=True)

class date(models.Model):
    def __str__(self):
        return self.date_id

    date_id = models.AutoField(primary_key=True)
    contact_id = models.ForeignKey(
        'Contacts',
        on_delete=models.CASCADE,
    )
    date_type = models.CharField(max_length=200, null=True, blank=True)
    date = models.CharField(max_length=200, null=True, blank=True)
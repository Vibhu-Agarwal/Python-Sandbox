from django.db import models


class Company(models.Model):
    pass


class Developer(models.Model):
    skills = models.CharField(max_length=20)
    # https://devdocs.io/django~3.0/topics/db/models#abstract-related-name
    work = models.ForeignKey(Company, on_delete=models.SET_NULL,
                             related_name='%(class)s',
                             blank=True, null=True)

    class Meta:
        abstract = True


class WebDeveloper(Developer):
    front_end_skills = models.PositiveSmallIntegerField()
    back_end_skills = models.PositiveSmallIntegerField()


class MobileDeveloper(Developer):
    knows_java = models.BinaryField()

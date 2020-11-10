from django.db import models
from django.contrib.auth import get_user_model

from django.db.models.signals import m2m_changed
from django.dispatch import receiver

User = get_user_model()


class ProjectRick(models.Model):
    name = models.CharField(max_length=20)
    admin_users = models.ManyToManyField(User, related_name='admin_rick_projects', blank=True)
    users = models.ManyToManyField(User, related_name='rick_projects', blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(ProjectRick, self).save(force_insert=False, force_update=False, using=None,
                                      update_fields=None)
        for admin in self.admin_users.all():
            if not self.users.filter(pk=admin.id).exists():
                self.users.add(admin)


class ProjectMorty(models.Model):
    name = models.CharField(max_length=20)
    admin_users = models.ManyToManyField(User, related_name='admin_morty_projects', blank=True)
    users = models.ManyToManyField(User, related_name='morty_projects', blank=True)


@receiver(m2m_changed, sender=ProjectMorty.admin_users.through)
def update_users_on_change(instance, action, **kwargs):
    if action == 'post_add':
        instance.name = f"{instance.name}_changed"  # changes to this field are reflected in DB
        instance.save()
        users = instance.users.all()
        for admin in instance.admin_users.all():
            if not users.filter(pk=admin.id).exists():
                instance.users.add(admin)

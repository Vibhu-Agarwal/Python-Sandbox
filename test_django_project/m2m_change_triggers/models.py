from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

User = get_user_model()


class Project(models.Model):
    name = models.CharField(max_length=20)
    admin_users = models.ManyToManyField(User, related_name='admin_morty_projects', blank=True)
    users = models.ManyToManyField(User, related_name='morty_projects', blank=True)


@receiver(m2m_changed, sender=Project.admin_users.through)
def update_users_on_change(instance, action, **kwargs):
    if action == 'post_add':
        for admin in instance.admin_users.all():
            if not instance.users.filter(pk=admin.id).exists():
                instance.users.add(admin)

        # instance.users.add(*instance.admin_users.all())
        # instance.users.set(instance.users.distinct())

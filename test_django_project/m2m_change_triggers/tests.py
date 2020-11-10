from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.serializers import ModelSerializer

from .models import Project

User = get_user_model()


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class TestProject(TestCase):

    def setUp(self) -> None:
        project_data = {
            'name': 'Project RnM'
        }
        users = [
            {
                'username': 'vibhu',
                'email': 'vibhu@vibhu.in',
                'first_name': 'Vibhu',
                'phone_number': '+999999999',
                'password': 'password'
            },
            {
                'username': 'guido',
                'email': 'guido@guido.in',
                'first_name': 'Guido',
                'phone_number': '+999999999',
                'password': 'password'
            },
            {
                'username': 'david',
                'email': 'david@david.in',
                'first_name': 'David',
                'phone_number': '+999999999',
                'password': 'password'
            }
        ]
        self.users = (
            User.objects.create(**users[0]),
            User.objects.create(**users[1]),
            User.objects.create(**users[2]),
        )
        self.project = Project.objects.create(**project_data)
        self.project.users.add(self.users[0])

    def test_m2m_signal_on_model_without_passing_changing_field(self):
        serializer = ProjectSerializer(self.project, data={
            'admin_users': [self.users[1].id],
        }, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            assert False
        self.assertTrue(self.project.users.filter(id=self.users[1].id).exists())

    def test_m2m_signal_on_model_when_passing_changing_field(self):
        serializer = ProjectSerializer(self.project, data={
            'admin_users': [self.users[1].id],
            'users': [self.users[2].id]
        }, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            assert False
        self.assertTrue(self.project.users.filter(id=self.users[2].id).exists())
        self.assertTrue(self.project.users.filter(id=self.users[1].id).exists())

from django.test import TestCase
from .models import ProjectRick, ProjectMorty
from django.contrib.auth import get_user_model
# from django.core.serializers import serialize

User = get_user_model()


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
            }
        ]
        self.users = (
            User.objects.create(**users[0]),
            User.objects.create(**users[1]),
        )
        self.project_rick = ProjectRick.objects.create(**project_data)
        self.project_rick.users.add(self.users[0])
        # print('SET-UP ProjectRick:', serialize('json', ProjectRick.objects.all()))

        self.project_morty = ProjectMorty.objects.create(**project_data)
        self.project_morty.users.add(self.users[0])
        # print('SET-UP ProjectMorty:', serialize('json', ProjectMorty.objects.all()))

    def test_save_fn_on_model(self):
        self.project_rick.admin_users.add(self.users[1])
        self.assertEqual(self.project_rick.users.filter(id=self.users[1].id).exists(), True)

    def test_m2m_signal_on_model(self):
        self.project_morty.admin_users.add(self.users[1])
        self.assertEqual(self.project_morty.users.filter(id=self.users[1].id).exists(), True)

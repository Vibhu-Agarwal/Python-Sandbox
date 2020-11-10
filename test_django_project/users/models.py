from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import PermissionsMixin, UserManager

from django.utils.translation import ugettext_lazy as _

PHONE_REGEX = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. "
                                     "Up to 15 digits allowed.")


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model to store all kinds of users in the database.
    user_type field indicates if the account-type of user is of Business, Non-Prime Passenger or Prime Passenger
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(upload_to='static', null=True, blank=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30, blank=True, null=True)
    nickname = models.CharField(_('nickname'), max_length=30, blank=True, null=True)
    phone_number = models.CharField(validators=[PHONE_REGEX], max_length=17)

    is_active = models.BooleanField(_('is active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','email', 'phone_number']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        user_representation = self.first_name
        if self.last_name:
            user_representation += f" {self.last_name}"
        return user_representation

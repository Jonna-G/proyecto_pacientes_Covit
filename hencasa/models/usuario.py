from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, id, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not id:
            raise ValueError('Users must have an id')
        usuario = self.model(id=id)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return user

    def create_superuser(self, id, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        usuario = self.create_user(
            id=id,
            password=password,
        )
        usuario.is_admin = True
        usuario.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.BigAutoField(primary_key=True)
    us_nombre = models.TextField('nombres', max_length=30)
    us_apellidos = models.TextField('apellidos', max_length=30)
    us_edad = models.IntegerField('edad', default=0)
    us_direccion = models.TextField('direccion', max_length=50)
    us_telefono = models.IntegerField('telefono', default=0)
    us_email = models.EmailField ('email', max_length=15)
    us_password = models.CharField('Password', max_length=10)
    us_num_documento = models.IntegerField('documento', unique=True)
    

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'id_usuario'



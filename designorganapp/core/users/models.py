from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from designorganapp.settings import MEDIA_URL, STATIC_URL
from django.forms import model_to_dict
from crum import get_current_request


# from .managers import UserManager

class User(AbstractUser):
    GENDER = (
        ('M','Masculino'),
        ('F','Femenino'),
        ('O', 'Otro'),
    )
    gender = models.CharField(max_length=1, choices=GENDER, default='O', verbose_name='Género')
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True, verbose_name='Avatar')
    token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)

    # Función para cargar imagen por defecto en caso de que este vacio o no se haya cargado ninguna
    # caso contrario, se carga la imagen seleccionada 
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'image/empty.png')

    # El método "model_to_dict" me permite obtener un diccionario a partir del modelo que nostros le enviamos
    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['gender'] = {'id': self.gender, 'name': self.get_gender_display()}
        item['image'] = self.get_image()
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        return item

    # Este "request = get_current_request()" me permite obtener la seción actual que se está utilizando
    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass
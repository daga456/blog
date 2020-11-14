from django.contrib.auth.models import User
from django.test import TestCase
from articulos.models import Publicacion

class PublicacionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        autor = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Publicacion.objects.create(autor = autor, titulo = 'Titulo publicacion',
                                   textp = 'Texto de prueba de la publicación')
        pass


    def test_titulo_label(self):
        publicacion=Publicacion.objects.get(id=1)
        field_label = publicacion._meta.get_field('textp').verbose_name
        self.assertEquals(field_label,'textp')

    def test_titulo_max_length(self):
        publicacion=Publicacion.objects.get(id=1)
        max_length = publicacion._meta.get_field('titulo').max_length
        self.assertEquals(max_length,200)

    def test_fecha_creacion_label (self):
        publicacion = Publicacion.objects.get(id=1)
        field_label = publicacion._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label,'titulo')

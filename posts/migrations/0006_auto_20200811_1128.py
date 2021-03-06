# Generated by Django 3.0.3 on 2020-08-11 09:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
import dogs.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0002_auto_20200802_2134'),
        ('posts', '0005_auto_20200810_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dog',
            field=models.ForeignKey(choices=[(dogs.models.Dog(uuid.UUID('cef0cbf3-6458-4f13-a418-ee4d7e7505cd'), 'Izy', 'Croisé Berger', datetime.date(2019, 2, 1), datetime.date(2019, 5, 16), 'Noir, Feux, Blanc', 'Petite queue mais pas coupée, doubles ergots aux pattes arrière', None, 1, None, False, True, False, False, False, '12301', '', 'F', 'medium', None, True, 'izy12301.jpg'), dogs.models.Dog(uuid.UUID('cef0cbf3-6458-4f13-a418-ee4d7e7505cd'), 'Izy', 'Croisé Berger', datetime.date(2019, 2, 1), datetime.date(2019, 5, 16), 'Noir, Feux, Blanc', 'Petite queue mais pas coupée, doubles ergots aux pattes arrière', None, 1, None, False, True, False, False, False, '12301', '', 'F', 'medium', None, True, 'izy12301.jpg')), (dogs.models.Dog(uuid.UUID('cef0cbf3-6458-4f13-a418-ee4d7e7505ef'), 'Micky', 'Croisé Bouvier', datetime.date(2020, 2, 1), datetime.date(2013, 8, 10), 'Noir, Fauve, Blanc', 'Pattes couleur fauve, ligne blanche sur le torse', None, 2, None, False, True, False, False, False, '12302', 'Micky 7 ans et Cody son vieux copain de toujours. Le propriétaire étant décédé, la famille a fait appel aux dogcatchers…. C’était pour eux la mort assurée dans d’horribles souffrances. Au refuge, ils sont très proches. Micky veille sur Cody, il dort contre lui. S’ils pouvaient trouver une famille qui les adopterait tous les deux  cela serait juste magnifique pour eux.', 'M', 'big', None, True, 'micky12302.jpg'), dogs.models.Dog(uuid.UUID('cef0cbf3-6458-4f13-a418-ee4d7e7505ef'), 'Micky', 'Croisé Bouvier', datetime.date(2020, 2, 1), datetime.date(2013, 8, 10), 'Noir, Fauve, Blanc', 'Pattes couleur fauve, ligne blanche sur le torse', None, 2, None, False, True, False, False, False, '12302', 'Micky 7 ans et Cody son vieux copain de toujours. Le propriétaire étant décédé, la famille a fait appel aux dogcatchers…. C’était pour eux la mort assurée dans d’horribles souffrances. Au refuge, ils sont très proches. Micky veille sur Cody, il dort contre lui. S’ils pouvaient trouver une famille qui les adopterait tous les deux  cela serait juste magnifique pour eux.', 'M', 'big', None, True, 'micky12302.jpg'))], default='', on_delete=django.db.models.deletion.CASCADE, related_name='dogPost', to='dogs.Dog'),
        ),
    ]

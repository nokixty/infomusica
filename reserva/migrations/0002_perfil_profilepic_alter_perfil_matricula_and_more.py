# Generated by Django 4.1.3 on 2023-10-23 17:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='matricula',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='data',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='hora',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='post',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='status',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='status', to='reserva.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserva.perfil', verbose_name='Usuário'),
        ),
    ]

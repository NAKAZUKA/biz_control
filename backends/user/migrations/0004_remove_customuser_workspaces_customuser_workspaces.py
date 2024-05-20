# Generated by Django 4.2.13 on 2024-05-20 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work_space', '0002_alter_workspace_address'),
        ('user', '0003_customuser_workspaces'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='workspaces',
        ),
        migrations.AddField(
            model_name='customuser',
            name='workspaces',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='work_space.workspace', verbose_name='Место работы'),
        ),
    ]
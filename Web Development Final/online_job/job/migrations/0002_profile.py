# # Generated by Django 2.1.7 on 2021-09-30 16:41
#
# from django.conf import settings
# from django.db import migrations, models
# import django.db.models.deletion
#
#
# class Migration(migrations.Migration):
#
#     dependencies = [
#         migrations.swappable_dependency(settings.AUTH_USER_MODEL),
#         ('job', '0001_initial'),
#     ]
#
#     operations = [
#         migrations.CreateModel(
#             name='Profile',
#             fields=[
#                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#                 ('forget_password_token', models.CharField(max_length=100)),
#                 ('created_at', models.DateField(auto_now_add=True)),
#                 ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
#             ],
#         ),
#     ]

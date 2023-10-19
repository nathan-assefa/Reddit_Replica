# Generated by Django 4.2.6 on 2023-10-09 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_comment_post_postupvoted_postlove_postlike_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('unread_messages_count', models.IntegerField(default=0)),
                ('unread_notifications_count', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='commentdownvoted',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='commentdownvoted',
            name='user',
        ),
        migrations.RemoveField(
            model_name='commentlike',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='commentlike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='commentlove',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='commentlove',
            name='user',
        ),
        migrations.RemoveField(
            model_name='commentupvoted',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='commentupvoted',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='CommentDownvoted',
        ),
        migrations.DeleteModel(
            name='CommentLike',
        ),
        migrations.DeleteModel(
            name='CommentLove',
        ),
        migrations.DeleteModel(
            name='CommentUpvoted',
        ),
    ]

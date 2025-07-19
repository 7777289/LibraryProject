from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),  # If this throws an error, change to []
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('publication_year', models.IntegerField()),
            ],
        ),
    ]

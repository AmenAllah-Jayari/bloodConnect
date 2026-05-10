from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_donneur_telephone'),
        ('donneur', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Don',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_don', models.DateField()),
                ('etablissement', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True)),
                ('enregistre_le', models.DateTimeField(auto_now_add=True)),
                ('donneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dons', to='accounts.donneur')),
            ],
            options={
                'ordering': ['-date_don'],
            },
        ),
    ]

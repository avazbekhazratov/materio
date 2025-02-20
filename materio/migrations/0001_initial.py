# Generated by Django 4.2.1 on 2023-07-11 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import materio.models.auth


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('user_type', models.SmallIntegerField(default=0)),
                ('is_superuser', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', materio.models.auth.CustomerUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Basket_order',
            fields=[
                ('basket_name', models.CharField(max_length=128)),
                ('order_num', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_condation', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=50)),
                ('oxirgi_product', models.DateTimeField(auto_now=True)),
                ('xabar_berish', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=50)),
                ('passport', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Maxsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=128)),
                ('size', models.CharField(max_length=128)),
                ('color', models.CharField(max_length=128)),
                ('joyi', models.CharField(max_length=128)),
                ('soni', models.IntegerField()),
                ('product_price', models.IntegerField(default=0)),
                ('product_price_type', models.CharField(choices=[('USD', 'USD'), ('YUAN', 'YUAN'), ('UZS', 'UZS')], max_length=128)),
                ('entry_price', models.IntegerField(default=0)),
                ('entry_price_type', models.CharField(choices=[('USD', 'USD'), ('YUAN', 'YUAN'), ('UZS', 'UZS')], max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('key', models.CharField(max_length=512)),
                ('is_conf', models.BooleanField(default=False)),
                ('is_expire', models.BooleanField(default=False)),
                ('tries', models.SmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('product_num', models.IntegerField()),
                ('money_type', models.CharField(choices=[('USD', 'USD'), ('YUAN', 'YUAN'), ('UZS', 'UZS')], max_length=128)),
                ('employee_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Storage_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('size', models.CharField(max_length=128)),
                ('date', models.DateTimeField(auto_now=True)),
                ('color', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('order_number', models.IntegerField()),
                ('sent_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='savdo_oynasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sotish_narxi', models.CharField(max_length=50)),
                ('valyuta', models.CharField(choices=[('USD', 'USD'), ('YUAN', 'YUAN'), ('UZS', 'UZS')], max_length=128)),
                ('clent_bolsa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materio.maxsulot')),
            ],
        ),
        migrations.CreateModel(
            name='OmborMaxsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materio.maxsulot')),
                ('ombor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materio.storage')),
            ],
        ),
        migrations.CreateModel(
            name='Ombor_buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('Buyurtma qilindi', 'Buyurtma qilindi'), ("Yig'ilyapti", "Yig'ilyapti"), ("Yo'lda", "Yo'lda"), ('Keldi', 'Keldi')], max_length=128)),
                ('ombor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materio.storage')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materio.storage_order')),
            ],
        ),
        migrations.CreateModel(
            name='chetdan_buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shartnome_raqami', models.IntegerField()),
                ('davlat_nomi', models.CharField(max_length=128)),
                ('zavod_nomi', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('holati', models.CharField(choices=[('tuzildi', 'tuzildi'), ('yakunlandi', 'yakunlandi'), ('yolda', 'yolda'), ('qabul_qilindi', 'qabul_qilindi')], max_length=128)),
                ('maxsulot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materio.maxsulot')),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quent', models.IntegerField(default=1)),
                ('price', models.BigIntegerField(default=0)),
                ('price_type', models.CharField(choices=[('USD', 'USD'), ('YUAN', 'YUAN'), ('UZS', 'UZS')], max_length=128)),
                ('status', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materio.maxsulot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

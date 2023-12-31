# Generated by Django 4.2.2 on 2023-06-29 20:14

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('CliDNI', models.CharField(max_length=8, unique=True)),
                ('CliApePat', models.CharField(max_length=20)),
                ('CliNom', models.CharField(max_length=20)),
                ('CliEstReg', models.BooleanField(default=True)),
                ('password', models.CharField(max_length=128, null=True)),
                ('username', models.CharField(max_length=150, null=True, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ArtNom', models.CharField(max_length=50, null=True)),
                ('ArtDes', models.TextField(help_text='Ingresa la descripción del artículo', max_length=1000, null=True)),
                ('ArtImg', models.ImageField(null=True, upload_to='imagenes/imgs')),
                ('ArtSto', models.IntegerField()),
                ('ArtPreUni', models.FloatField()),
                ('ArtEstReg', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MarNom', models.CharField(max_length=20)),
                ('MarImg', models.ImageField(null=True, upload_to='imagenes/imgs')),
                ('MarEstReg', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PedidoCabecera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PedCabFec', models.DateField()),
                ('PedCabEstReg', models.BooleanField(default=True)),
                ('PedCabCodCli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoArticulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipArtNom', models.CharField(max_length=20)),
                ('TipArtEstReg', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VenDNI', models.CharField(max_length=8, unique=True)),
                ('VenApePat', models.CharField(max_length=20)),
                ('VenNom', models.CharField(max_length=20)),
                ('VenEstReg', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PedidoDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PedDetCantidad', models.IntegerField(default=1)),
                ('PedDetPreUniArt', models.FloatField(default=0.0)),
                ('PedDetSubtotal', models.FloatField(default=0.0)),
                ('PedDetTot', models.FloatField(default=0.0)),
                ('PedDetEstReg', models.BooleanField(default=True)),
                ('PedDetArtCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.articulo')),
                ('PedDetCodCab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='tienda.pedidocabecera')),
            ],
        ),
        migrations.AddField(
            model_name='pedidocabecera',
            name='PedCabCodVen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.vendedor'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='ArtMarCod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.marca'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='ArtTipCod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.tipoarticulo'),
        ),
    ]

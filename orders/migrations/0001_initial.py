# Generated by Django 4.0.4 on 2022-06-28 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('accounts', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.TextField()),
                ('payment_id', models.TextField()),
                ('amount', models.IntegerField()),
                ('date', models.TextField(default='-')),
                ('card_number', models.TextField(default='****')),
                ('idpay_track_id', models.IntegerField(default=0)),
                ('bank_track_id', models.TextField(default=0)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('date_of_order', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('social_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='socialaccount.socialaccount')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('payment_info', models.JSONField(default=dict)),
                ('shipment_type', models.CharField(choices=[('R', 'Regular'), ('P', 'Pishtaz')], default='regular', max_length=100)),
                ('final_price', models.PositiveIntegerField(default=0)),
                ('address', models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, related_name='address_set', to='accounts.address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='inventory.product')),
            ],
        ),
    ]

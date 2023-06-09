# Generated by Django 4.1 on 2022-09-28 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Name', models.CharField(max_length=64)),
                ('Description', models.CharField(max_length=264)),
                ('Starting_price', models.IntegerField()),
                ('Current_Bid', models.IntegerField()),
                ('Auction_closed', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='auctions.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lister', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

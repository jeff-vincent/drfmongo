# Generated by Django 2.2.5 on 2019-09-23 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(blank=True, default='', max_length=100)),
                ('y', models.CharField(blank=True, default='', max_length=100)),
                ('pams_pin', models.CharField(blank=True, default='', max_length=100)),
                ('municipal_code', models.CharField(blank=True, default='', max_length=100)),
                ('block', models.CharField(blank=True, default='', max_length=100)),
                ('lot', models.CharField(blank=True, default='', max_length=100)),
                ('qualifier', models.CharField(blank=True, default='', max_length=100)),
                ('prop_class', models.CharField(blank=True, default='', max_length=100)),
                ('municipal_name', models.CharField(blank=True, default='', max_length=100)),
                ('property_location', models.CharField(blank=True, default='', max_length=100)),
                ('owner_name', models.CharField(blank=True, default='', max_length=100)),
                ('owner_st_address', models.CharField(blank=True, default='', max_length=100)),
                ('owner_city_state', models.CharField(blank=True, default='', max_length=100)),
                ('owner_zip_code', models.CharField(blank=True, default='', max_length=100)),
                ('land_val', models.CharField(blank=True, default='', max_length=100)),
                ('imprvt_val', models.CharField(blank=True, default='', max_length=100)),
                ('net_value', models.CharField(blank=True, default='', max_length=100)),
                ('last_yr_tx', models.CharField(blank=True, default='', max_length=100)),
                ('bldg_desc', models.CharField(blank=True, default='', max_length=100)),
                ('land_desc', models.CharField(blank=True, default='', max_length=1500)),
                ('calc_acre', models.CharField(blank=True, default='', max_length=100)),
                ('add_lots1', models.CharField(blank=True, default='', max_length=100)),
                ('add_lots2', models.CharField(blank=True, default='', max_length=100)),
                ('fac_name', models.CharField(blank=True, default='', max_length=100)),
                ('prop_use', models.CharField(blank=True, default='', max_length=100)),
                ('bldg_class', models.CharField(blank=True, default='', max_length=100)),
                ('deed_book', models.CharField(blank=True, default='', max_length=100)),
                ('deed_page', models.CharField(blank=True, default='', max_length=100)),
                ('deed_date', models.CharField(blank=True, default='', max_length=100)),
                ('yr_constr', models.CharField(blank=True, default='', max_length=100)),
                ('sales_code', models.CharField(blank=True, default='', max_length=100)),
                ('sale_price', models.CharField(blank=True, default='', max_length=100)),
                ('dwell', models.CharField(blank=True, default='', max_length=100)),
                ('comm_dwell', models.CharField(blank=True, default='', max_length=100)),
                ('latitude', models.CharField(blank=True, default='', max_length=100)),
                ('longitude', models.CharField(blank=True, default='', max_length=100)),
                ('accuracy_score', models.CharField(blank=True, default='', max_length=100)),
                ('accuracy_type', models.CharField(blank=True, default='', max_length=100)),
                ('number', models.CharField(blank=True, default='', max_length=100)),
                ('property_street', models.CharField(blank=True, default='', max_length=100)),
                ('street', models.CharField(blank=True, default='', max_length=100)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('state', models.CharField(blank=True, default='', max_length=100)),
                ('zipcode', models.CharField(blank=True, default='', max_length=100)),
                ('county', models.CharField(blank=True, default='', max_length=100)),
                ('source', models.CharField(blank=True, default='', max_length=100)),
                ('summary', models.CharField(blank=True, default='', max_length=10000)),
                ('delivery_line_1', models.CharField(blank=True, default='', max_length=100)),
                ('delivery_line_2', models.CharField(blank=True, default='', max_length=100)),
                ('city_name', models.CharField(blank=True, default='', max_length=100)),
                ('state_abbreviation', models.CharField(blank=True, default='', max_length=100)),
                ('full_zipcode', models.CharField(blank=True, default='', max_length=100)),
                ('notes', models.CharField(blank=True, default='', max_length=100)),
                ('county_name', models.CharField(blank=True, default='', max_length=100)),
                ('rdi', models.CharField(blank=True, default='', max_length=100)),
                ('precision', models.CharField(blank=True, default='', max_length=100)),
                ('dpv_match_code', models.CharField(blank=True, default='', max_length=100)),
                ('dpv_footnotes', models.CharField(blank=True, default='', max_length=100)),
                ('footnotes', models.CharField(blank=True, default='', max_length=100)),
                ('zip_type', models.CharField(blank=True, default='', max_length=100)),
                ('carrier_route', models.CharField(blank=True, default='', max_length=100)),
                ('dpv_vacant', models.CharField(blank=True, default='', max_length=100)),
                ('active', models.CharField(blank=True, default='', max_length=100)),
                ('urbanization', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]

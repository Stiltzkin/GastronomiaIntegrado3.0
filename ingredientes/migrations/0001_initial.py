# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-17 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unidades_medida', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id_ingrediente', models.AutoField(primary_key=True, serialize=False)),
                ('nome_ingrediente', models.CharField(max_length=200)),
                ('quantidade_calorica_ingrediente', models.DecimalField(decimal_places=1, max_digits=6)),
                ('aproveitamento_ingrediente', models.DecimalField(decimal_places=1, max_digits=4)),
                ('quantidade_estoque_ingrediente', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('quantidade_reservada_ingrediente', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('valor_ingrediente', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('motivo_retirada_estoque', models.CharField(max_length=200, null=True)),
                ('id_unidade_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_unidades_medida', to='unidades_medida.UnidadeMedida')),
            ],
        ),
    ]

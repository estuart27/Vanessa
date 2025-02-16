# Generated by Django 5.1.5 on 2025-02-14 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0012_produto_subcategory_alter_produto_imagem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('motivo', models.CharField(choices=[('reclamacao', 'Reclamação'), ('elogio', 'Elogio'), ('sugestao', 'Sugestão'), ('duvida', 'Dúvida'), ('outro', 'Outro')], max_length=20)),
                ('mensagem', models.TextField()),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
    ]

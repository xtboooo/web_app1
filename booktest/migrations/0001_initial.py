# Generated by Django 2.2.5 on 2020-12-15 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=20, verbose_name='标题')),
                ('bpub_date', models.DateField(verbose_name='发布日期')),
                ('bread', models.IntegerField(default=0, verbose_name='阅读量')),
                ('bcomment', models.IntegerField(default=0, verbose_name='评论量')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
            ],
            options={
                'verbose_name': '图书',
                'db_table': 'tb_books',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20, verbose_name='名称')),
                ('hgender', models.BooleanField(default=False, verbose_name='性别')),
                ('hcomment', models.CharField(max_length=200, null=True, verbose_name='备注')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heros', to='booktest.BookInfo', verbose_name='所属图书')),
            ],
            options={
                'verbose_name': '英雄',
                'db_table': 'tb_heros',
            },
        ),
    ]

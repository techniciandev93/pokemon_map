from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Наименование на Русском')
    title_en = models.CharField(max_length=200, verbose_name='Наименование на Английском', blank=True)
    title_jp = models.CharField(max_length=200, verbose_name='Наименование на Японском', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    previous_evolution = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                           related_name='next_evolutions',
                                           verbose_name='От кого эволюционировал')
    image = models.ImageField(upload_to='images/pokemons', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.title_ru

    @property
    def next_evolution(self):
        return self.next_evolutions.first()


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон',
                                related_name='entities')
    appeared_at = models.DateTimeField(verbose_name='Дата появления')
    disappeared_at = models.DateTimeField(verbose_name='Дата исчезновения')
    level = models.IntegerField(verbose_name='Уровень', null=True, blank=True)
    health = models.IntegerField(verbose_name='Здоровье', null=True, blank=True)
    strength = models.IntegerField(verbose_name='Сила', null=True, blank=True)
    defence = models.IntegerField(verbose_name='Защита', null=True, blank=True)
    stamina = models.IntegerField(verbose_name='Выносливость', null=True, blank=True)

    def __str__(self):
        return self.pokemon.title_ru

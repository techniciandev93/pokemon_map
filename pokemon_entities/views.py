import folium
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def add_pokemon_to_map():
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    current_time = localtime()
    entity_pokemons = PokemonEntity.objects.select_related('pokemon').filter(appeared_at__lte=current_time,
                                                                             disappeared_at__gte=current_time)
    for entity_pokemon in entity_pokemons:
        add_pokemon(folium_map,
                    entity_pokemon.lat,
                    entity_pokemon.lon,
                    entity_pokemon.pokemon.image.path
                    )
    return folium_map


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    folium_map = add_pokemon_to_map()
    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    folium_map = add_pokemon_to_map()

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })

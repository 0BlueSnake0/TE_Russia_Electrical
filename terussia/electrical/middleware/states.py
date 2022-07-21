from ..models import State, Region
from django.conf import settings   



STATES = {
    "#00a2e8": [ 
       ("Adygey", "RUS2279"),
       ("Karachay-Cherkess", "RUS2280"),
       ("Kabardin-Balkar", "RUS2304"),
       ("North Ossetia", "RUS2305"),
       ("Stavropol'", "RUS2306"),
       ("Bryansk", "RUS2342"),
       ("Smolensk", "RUS2343"),
       ("Ivanovo", "RUS2355"),
       ("Kostroma", "RUS2356"),
       ("Tver'", "RUS2358"),
       ("Yaroslavl'", "RUS2360"),
       ("Kaluga", "RUS2361"),
       ("Kursk", "RUS2362"),
       ("Lipetsk", "RUS2363"),
       ("Moskovsskaya", "RUS2364"),
       ("Moskva", "RUS2365"),
       ("Orel", "RUS2366"),
       ("Rostov", "RUS2367"),
       ("Tula", "RUS2368"),
       ("Volgograd", "RUS2369"),
       ("Belgorod", "RUS2370"),
       ("Krasnodar", "RUS2371"),
       ("Ryazan'", "RUS2374"),
       ("Tambov", "RUS2375"),
       ("Vladimir", "RUS2376"),
       ("Voronezh", "RUS2377"),
       ("Astrakhan'", "RUS2388"),
       ("Kalmyk", "RUS2390"),
       ("Chechnya", "RUS2416"),
       ("Dagestan", "RUS2417"),
    ],
    "#b5e61d": [
        ("Kaliningrad", "RUS2324"),
        ("Murmansk", "RUS2333"),
        ("Novgorod", "RUS2334"),
        ("Pskov", "RUS2335"),
        ("Leningrad", "RUS2336"),
        ("City of St. Petersburg", "RUS2337"),
        ("Karelia", "RUS2353"),
        ("Arkhangel'sk", "RUS2354"),
        ("Vologda", "RUS2359"),
        ("Nenets", "RUS2381"),
        ("Yamal-Nenets", "RUS2382"),
        ("Komi", "RUS2383"),
        ("Kirov", "RUS2384"),
        ("Mariy-El", "RUS2385"),
        ("Chuvash", "RUS2389"),
        ("Tatarstan", "RUS2394"),
    ],
    "#880015": [
       ("Tomsk", "RUS2167"),
       ("Ingush", "RUS2303"),
       ("Chukchi Autonomous Okrug", "RUS2321"),
       ("Nizhegorod", "RUS2357"),
       ("Mordovia", "RUS2372"),
       ("Penza", "RUS2373"),
       ("Bashkortostan", "RUS2378"),
       ("Chelyabinsk", "RUS2379"),
       ("Sverdlovsk", "RUS2386"),
       ("Udmurt", "RUS2387"),
       ("Orenburg", "RUS2391"),
       ("Samara", "RUS2392"),
       ("Saratov", "RUS2393"),
       ("Ul'yanovsk", "RUS2395"),
       ("Khanty-Mansiy", "RUS2396"),
       ("Omsk", "RUS2397"),
       ("Tyumen'", "RUS2398"),
       ("Altay", "RUS2399"),
       ("Gorno-Altay", "RUS2400"),
       ("Kemerovo", "RUS2401"),
       ("Khakass", "RUS2402"),
       ("Novosibirsk", "RUS2403"),
       ("Irkutsk", "RUS2602"),
       ("Krasnoyarsk", "RUS2603"),
       ("Tuva", "RUS2605"),
       ("Buryat", "RUS2606"),
       ("Amur", "RUS2609"),
       ("Chita", "RUS2610"),
       ("Primor'ye", "RUS2611"),
       ("Sakha (Yakutia)", "RUS2612"),
       ("Yevrey", "RUS2613"),
       ("Khabarovsk", "RUS2614"),
       ("Maga Buryatdan", "RUS2615"),
       ("Sakhalin", "RUS2616"),
       ("Perm'", "RUS3200"),
       ("Kamchatka", "RUS3468"),
    ],
}


class InitStatesMiddleware: 
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request): 
        if 'admin' in request.path:
            for region_color in STATES:
                for (name, slug) in STATES[region_color]:
                    if not State.objects.filter(slug=slug).exists():
                        state = State.objects.create(slug=slug, name=name)
                        if Region.objects.filter(color=region_color).exists():
                            state.region = Region.objects.get(color=region_color)
                            state.save()

        return self.get_response(request)

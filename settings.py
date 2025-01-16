WIDTH = 1280
HEIGHT = 768
FPS = 60
TILESIZE = 64
DIMENSION = 61
MIDPOINT = 30
text_colour = '#000000'

weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/melee sprites/up.png'},
}

monster_data = {
    'monster': {'health':100, 'exp':100, 'dmg':1, 'attack_type': 'melee', 'speed': 2, 'knockback':3, 'attack_radius': 80, 'agro_radius': 560}
}

weapon_data = {
    'sword' : {'cooldown': 100, 'damage': 15, 'graphics': '/graphics/weapons/sword/full.png'}
}

magic_data = {
    'flame' : {'strength': 5, 'cost': 20, 'graphics': '/graphics/weapons/axe/full.png'},
    'heal' : {'strength': 30, 'cost': 10, 'graphics': '/graphics/weapons/axe/full.png'}}
WIDTH = 1280
HEIGHT = 768
FPS = 60
TILESIZE = 64

weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/melee sprites/up.png'},
}

# world_map =  [
#     ['x', '', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
#     ['x', '', '', '', '', '', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
#     ['x', '', '', '', '', '', '', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
#     ['x', '', '', 'p', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
#     ['x', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
#     ['x', '', '', 'y', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
#     ['x', '', '', '', '', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
#     ['x', 'y', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
#     ['x', '', '', '', '', '', 'y', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
#     ['x', '', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
#     ['x', '', '', '', 'y', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
#     ['x', '', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
#     ['x', '', '', '', '', 'x', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
#     ['x', '', '', '', '', 'x', 'x', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
#     ['x', '', '', '', '', 'x', 'x', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
#     ['x', '', '', '', '', 'x', 'x', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
#     ['x', '', '', '', '', 'x', 'x', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
#     ['x', '', '', '', '', 'x', 'x', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
#     ['x', '', '', '', '', 'x', 'x', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
#     ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
# ]

monster_data = {
    'monster': {'health':100, 'exp':100, 'dmg':10, 'attack_type': 'melee', 'speed': 3, 'knockback':3, 'attack_radius': 80, 'agro_radius': 560}
}

weapon_data = {
    'sword' : {'cooldown': 100, 'damage': 15, 'graphics': '/graphics/weapons/sword/full.png'}
}

magic_data = {
    'flame' : {'strength': 5, 'cost': 20, 'graphics': '/graphics/weapons/axe/full.png'},
    'heal' : {'strength': 30, 'cost': 10, 'graphics': '/graphics/weapons/axe/full.png'}}
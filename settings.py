WIDTH = 1280
HEIGHT = 768
FPS = 60
TILESIZE = 64

world_map =  [
    ['x', '', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '', '', '', '', '', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '', '', '', '', '', '', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '', '', 'p', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '', '', 'y', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '', '', '', '', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'y', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', '', '', 'y', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', 'y', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', '', 'x', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', '', 'x', 'x', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', '', 'x', 'x', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', '', 'x', 'x', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', '', 'x', 'x', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', '', 'x', 'x', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', '', 'x', 'x', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
]

monster_data = {
    'monster': {'health':100, 'exp':100, 'dmg':10, 'attack_type': 'melee', 'speed': 3, 'knockback':3, 'attack_radius': 80, 'agro_radius': 400}
}
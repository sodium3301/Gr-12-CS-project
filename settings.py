WIDTH = 1280
HEIGHT = 768
FPS = 60
TILESIZE = 64

worldMap =  [
    ['x', '', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '', '', '', '', '', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '', '', '', '', '', '', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '', '', 'p', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '', '', '', 'y', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
    ['x', '', '', '', '', '', '', 'x', '', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '', 'x'],
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
    'mob': {'health':100, 'exp':100, 'dmg':10, 'attack_type': 'melee', 'speed': 2, 'knockback':3, 'attack_radius': 120, 'agro_radius': 400}
}
import tcod

from enum import Enum, auto


# This will probably be useful but we'll leave it for later
class RenderOrder(Enum):
    PLACEHOLDER = auto()


def get_names_under_mouse(mouse, entities):
    (x, y) = (mouse.cx, mouse.cy)

    names = [entity.name for entity in entities if entity.x == x and entity.y == y]
    names = ', '.join(names)

    return names.capitalize()


def render_bar(panel, x, y, total_width, name, value, maximum, bar_color, back_color):
    bar_width = int(float(value) / maximum * total_width)

    tcod.console_set_default_background(panel, back_color)
    tcod.console_rect(panel, x, y, total_width, 1, False, tcod.BKGND_SCREEN)

    tcod.console_set_default_background(panel, bar_color)
    if bar_width > 0:
        tcod.console_rect(panel, x, y, bar_width, 1, False, tcod.BKGND_SCREEN)

    tcod.console_set_default_foreground(panel, tcod.white)
    tcod.console_print_ex(panel, int(x + total_width / 2), y, tcod.BKGND_NONE, tcod.CENTER,
                             '{0}: {1}/{2}'.format(name, value, maximum))


# Render all entities in the given list. Hacked a lot of fov stuff out of here so hopefully it aint brok
# todo: wtf is a panel? may need to keep tweaking this. May need full rewrite!
def render_all(con, panel, entities, game_map, message_log, screen_width, screen_height,
               panel_height, panel_y, mouse, colors):

    for y in range(game_map.height):
        for x in range(game_map.width):
            wall = game_map.tiles[x][y].block_sight
            if wall:
                tcod.console_set_char_background(con, x, y, colors.get('light_wall'), tcod.BKGND_SET)
            else:
                tcod.console_set_char_background(con, x, y, colors.get('light_ground'), tcod.BKGND_SET)

    entities_in_render_order = sorted(entities, key=lambda x: x.render_order.value)

    for entity in entities_in_render_order:
        draw_entity(con, entity)

    # deprecated, should use Console.blit
    # tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0) on second thought this doesnt do anything?

    tcod.console_set_default_background(panel, tcod.black)
    tcod.console_clear(panel)

    y = 1
    for message in message_log.visible:
        tcod.console_set_default_foreground(panel, message.color)
        tcod.console_print_ex(panel, message_log.x, y, tcod.BKGND_NONE, tcod.LEFT, message.text)
        y += 1

    tcod.console_set_default_foreground(panel, tcod.light_gray)
    tcod.console_print_ex(panel, 1, 0, tcod.BKGND_NONE, tcod.LEFT, get_names_under_mouse(mouse, entities))

    tcod.console_blit(panel, 0, 0, screen_width, panel_height, 0, 0, panel_y)


'''
# This stuff might be handy, can grab the rest from Gou if needed
# Displays a popup with the given size and message. Is dismissed when any key is pressed
def popup(con, message, width, height):
    dismiss = False

    while not dismiss:
        message_box(con, message, 50,
                    width, height)
        tcod.console_flush()
        key = tcod.console_wait_for_keypress(True)
        action = handle_popup(key)
        dismiss = action.get('dismiss')
'''


# erase all entities in the given list
def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


# draw an entity's char
def draw_entity(con, entity):
    tcod.console_set_default_foreground(con, entity.color)
    tcod.console_put_char(con, entity.x, entity.y, entity.char, tcod.BKGND_NONE)


# erase an entity's char
def clear_entity(con, entity):
    tcod.console_put_char(con, entity.x, entity.y, ' ', tcod.BKGND_NONE)

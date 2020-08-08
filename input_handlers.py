import tcod


# This lets different keys do different things in different menus, if we want that. see Gou for details
def handle_keys(key):
    return handle_sim_keys(key)


# Key handler for simulation running normally
def handle_sim_keys(key):
    if key.vk == tcod.KEY_ESCAPE:
        return {'exit': True}
    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt Enter to enter fullscreen
        return {'fullscreen': True}

    return {}


def handle_mouse(mouse):
    x, y = mouse.cx, mouse.cy

    if mouse.lbutton_pressed:
        return {'left_click': (x, y)}
    elif mouse.rbutton_pressed:
        return {'right_click': (x, y)}
    elif mouse.wheel_up:
        return {'wheel_up': True}
    elif mouse.wheel_down:
        return {'wheel_down': True}

    return {}

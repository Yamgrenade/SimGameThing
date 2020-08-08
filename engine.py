import tcod
from render_functions import render_all, clear_all
from loader_functions.init_new_game import get_constants, get_game_variables, place_animals
import time
from input_handlers import handle_mouse, handle_keys
from game_messages import Message


def main():
    constants = get_constants()

    '''
    If we want to change "tileset" we can use this, hopefully it works without tho
    # tcod.console_set_custom_font('symbols.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    Or this might be more current:
    # tileset = tcod.tileset.load_tilesheet(
    #    "whatever.png", 32, 8, tcod.tileset.CHARMAP_TCOD,
    # )
    

    tcod.console_init_root(constants['screen_width'], constants['screen_height'], constants['window_title'], False,
                              renderer=tcod.RENDERER_SDL2, vsync=True)


    con = tcod.console.Console(constants['screen_width'], constants['screen_height'])
    panel = tcod.console.Console(constants['screen_width'], constants['panel_height'])
    
    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS | tcod.EVENT_MOUSE, key, mouse)

        render_all(con, panel, entities, player, game_map, message_log,
                   constants['screen_width'],
                   constants['screen_height'], constants['bar_width'], constants['panel_height'],
                   constants['panel_y'], mouse, constants['colors'])

        tcod.console_flush()

        clear_all(con, entities)

        # Input handling block goes here
        action = handle_keys(key)
        mouse_action = handle_mouse(mouse)

        fullscreen = action.get('fullscreen')

        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
    '''

    # old stuff   ^
    # new attempt v

    entities, game_map, message_log = get_game_variables(constants)

    place_animals(constants, entities, game_map)

    key = tcod.Key()
    mouse = tcod.Mouse()

    tileset = tcod.tileset.load_tilesheet("symbols.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    console = tcod.Console(constants['screen_width'], constants['screen_height'])
    panel = tcod.Console(constants['panel_height'], constants['panel_y'])
    with tcod.context.new_terminal(constants['screen_width'], constants['screen_height'], tileset=tileset) as context:
        # Main game loop
        while True:
            console.clear(fg=(159, 159, 159))

            render_all(console, panel, entities, game_map, message_log,
                       constants['screen_width'],
                       constants['screen_height'], constants['panel_height'],
                       constants['panel_y'], mouse, constants['colors'])

            context.present(console)

            for event in tcod.event.get():
                context.convert_event(event)  # Sets tile coordinates for mouse events.
                # print(event)  # Print event information to stdout.
                if event.type == "QUIT":
                    raise SystemExit()
            time.sleep(constants["turn_length"])
            for entity in entities:
                if entity.ai:
                    entity.ai.take_turn(game_map, entities)

            
if __name__ == '__main__':
    main()

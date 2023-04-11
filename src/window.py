import pyray as rl
import logic as l
import time
rl.init_window(1200, 600, "Cricket")

font_size = 100
clicked = False
balls = 12
score = []
offscreen = l.choose(5)
onscreen = ["*" for x in range(len(offscreen))]
number_color = rl.WHITE
background_color = rl.BLACK

while not rl.window_should_close():
    rl.set_target_fps(60)
    # rl.draw_fps(0,0)
    for i in range(len(offscreen)):
        mouse_pos = rl.get_mouse_position()
        number_pos = rl.Vector2(200 * (i + 1), 300)
        if(not clicked and balls != 0):
            if rl.check_collision_point_rec(mouse_pos, rl.Rectangle(number_pos.x - font_size / 2,
                                                                    number_pos.y - font_size / 2,
                                                                    font_size,
                                                                    font_size)):
                if rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
                    # onscreen[i] = offscreen[i]
                    clicked = True
                    score.append(onscreen[i])
                    balls-=1
                    offscreen = l.choose(len(offscreen))
                    # onscreen = ["*" for x in range(len(offscreen))]
                    clicked = False

    rl.begin_drawing()
    rl.clear_background(background_color)

    for i in range(len(onscreen)):
        number_pos = rl.Vector2(200 * (i + 1), 300)
        rl.draw_text(str(onscreen[i]), int(number_pos.x - font_size / 2),
                     int(number_pos.y - font_size / 2),
                     font_size,
                     number_color)
    rl.draw_text("SCORE : "+str(sum(score))+":"+str(score), 0,
                 0,
                 font_size // 4,
                 number_color)

    rl.end_drawing()

rl.close_window()
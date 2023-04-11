import pyray as rl
import logic as l
import time
rl.init_window(1200, 600, "Numbers")

font_size = 100
clicked = False
choices = 5
balls = 12
score = []
screen = l.choose(choices)
numbers = [0 for x in range(len(screen))]
number_color = rl.WHITE
background_color = rl.BLACK

while not rl.window_should_close():
    rl.set_target_fps(60)
    # rl.draw_fps(0,0)
    for i in range(len(numbers)):
        mouse_pos = rl.get_mouse_position()
        number_pos = rl.Vector2(200 * (i + 1), 300)
        if(not clicked and balls != 0):
            if rl.check_collision_point_rec(mouse_pos, rl.Rectangle(number_pos.x - font_size / 2,
                                                                    number_pos.y - font_size / 2,
                                                                    font_size,
                                                                    font_size)):
                if rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
                    numbers[i] = screen[i]
                    clicked = True
                    print(screen[i])
                    score.append(numbers[i])
                    balls-=1
                    screen = l.choose(choices)
                    numbers = [0 for x in range(len(screen))]
                    clicked = False

    rl.begin_drawing()
    rl.clear_background(background_color)

    for i in range(len(numbers)):
        number_pos = rl.Vector2(200 * (i + 1), 300)
        rl.draw_text(str(numbers[i]), int(number_pos.x - font_size / 2),
                     int(number_pos.y - font_size / 2),
                     font_size,
                     number_color)
        rl.draw_text("SCORE : "+str(sum(score))+":"+" ".join(str(score)), 0,
                     0,
                     font_size // 4,
                     number_color)

    rl.end_drawing()

rl.close_window()
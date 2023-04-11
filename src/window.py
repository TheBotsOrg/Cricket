import pyray as rl
import logic as l
import time
rl.init_window(1200, 600, "Cricket")

font_size = 100
clicked = False
balls = 12
score = []
offscreen = l.choose(5)
onscreen = [0 for x in range(len(offscreen))]
number_color = rl.WHITE
background_color = rl.BLACK

def getScore(score,balls):
    runs = 0
    wickets = 0
    for x in range(len(score)):
        match score[x]:
            case "wicket":
                wickets+=1
            case "no ball":
                r = l.choose(1,nob=True)[0]
                # score[x] += ("("+str(r)+")")
                runs+=r
            case "wide":
                runs+=1
            case default:
                runs+=score[x]
    return (runs , wickets)


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
                    onscreen[i] = offscreen[i]
                    clicked = True
                    print(offscreen[i])
                    score.append(onscreen[i])
                    balls-=1
                    offscreen = l.choose(len(offscreen))
                    onscreen = [0 for x in range(len(offscreen))]
                    clicked = False

    rl.begin_drawing()
    rl.clear_background(background_color)

    for i in range(len(onscreen)):
        number_pos = rl.Vector2(200 * (i + 1), 300)
        rl.draw_text(str(onscreen[i]), int(number_pos.x - font_size / 2),
                     int(number_pos.y - font_size / 2),
                     font_size,
                     number_color)
    runs , wickets = getScore(score , balls)
    rl.draw_text("SCORE : "+str(runs)+"/"+str(wickets)+":", 0,
                 0,
                 font_size // 4,
                 number_color)
    rl.draw_text(str(score), 560,
                 0,
                 font_size // 4,
                 number_color)
    rl.draw_text(str((12-balls)//6)+"."+str((12-balls)%6), 0,
                 40,
                 font_size // 4,
                 number_color)

    rl.end_drawing()

rl.close_window()
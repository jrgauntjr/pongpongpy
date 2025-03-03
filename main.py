import arcade
import random
import os


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Pong Pong"
SPRITE_SCALING = 0.5
MOVEMENT_SPEED = 7

class PongPong(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.paused = False
        self.background = None

        self.player = None
        self.player2 = None
        self.player_list = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.w_pressed = False
        self.s_pressed = False

        self.setup()

    def setup(self):
        self.background = arcade.load_texture("images/wall.png")

        self.player_list = arcade.SpriteList()

        self.player1 = Player("images/player.png", scale=SPRITE_SCALING)
        self.player1.center_x = 50
        self.player1.center_y = SCREEN_HEIGHT / 2

        self.player2 = Player("images/player.png", scale=SPRITE_SCALING)
        self.player2.center_x = SCREEN_WIDTH - 51
        self.player2.center_y = SCREEN_HEIGHT / 2

        self.player_list.append(self.player1)
        self.player_list.append(self.player2)

    
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background, arcade.LBWH(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.paused:
            arcade.draw_text("Paused", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE, 48, anchor_x="center")
        self.player_list.draw()

    def on_update(self, delta_time):
        if not self.paused:
            self.player_list.update()
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            arcade.close_window()
        elif symbol == arcade.key.P:
            self.paused = not self.paused
            if self.paused:               
                arcade.pause()
            else:
                arcade.start()

        # Movement       
        elif symbol == arcade.key.UP:
            self.up_pressed = True
            self.update_player1_speed()
        elif symbol == arcade.key.DOWN:
            self.down_pressed = True
            self.update_player1_speed()
        elif symbol == arcade.key.W:
            self.w_pressed = True
            self.update_player2_speed()
        elif symbol == arcade.key.S:
            self.s_pressed = True
            self.update_player2_speed()

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.up_pressed = False
            self.update_player1_speed()
        elif symbol == arcade.key.DOWN:
            self.down_pressed = False
            self.update_player1_speed()
        elif symbol == arcade.key.W:
            self.w_pressed = False
            self.update_player2_speed()
        elif symbol == arcade.key.S:
            self.s_pressed = False
            self.update_player2_speed()
        
    def update_player1_speed(self):
        self.player1.change_x = 0
        self.player1.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player1.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player1.change_y = -MOVEMENT_SPEED
    
    def update_player2_speed(self):
        self.player2.change_x = 0
        self.player2.change_y = 0

        if self.w_pressed and not self.s_pressed:
            self.player2.change_y = MOVEMENT_SPEED
        elif self.s_pressed and not self.w_pressed:
            self.player2.change_y = -MOVEMENT_SPEED




class Player(arcade.Sprite):
    def update(self, delta_time: float = 1/60):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1


        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


def main():
    window = PongPong(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()

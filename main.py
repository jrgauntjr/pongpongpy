import arcade
import os

SCREEN_WIDTH, SCREEN_HEIGHT = arcade.get_display_size()
SCREEN_TITLE = "Pong Pong"
SPRITE_SCALING = 0.5
MOVEMENT_SPEED = 5

class PongPong(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.paused = False
        self.background = None

        self.player = None
        self.player_list = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.setup()

    def setup(self):
        self.background = arcade.load_texture("images/wall.png")

        self.player_list = arcade.SpriteList()
        self.player = Player("images\player.png", scale=SPRITE_SCALING)

        self.player.center_x = 50
        self.player.center_y = 50
        self.player_list.append(self.player)

    

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background, arcade.LBWH(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player_list.draw()
    
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
            self.update_player_speed()
        elif symbol == arcade.key.DOWN:
            self.down_pressed = True
            self.update_player_speed()

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.up_pressed = False
            self.update_player_speed()
        elif symbol == arcade.key.DOWN:
            self.down_pressed = False
            self.update_player_speed()
        
    def update_player_speed(self):
        self.player.change_x = 0
        self.player.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player.change_y = -MOVEMENT_SPEED




class Player(arcade.Sprite):
    def update(self, delta_time: float = 1/60):

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
    window.set_fullscreen(True)
    arcade.run()

if __name__ == "__main__":
    main()

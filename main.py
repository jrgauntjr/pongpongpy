import arcade
import os

SCREEN_WIDTH, SCREEN_HEIGHT = arcade.get_display_size()
SCREEN_TITLE = "Pong Pong"

class PongPong(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.paused = False
        self.background = None
        self.setup()

    def setup(self):
        self.background = arcade.load_texture("images/wall.png")
        
    

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background, arcade.LBWH(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            arcade.close_window()
        elif symbol == arcade.key.P:
            self.paused = not self.paused
            if self.paused:
                arcade.pause()
            else:
                arcade.start()

def main():
    window = PongPong(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.set_fullscreen(True)
    arcade.run()

if __name__ == "__main__":
    main()

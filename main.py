import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = arcade.get_display_size()
SCREEN_TITLE = "Pong Pong"

class PongPong(arcade.View):
    def __init__(self):
        super().__init__()
        self.paused = False

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        
    
    def on_key_press(self, symbol, modifiers):
        return super().on_key_press(symbol, modifiers)

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.set_fullscreen(True)
    game = PongPong()
    game.setup()
    
    window.show_view(game)
    arcade.run()




if __name__ == "__main__":
    main()
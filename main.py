import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = arcade.get_display_size()
SCREEN_TITLE = "Pong Pong"

class PongPong(arcade.Window):
    def __init__(self):
        super().__init__()

    def setup(self):
        pass

    def on_draw(self):
        pass

def main():
    print(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")




if __name__ == "__main__":
    main()
import arcade
import random

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Pong Pong"
SPRITE_SCALING = 0.5
MOVEMENT_SPEED = 8

class PongPong(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.paused = False
        self.background = None

        self.player1 = None
        self.p1_score = 0

        self.player2 = None
        self.p2_score = 0


        self.player_list = None

        self.ball_list = None

        self.up_pressed = False
        self.down_pressed = False
        self.w_pressed = False
        self.s_pressed = False

        self.setup()

    def setup(self):
        self.background = arcade.load_texture("images/wall.png")

        self.player_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()

        self.player1 = Player("images/player.png", scale=SPRITE_SCALING)
        self.player1.center_x = 50
        self.player1.center_y = SCREEN_HEIGHT / 2

        self.player2 = Player("images/player.png", scale=SPRITE_SCALING)
        self.player2.center_x = SCREEN_WIDTH - 51
        self.player2.center_y = SCREEN_HEIGHT / 2

        self.ball = Ball("images/ball.png", scale=SPRITE_SCALING)
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

        self.player_list.append(self.player1)
        self.player_list.append(self.player2)
        self.ball_list.append(self.ball)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background, arcade.LBWH(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        s1 = f"P1 Score: {self.p1_score}"
        arcade.draw_text(s1, 10, SCREEN_HEIGHT - 20, arcade.color.GOLD, 14)
        s2 = f"P2 Score: {self.p2_score}"
        arcade.draw_text(s2, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 20, arcade.color.BLACK, 14)
        if self.paused:
            arcade.draw_text("Paused", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE, 48, anchor_x="center")
        self.player_list.draw()
        self.ball_list.draw()

    def on_update(self, delta_time):
        if not self.paused:
            self.player_list.update()
            self.ball_list.update(delta_time)

            for ball in self.ball_list:
                if ball.collision_cooldown > 0:
                    continue  # Skip collision checks if cooldown is active

                ball_collided = False

                # Check for collisions with player1
                if arcade.check_for_collision(ball, self.player1):
                    ball.change_x *= -1
                    ball.change_y += random.uniform(-1, 1)  # Add randomness to the y direction
                    ball.center_x = self.player1.right + ball.width / 2
                    self.add_new_ball()
                    ball_collided = True
                    ball.collision_cooldown = 0.5  # Set cooldown period

                # Check for collisions with player2
                if not ball_collided and arcade.check_for_collision(ball, self.player2):
                    ball.change_x *= -1
                    ball.change_y += random.uniform(-1, 1)  # Add randomness to the y direction
                    ball.center_x = self.player2.left - ball.width / 2
                    self.add_new_ball()
                    ball_collided = True
                    ball.collision_cooldown = 0.5  # Set cooldown period

                if ball.left < 0:
                    self.p2_score += 1
                    self.ball_list.remove(ball)

                if ball.right > SCREEN_WIDTH:
                    self.p1_score += 1
                    self.ball_list.remove(ball)

            if len(self.ball_list) == 0:
                self.add_new_ball()

                
    def add_new_ball(self):
        new_ball = Ball("images/ball.png", scale=SPRITE_SCALING)
        new_ball.center_x = SCREEN_WIDTH / 2
        new_ball.center_y = SCREEN_HEIGHT / 2
        new_ball.change_x = random.choice([-4, 4])  # Random initial x direction
        new_ball.change_y = random.uniform(-2, 2)  # Random initial y direction
        self.ball_list.append(new_ball)

    def on_key_press(self, symbol, modifiesrs):
        if symbol == arcade.key.Q:
            arcade.close_window()
        elif symbol == arcade.key.P:
            self.paused = not self.paused

        # Movement
        elif symbol == arcade.key.UP:
            self.up_pressed = True
            self.update_player2_speed()
        elif symbol == arcade.key.DOWN:
            self.down_pressed = True
            self.update_player2_speed()
        elif symbol == arcade.key.W:
            self.w_pressed = True
            self.update_player1_speed()
        elif symbol == arcade.key.S:
            self.s_pressed = True
            self.update_player1_speed()

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.up_pressed = False
            self.update_player2_speed()
        elif symbol == arcade.key.DOWN:
            self.down_pressed = False
            self.update_player2_speed()
        elif symbol == arcade.key.W:
            self.w_pressed = False
            self.update_player1_speed()
        elif symbol == arcade.key.S:
            self.s_pressed = False
            self.update_player1_speed()

    def update_player1_speed(self):
        self.player1.change_x = 0
        self.player1.change_y = 0

        if self.w_pressed and not self.s_pressed:
            self.player1.change_y = MOVEMENT_SPEED
        elif self.s_pressed and not self.w_pressed:
            self.player1.change_y = -MOVEMENT_SPEED

    def update_player2_speed(self):
        self.player2.change_x = 0
        self.player2.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player2.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
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


class Ball(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.change_x = 4
        self.change_y = 4
        self.collision_cooldown = 0  # Cooldown period for collisions

    def update(self, delta_time: float = 1/60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1
            self.change_y += random.uniform(-1, 1)
        if self.right > SCREEN_WIDTH - 1:
            self.change_x *= -1
            self.change_y += random.uniform(-1, 1)
        if self.bottom < 0:
            self.change_y *= -1
            self.change_x += random.uniform(-1, 1)
        if self.top > SCREEN_HEIGHT - 1:
            self.change_y *= -1
            self.change_x += random.uniform(-1, 1)

        if self.collision_cooldown > 0:
            self.collision_cooldown -= delta_time


def main():
    window = PongPong(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()

from consts import *
from enemy import Enemy
from player import Player
from floor import Lava
from soundtracks import SoundTrack
from animated import *
import json


class Screen:
    '''This class printing every scene on our game screen and calculating events that are happening in our game scene'''

    def __init__(self, display, player: Player, bullet_img, enemy: Enemy, lava: Lava, heart: Heart):
        self.display = display
        self.player = player
        self.bullet_img = bullet_img
        self.enemy = enemy
        self.lava = lava
        self.heart = heart
        self.bigfont = pygame.font.Font('freesansbold.ttf', 45)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.background = AnimatedBackground()
        self.animated_explosion = Explosion()
        self.explode_enemy = []
        self.health_drop = 25
        self.get_current_position = False
        self.count = 0
        self.heart_timer = randint(0, 1000)

    def get_frame_time(self):
        return pygame.time.get_ticks()

    def get_player_current_position(self):
        x, y = self.player.rectangle.x, self.player.rectangle.y
        return x, y

    def start(self):
        '''This function is the starting screen of the game'''
        mixer_background = SoundTrack.starting_background()
        score_file = open('score.json', 'r')
        load_score_file = json.load(score_file)
        score_file.close()
        starting_font = self.bigfont.render(
            'Press Any Key To Start!', True, (255, 255, 255))
        highest_score_text = self.font.render(
            f'Highest Score: {load_score_file["highestscore"]}', True, (255, 255, 255))
        last_score_text = self.font.render(
            f'Last Score: {load_score_file["lastscore"]}', True, (255, 255, 255))
        clock = pygame.time.Clock()
        game = False
        while game == False:
            mixer_background
            clock.tick(FPS)
            animated_background = self.background.background_image
            WIN.blit(animated_background, (0, 0))
            WIN.blit(starting_font, (WIDTH/3.4, HEIGHT/2.2))
            WIN.blit(highest_score_text, (10, 10))
            WIN.blit(last_score_text, (10, 50))
            pygame.display.update()
            self.background.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    game = True

    def save_score(self, score: list):
        '''This function saving the highest score and the last score and saving it in a json file'''

        score_file = open('score.json', 'r')
        load_score_file = json.load(score_file)
        score_file.close()
        if score[0] > load_score_file['highestscore']:
            load_score_file['highestscore'] = score[0]
        load_score_file['lastscore'] = score[0]
        score_file = open('score.json', 'w')
        json.dump(load_score_file, score_file)
        score_file.close()

    def onCollision(self, score: list):
        '''This function determines object collisions on screen and returns a reactions'''
        # Determines if player1 bullet collided an object.
        for bullets in self.player.bullets:
            for enemy in self.enemy.enemies:
                if bullets.colliderect(enemy):
                    self.enemy.enemies.remove(enemy)
                    self.player.bullets.remove(bullets)
                    self.animated_explosion.is_exploding = True
                    self.explode_enemy.append(enemy)
                    SoundTrack.enemyhit()
                    score[0] += 100

        # Determines if enemy collided the player.
        for enemy in self.enemy.enemies:
            if enemy.colliderect(self.player.rectangle):
                self.enemy.enemies.remove(enemy)
                self.player.health -= self.health_drop
                SoundTrack.playerhit()

        # Determines if the lava floor collided with player.
        if self.lava.rectangle.colliderect(self.player.rectangle):
            self.player.rectangle.y += 5

        # Determines if player collided with heart object.
        for heart in self.heart.heart_rectangle_objects:
            if heart.colliderect(self.player.rectangle):
                if self.player.health != 100:
                    self.player.health += 25
                self.heart.heart_rectangle_objects.remove(heart)
                SoundTrack.collect()
                self.heart_timer += randint(500, 15000)

    def game_over(self, score: list):
        '''This function determines the game lost'''
        # Prints losing font
        if self.player.health <= 0 or self.player.rectangle.y > HEIGHT - 50:
            game_over_font = self.bigfont.render(
                f'You have lost!', True, (255, 255, 255))
            WIN.blit(game_over_font, (WIDTH/2.7, HEIGHT/2.2))

            # Prints score front
            score_font = self.font.render(
                f'Your score: {score[0]}', True, (255, 255, 255))
            WIN.blit(score_font, (WIDTH/2.52, HEIGHT/1.95))
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.quit()

    def draw(self, score):
        '''This function prints every object to the screen'''

        # Prints the animated background
        WIN.blit(self.background.background_image, (0, 0))
        self.background.update()

        # Prints player1 health.
        player_health_font = self.font.render(
            f'Health: {self.player.health}', True, (255, 255, 255))
        WIN.blit(player_health_font, (WIDTH - 185, 0))

        # Prints total score.
        score_font = self.font.render(
            f'Score: {score[0]}', True, (255, 255, 255))
        WIN.blit(score_font, (15, 0))

        # Prints player1 img with the player1 rectangle.
        WIN.blit(self.player.img,
                 (self.player.rectangle.x, self.player.rectangle.y))

        # Print each falling enenmies to the screen.
        for enemy in self.enemy.enemies:
            WIN.blit(self.enemy.img, (enemy.x, enemy.y))

        # Prints falling heart object to the screen.
        self.heart.heart_drop = True
        if len(self.heart.heart_rectangle_objects) == 1:
            for heart in self.heart.heart_rectangle_objects:
                WIN.blit(self.heart.current_img, (heart.x, heart.y))
                self.heart.update()
                if score[0] > self.heart_timer:
                    heart.y += 5
                    if heart.y > HEIGHT:
                        self.heart_timer += randint(500, 15000)
                        self.heart.heart_rectangle_objects.remove(heart)
                        self.heart.heart_drop = False

        # Prints lava if player isn't moving for 4 seconds. 
        # Disabled due to couple changes I made, and don't have the time to fix it.
        # if self.count == 0:
        #     self.rx, self.ry = self.get_player_current_position()
        #     self.count += 1
        # self.get_current_position = False
        # if self.get_frame_time() - self.player.not_moving > 10000 and self.get_frame_time() > 4000:
        #     self.get_current_position = True
        #     self.lava.rectangle.x = self.player.rectangle.x
        #     self.lava.rectangle.y = self.player.rectangle.y
        #     WIN.blit(self.lava.image,
        #              (0, self.ry + 152))
        #     self.lava.update()
        # if self.get_current_position == False:
        #     self.count = 0
            

        # Prints our Exploding animation in a certain condition

        for enemy in self.explode_enemy:
            if self.animated_explosion.is_exploding == True:
                WIN.blit(self.animated_explosion.explosion_image,
                         (enemy.x - 20, enemy.y))
                self.animated_explosion.update()
                if self.animated_explosion.is_exploding == False:
                    self.explode_enemy.clear()

        # Print every player1 bullets to the screen.
        for b in self.player.bullets:
            WIN.blit(self.bullet_img, (b.x, b.y))

        # Updates everything on screen
        pygame.display.update()

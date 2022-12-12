import pygame
from consts import *
from player import Player
from enemy import Enemy
from screen import Screen
from soundtracks import SoundTrack
from floor import Lava
from animated import Heart
import cv2
import multiprocessing
import time
from HandTrackerModule import handDetector
import math


pygame.init()
pygame.display.set_caption(GAME_NAME)


def hand_tracker(hand_pos_x, thumb_finger_collide):
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    detector.maxHands = 1
    pTime = 0

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        if len(lmList) != 0:
            if lmList[0][0] != False:
                hand_pos_x.value = 299
            else:
                hand_pos_x.value = lmList[0][1]

            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]

            thumb_finger_collide.value = math.hypot(x2 - x1, y2 - y1)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
        cv2.imshow("Image", cv2.flip(img, 1))
        cv2.waitKey(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def game(hand_pos_x, thumb_finger_collide):
    clock = pygame.time.Clock()
    score = [0]
    launcher = Player(LAUNCHER_IMG, 97, 100, (WIDTH, HEIGHT))
    heart = Heart(90, 80)
    rock = Enemy(ROCK_IMG, 5)
    lava = Lava(WIDTH + 20, 200) 
    main = Screen(WIN, launcher, BULLET_IMG, rock, lava, heart)
    hand_pos_x.value = 299
    main.start()
    count = 0
    SoundTrack.background()
    shooting = False
    bullet_delay = 0
    while True:
        clock.tick(FPS)
        main.get_frame_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main.save_score(score)
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(launcher.bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        launcher.rectangle.x + 20, launcher.rectangle.y, 100, 100)
                    launcher.bullets.append(bullet)
                    SoundTrack.gunshot()

        if hand_pos_x.value in range(0, 298) and launcher.rectangle.x < WIDTH - 120:
            launcher.rectangle.x += 5

        if hand_pos_x.value in range(300, 650) and launcher.rectangle.x > 0:
            launcher.rectangle.x -= 5

        if shooting == False and thumb_finger_collide:
            if thumb_finger_collide.value < 30 and len(launcher.bullets) < MAX_BULLETS:
                bullet = pygame.Rect(launcher.rectangle.x + 20,
                                     launcher.rectangle.y, 100, 100)
                launcher.bullets.append(bullet)
                SoundTrack.gunshot()
                bullet_delay = pygame.time.get_ticks()
                shooting = True
        if pygame.time.get_ticks() - bullet_delay > 150:
            shooting = False

        if count == 0:
            if score[0] > 3500:
                SoundTrack.second_background()
                count += 1

        launcher.handle_movement(pygame.key.get_pressed())
        heart.spawn()
        rock.spawn()
        rock.handle_enemy()
        rock.despawn()
        launcher.handle_bullet()
        main.onCollision(score)
        main.draw(score)
        rock.levelup(score)
        main.game_over(score)


if __name__ == "__main__":
    hand_pos_x = multiprocessing.Value("d", 0.0, lock=False)
    thumb_finger_collide = multiprocessing.Value("d", 0.0, lock=False)
    hand_tracking_process = multiprocessing.Process(
        target=hand_tracker, args=[hand_pos_x, thumb_finger_collide])
    hand_tracking_process.start()
    game(hand_pos_x, thumb_finger_collide)
    hand_tracking_process.terminate()
    pygame.quit()



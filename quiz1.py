import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Imelda\'s Quiz')

def display_message(text):
    message = FONT.render(text, True, (0, 0, 0))
    screen.blit(message, (WIDTH//2 - message.get_width()//2, HEIGHT//2 - message.get_height()//2))
    pygame.display.flip()

def main():
    score = 0
    total_questions = 3

    display_message("What is your favorite programming language?")
    pygame.display.flip()
    pygame.time.wait(1000)
    answer = input("What is your favorite programming language?: ")

    if answer.lower() == 'python':
        score += 1

    display_message("Are you a student at IGS?")
    pygame.display.flip()
    pygame.time.wait(1000)
    answer = input("Are you a student at IGS?: ")

    if answer.lower() == 'yes':
        score += 1

    display_message("What is Imelda's age?")
    pygame.display.flip()
    pygame.time.wait(1000)
    answer = input("What is Imelda's age?: ")

    if answer == '15':
        score += 1

    display_message(f"Thank you for playing this small quiz game! You answered {score} questions correctly!")
    mark = (score / total_questions) * 100
    print(f"Marks obtained: {mark}")
    display_message("Press any key to exit.")

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

if __name__ == "__main__":
    main()

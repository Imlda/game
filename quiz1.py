import pygame
import sys
from pygame_menu import Menu, themes

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Imelda's Quiz")

def display_message(text):
    message = FONT.render(text, True, (0, 0, 0))
    screen.fill(WHITE)
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
    pygame.display.flip()

def main():
    score = 0
    total_questions = 3

    questions = [
        "What is your favorite programming language?",
        "Are you a student at IGS?",
        "What is Imelda's age?"
    ]

    for question in questions:
        display_message(question)

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Check for Enter key
                        waiting_for_input = False

        pygame.time.wait(1000)

        display_message("Type your answer:")

        menu = Menu(WIDTH, HEIGHT, 'Menu', theme=themes.THEME_DARK)

        text_input = menu.add_text_input('Answer: ', textinput_id='answer', input_type=pygame_menu.locals.INPUT_TEXT, align=pygame_menu.locals.ALIGN_LEFT)

        menu.mainloop(screen)

        answer = text_input.get_value()

        if question.lower() == "What is your favorite programming language?".lower() and answer.lower() == 'python':
            score += 1
        elif question.lower() == "Are you a student at IGS?".lower() and answer.lower() == 'yes':
            score += 1
        elif question.lower() == "What is Imelda's age?".lower() and answer == '15':
            score += 1

    display_message(f"Thank you for playing this small quiz game! You answered {score} questions correctly!")
    mark = (score / total_questions) * 100
    print(f"Marks obtained: {mark}")
    display_message("Press any key to exit.")

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting_for_input = False

if __name__ == "__main__":
    main()

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Imelda's Quiz")

questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: ",
    "What is the capital of France?: ",
    "Who wrote 'Romeo and Juliet'?: ",
    "What is the largest ocean on Earth?: ",
    "In which year did World War II end?: ",
    "What is the currency of Japan?: ",
    "Who painted the Mona Lisa?: ",
    "What is the speed of light?: ",
    "Which element has the chemical symbol 'H'?: ",
    "What is the largest mammal in the world?: ",
    "Who is known as the 'Father of Computer Science'?: ",
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
    ("A. Paris", "B. Berlin", "C. London", "D. Rome"),
    ("A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. J.K. Rowling"),
    ("A. Pacific Ocean", "B. Atlantic Ocean", "C. Indian Ocean", "D. Southern Ocean"),
    ("A. 1944", "B. 1945", "C. 1946", "D. 1950"),
    ("A. Yen", "B. Won", "C. Ringgit", "D. Baht"),
    ("A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"),
    ("A. 299,792 kilometers per second", "B. 100,000 kilometers per second", "C. 500,000 kilometers per second", "D. 1,000,000 kilometers per second"),
    ("A. Hydrogen", "B. Helium", "C. Oxygen", "D. Carbon"),
    ("A. Blue Whale", "B. Elephant", "C. Giraffe", "D. Polar Bear"),
    ("A. Alan Turing", "B. Bill Gates", "C. Steve Jobs", "D. Mark Zuckerberg"),
)

answers = (
    "C", "D", "A", "A", "B", "A", "A", "A", "B", "A", "C", "A", "A",
)

question_num = 0
guesses = []
score = 0

on_home_page = True
game_running = False

while on_home_page:
    screen.fill(WHITE)

    title_text = FONT.render("Imelda's Quiz", True, (0, 0, 0))
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))

    start_text = FONT.render("Press SPACE to start the Quiz", True, (0, 0, 0))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on_home_page = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            on_home_page = False
            game_running = True

while game_running:
    screen.fill(WHITE)

    if question_num < len(questions) and question_num < len(answers):
        question_text = FONT.render(questions[question_num], True, (0, 0, 0))
        screen.blit(question_text, (WIDTH // 2 - question_text.get_width() // 2, HEIGHT // 4))

        option_y = HEIGHT // 2
        for option in options[question_num]:
            option_text = FONT.render(option, True, (0, 0, 0))
            screen.blit(option_text, (WIDTH // 2 - option_text.get_width() // 2, option_y))
            option_y += 40

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    guess = 'A'
                elif event.key == pygame.K_b:
                    guess = 'B'
                elif event.key == pygame.K_c:
                    guess = 'C'
                elif event.key == pygame.K_d:
                    guess = 'D'
                else:
                    guess = ''

                if guess:
                    guesses.append(guess)
                    if guess == answers[question_num]:
                        score += 1

                    question_num += 1

        if question_num == len(questions):
            game_running = False
    else:
        game_running = False

screen.fill(WHITE)
result_text = FONT.render("----------------------\n       RESULTS        \n----------------------", True, (0, 0, 0))
screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 4))

answers_text = FONT.render("Answers: " + " ".join(answers), True, (0, 0, 0))
screen.blit(answers_text, (WIDTH // 2 - answers_text.get_width() // 2, HEIGHT // 2))

guesses_text = FONT.render("Guesses: " + " ".join(guesses), True, (0, 0, 0))
screen.blit(guesses_text, (WIDTH // 2 - guesses_text.get_width() // 2, HEIGHT // 2 + 40))

score_percentage = int(score / len(questions) * 100)
score_text = FONT.render(f"Your score is: {score_percentage}%", True, (0, 0, 0))
screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 80))

pygame.display.flip()

waiting_for_input = True
while waiting_for_input:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting_for_input = False
            game_running = False
        elif event.type == pygame.KEYDOWN:
            waiting_for_input = False

pygame.quit()
sys.exit()

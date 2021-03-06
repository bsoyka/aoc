from typing import Dict

answers: Dict[str, str] = {
    'Rock': 'Paper',
    'Paper': 'Scissors',
    'Scissors': 'Rock',
    'Fox': 'Foxen',
}

for _ in range(int(input())):
    choice = input()

    if choice == 'Foxen':
        break

    print(answers[choice])

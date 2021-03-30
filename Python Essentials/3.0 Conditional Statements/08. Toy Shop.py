trip, puzzle, doll, bear, minion, truck = [float(input()) for _ in range(6)]
toys_count = puzzle + doll + bear + minion + truck
toys_total = (puzzle * 2.60) + (doll * 3) + (bear * 4.1) + (minion * 8.20) + (truck * 2)

if toys_count >= 50:
    toys_total *=  0.75
toys_total *= 0.90

if toys_total >= trip:
    print(f'Yes! {(toys_total - trip):.2f} lv left.')
else:
    print(f'Not enough money! {(trip - toys_total):.2f} lv needed.')


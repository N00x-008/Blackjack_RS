import random
import tkinter as tk
from tkinter import messagebox

turn = 1
cards_p1 = []
cards_p2 = []


def random_number():
    return random.randint(1, 11)


def card():
    sign = random.choice(["♥", "♦", "♠", "♣"])
    value = random_number()
    print("Obtuviste:", value, sign)
    return value, sign


# show cards and total
def show_cards(cards, label_cards, label_total):
    lines = ["", "", "", "", ""]
    for value, sign in cards:
        val_str = str(value).ljust(2)
        lines[0] += " ----- "
        lines[1] += f"|{val_str}   | "
        lines[2] += f"|  {sign}  | "
        lines[3] += f"|   {val_str}| "
        lines[4] += " ----- "
    ascii = "\n".join(lines)
    label_cards.config(text=ascii, font=("Courier", 12))
    total = sum(v for v, s in cards)
    label_total.config(text=f"Total: {total}")


# ask card function
def ask_card():
    global turn
    new_card = card()

    if turn == 1:
        cards_p1.append(new_card)
        show_cards(cards_p1, lbl_p1_cards, lbl_p1_total)
        if sum(v for v, _ in cards_p1) >= 21 or len(cards_p1) >= 5:
            skip()
    else:
        cards_p2.append(new_card)
        show_cards(cards_p2, lbl_p2_cards, lbl_p2_total)
        if sum(v for v, _ in cards_p2) >= 21 or len(cards_p2) >= 5:
            end_game()


# skip turn
def skip():
    global turn, cards_p2
    if turn == 1:
        turn = 2
        lbl_turn.config(text="turno: jugador 2")
        cards_p2 = [card(), card()]
        show_cards(cards_p2, lbl_p2_cards, lbl_p2_total)
    else:
        end_game()


# turn of player 1
def start_turn():
    global cards_p1
    cards_p1 = [card(), card()]
    show_cards(cards_p1, lbl_p1_cards, lbl_p1_total)


# ending of the game
def end_game():
    btn_card.config(state="disabled")
    btn_skip.config(state="disabled")

    total_p1 = sum(v for v, _ in cards_p1)
    total_p2 = sum(v for v, _ in cards_p2)

    result = f"P1: {total_p1} | P2: {total_p2}\n"

    if total_p1 > 21:
        result += "jugador 1 se pasó. ¡Gana jugador 2!"
    elif total_p2 > 21:
        result += "jugador 2 se pasó. ¡Gana jugador 1!"
    elif total_p1 > total_p2:
        result += "¡Gana jugador 1!"
    elif total_p2 > total_p1:
        result += "¡Gana jugador 2!"
    else:
        result += "¡Empate!"

    messagebox.showinfo("Resultado", result)


def restart():
    global turn, cards_p1, cards_p2
    turn = 1
    cards_p1 = []
    cards_p2 = []
    lbl_turn.config(text="Turno: Jugador 1")
    lbl_p1_cards.config(text="")
    lbl_p2_cards.config(text="")
    lbl_p1_total.config(text="Total: 0")
    lbl_p2_total.config(text="Total: 0")
    btn_card.config(state="normal")
    btn_skip.config(state="normal")
    start_turn()


window = tk.Tk()
window.title("Blackjack - ¡21!")

tk.Label(window, text="Blackjack", font=("Arial", 20, "bold")).pack(pady=10)

lbl_turn = tk.Label(window, text="turno: jugador 1", font=("Arial", 14))
lbl_turn.pack()

# player 1
frame_p1 = tk.LabelFrame(window, text="jugador 1", padx=10, pady=10)
frame_p1.pack(padx=10, pady=5, fill="x")

lbl_p1_cards = tk.Label(frame_p1, text="", font=("Courier", 14))
lbl_p1_cards.pack()
lbl_p1_total = tk.Label(frame_p1, text="Total: 0", font=("Arial", 12))
lbl_p1_total.pack()

# player 2
frame_p2 = tk.LabelFrame(window, text="jugador 2", padx=10, pady=10)
frame_p2.pack(padx=10, pady=5, fill="x")

lbl_p2_cards = tk.Label(frame_p2, text="", font=("Courier", 14))
lbl_p2_cards.pack()
lbl_p2_total = tk.Label(frame_p2, text="Total: 0", font=("Arial", 12))
lbl_p2_total.pack()

# buttons
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

btn_card = tk.Button(frame_buttons, text="pedir una carta", width=12, command=ask_card)
btn_card.grid(row=0, column=0, padx=10)

btn_skip = tk.Button(frame_buttons, text="pasar", width=12, command=skip)
btn_skip.grid(row=0, column=1, padx=10)

btn_restart = tk.Button(window, text="reiniciar el juego", command=restart)
btn_restart.pack(pady=5)

tk.Label(
    window,
    text="Kimberly Sujey Reyes Sandoval - 1D entornos virtuales y negocios digitales BIS",
    font=("Arial", 12),
).pack(pady=20)
start_turn()
window.mainloop()

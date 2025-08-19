import random
import tkinter as tk
from tkinter import messagebox

# Variables globales
turno = 1
cartas_p1 = []
cartas_p2 = []


# Funciones básicas
def aleatorio():
    return random.randint(1, 11)


def carta():
    signo = random.choice(["♥", "♦", "♠", "♣"])
    valor = aleatorio()
    print("You got:", valor, signo)
    return valor, signo


# Mostrar cartas y total
def mostrar_cartas(cards, label_cards, label_total):
    lines = ["", "", "", "", ""]
    for value, sign in cards:
        val_str = str(value).ljust(2)
        lines[0] += " ----- "
        lines[1] += f"|{val_str}   | "
        lines[2] += f"|  {sign}  | "
        lines[3] += f"|   {val_str}| "
        lines[4] += " ----- "
    ascii_text = "\n".join(lines)
    label_cards.config(text=ascii_text, font=("Courier", 12))
    total = sum(v for v, s in cards)
    label_total.config(text=f"Total: {total}")


# Función de pedir carta
def pedir_carta():
    global turno
    nueva = carta()

    if turno == 1:
        cartas_p1.append(nueva)
        mostrar_cartas(cartas_p1, lbl_p1_cartas, lbl_p1_total)
        if sum(v for v, _ in cartas_p1) >= 21 or len(cartas_p1) >= 5:
            pasar()
    else:
        cartas_p2.append(nueva)
        mostrar_cartas(cartas_p2, lbl_p2_cartas, lbl_p2_total)
        if sum(v for v, _ in cartas_p2) >= 21 or len(cartas_p2) >= 5:
            finalizar_juego()


# Función de pasar turno
def pasar():
    global turno, cartas_p2
    if turno == 1:
        turno = 2
        lbl_turno.config(text="Turno: Jugador 2")
        cartas_p2 = [carta(), carta()]
        mostrar_cartas(cartas_p2, lbl_p2_cartas, lbl_p2_total)
    else:
        finalizar_juego()


# Función para empezar el turno del jugador 1
def iniciar_turno():
    global cartas_p1
    cartas_p1 = [carta(), carta()]
    mostrar_cartas(cartas_p1, lbl_p1_cartas, lbl_p1_total)


# Función para finalizar el juego
def finalizar_juego():
    btn_carta.config(state="disabled")
    btn_pasar.config(state="disabled")

    total_p1 = sum(v for v, _ in cartas_p1)
    total_p2 = sum(v for v, _ in cartas_p2)

    resultado = f"P1: {total_p1} | P2: {total_p2}\n"

    if total_p1 > 21:
        resultado += "Jugador 1 se pasó. ¡Gana Jugador 2!"
    elif total_p2 > 21:
        resultado += "Jugador 2 se pasó. ¡Gana Jugador 1!"
    elif total_p1 > total_p2:
        resultado += "¡Gana Jugador 1!"
    elif total_p2 > total_p1:
        resultado += "¡Gana Jugador 2!"
    else:
        resultado += "¡Empate!"

    messagebox.showinfo("Resultado", resultado)


# Función para reiniciar el juego
def reiniciar():
    global turno, cartas_p1, cartas_p2
    turno = 1
    cartas_p1 = []
    cartas_p2 = []
    lbl_turno.config(text="Turno: Jugador 1")
    lbl_p1_cartas.config(text="")
    lbl_p2_cartas.config(text="")
    lbl_p1_total.config(text="Total: 0")
    lbl_p2_total.config(text="Total: 0")
    btn_carta.config(state="normal")
    btn_pasar.config(state="normal")
    iniciar_turno()


# ---------------- INTERFAZ ----------------

ventana = tk.Tk()
ventana.title("Blackjack - ¡21!")

tk.Label(ventana, text="Blackjack", font=("Arial", 20, "bold")).pack(pady=10)

lbl_turno = tk.Label(ventana, text="Turno: Jugador 1", font=("Arial", 14))
lbl_turno.pack()

# Jugador 1
frame_p1 = tk.LabelFrame(ventana, text="Jugador 1", padx=10, pady=10)
frame_p1.pack(padx=10, pady=5, fill="x")

lbl_p1_cartas = tk.Label(frame_p1, text="", font=("Courier", 14))
lbl_p1_cartas.pack()
lbl_p1_total = tk.Label(frame_p1, text="Total: 0", font=("Arial", 12))
lbl_p1_total.pack()

# Jugador 2
frame_p2 = tk.LabelFrame(ventana, text="Jugador 2", padx=10, pady=10)
frame_p2.pack(padx=10, pady=5, fill="x")

lbl_p2_cartas = tk.Label(frame_p2, text="", font=("Courier", 14))
lbl_p2_cartas.pack()
lbl_p2_total = tk.Label(frame_p2, text="Total: 0", font=("Arial", 12))
lbl_p2_total.pack()

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_carta = tk.Button(frame_botones, text="Pedir Carta", width=12, command=pedir_carta)
btn_carta.grid(row=0, column=0, padx=10)

btn_pasar = tk.Button(frame_botones, text="Pasar", width=12, command=pasar)
btn_pasar.grid(row=0, column=1, padx=10)

btn_reiniciar = tk.Button(ventana, text="Reiniciar Juego", command=reiniciar)
btn_reiniciar.pack(pady=5)

tk.Label(
    ventana, text="Kimberly Sujey Reyes Sandoval - 1D ITIID BIS", font=("Arial", 12)
).pack(pady=20)
iniciar_turno()
ventana.mainloop()

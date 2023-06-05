from señales_calc import *
import tkinter
from tkinter import *

# V E N T A N A
alto = 700
ancho = 1200

root = Tk()
root.resizable(False, False)
root.title("Serie de Fourier")
root.iconbitmap("Waves_icon.ico")
root.config(bg="antique white")

# I M A G E N E S
ond_cuad = PhotoImage(file="Imagenes/onda_cuad.png")
ond_trian = PhotoImage(file="Imagenes/onda_trian.png")
ond_escal = PhotoImage(file="Imagenes/onda_escal.png")

# variables
columnas = 7

# G R A F I C A
fig, ax = plt.subplots(dpi=90, figsize=(15, 5), facecolor="#faebd7")
plt.title("Serie de Fourier", color="black", size=20, family="Arial")

plt.xlim(0, 2)
plt.ylim(1.5, -1.5)
ax.set_facecolor("white")
ax.axhline(linewidth=2, color="r")
ax.axvline(linewidth=2, color="r")
ax.set_xlabel("Tiempo (seg)", color="black")
ax.set_ylabel("Amplitud", color="black")
ax.grid(True)
ax.tick_params(direction="out", length=6, width=2, colors="black", grid_color="r", grid_alpha=0.5)
fig.tight_layout()


def Decidsenal(tipo):
    k = scale_const.get()
    duration = 2.0  # Duración en segundos
    sampling_freq = 44100  # Frecuencia de muestreo en Hz
    num_samples = int(duration * sampling_freq)
    t = np.linspace(0, duration, num_samples)
    lconst.config(text=k, font=("Arial", 18))

    freq = 5

    if tipo == 1:
        print("Onda Cuadrada")
        senal = generar_cuadrada(t, freq, k)
        graficar_Fourier(t, senal)

    elif tipo == 2:
        print("Onda Triangular")
        senal = generar_triangular(t, freq, k)
        graficar_Fourier(t, senal)

    elif tipo == 3:
        print("Onda Dientes de Sierra")
        senal = generar_d_sierra(t, freq, k)
        graficar_Fourier(t, senal)


def graficar_Fourier(t, senal):
    fig, ax = plt.subplots(dpi=90, figsize=(15, 5), facecolor="#faebd7")
    plt.title("Serie de Fourier", color="black", size=20, family="Arial")

    plt.xlim(0, 2)
    plt.ylim(1.5, -1.5)

    ax.set_facecolor("white")
    ax.axhline(linewidth=2, color="r")
    ax.axvline(linewidth=2, color="r")

    ax.plot(t, senal)
    ax.set_xlabel("Tiempo (seg)", color="black")
    ax.set_ylabel("Amplitud", color="black")
    ax.grid(True)
    ax.tick_params(direction="out", length=6, width=2, colors="black", grid_color="r", grid_alpha=0.5)
    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=1, columnspan=columnas, padx=5, pady=5)


# F R A M E para almacenar la gráfica
frame = Frame(root, bg="antique white")
frame.grid(column=0, row=0)

# C A N V A S
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().grid(column=0, row=1, columnspan=columnas, padx=5, pady=5)

lconst = Label(frame)
lconst.config(width="15")
lconst.grid(column=1, row=0, pady=5)

lblconstante = Label(frame, text="K=")
lblconstante.grid(row=0, column=1, pady=5, columnspan=2)
lblconstante.config(font=("Arial", 18), justify=RIGHT, bg="antique white")

scale_const = Scale(frame, to=100, from_=1, orient="horizontal", length=800)
scale_const.grid(row=0, column=1, pady=5, columnspan=2)

b1 = tkinter.Button(frame, image=ond_cuad, command=lambda: Decidsenal(1))
b1.config(bg="linen")
b1.grid(column=0, row=2, pady=5)
lb1 = Label(frame, text="Onda Cuadrada")
lb1.grid(row=3, column=0, pady=5)
lb1.config(font=("Arial", 18), justify=CENTER, bg="antique white")

b2 = tkinter.Button(frame, image=ond_trian, command=lambda: Decidsenal(2))
b2.config(bg="linen")
b2.grid(column=1, row=2, pady=5)
lb2 = Label(frame, text="Onda Triangular")
lb2.grid(row=3, column=1, pady=5)
lb2.config(font=("Arial", 18), justify=CENTER, bg="antique white")

b3 = tkinter.Button(frame, image=ond_escal, command=lambda: Decidsenal(3))
b3.config(bg="linen")
b3.grid(column=2, row=2, pady=5)
lb3 = Label(frame, text="Onda Dientes de Sierra")
lb3.grid(row=3, column=2, pady=5)
lb3.config(font=("Arial", 18), justify=CENTER, bg="antique white")

for r in range(0, 5):
    for c in range(0, 5):
        cell = Entry(frame, width=10)
        cell.grid(row=r, column=c)
        cell.insert(0, '({}, {})'.format(r, c))

root.mainloop()

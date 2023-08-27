from tkinter import *
from tkinter import filedialog
import pygame


window = Tk()

icon = PhotoImage(file="iconplay2.png")

window.geometry("420x420")
window.title("MiniPlayer")
window.iconphoto(False, icon)



pygame.mixer.init()

def adicionar_musica():
    musica = filedialog.askopenfilename(initialdir="audio/",filetypes=(("mp3 Files", "*.mp3"),))
    musica = musica.replace("C:/Users/Mateus/Downloads/", "")
    listareproducao.insert(END, musica)
def deletar_som():
    listareproducao.delete(ANCHOR)
    pygame.mixer.music.stop()
def deletar_tudo():
    listareproducao.delete(0, END)
    pygame.mixer.music.stop()

def sair():
    window.destroy()
def play():
    try:
        musica = listareproducao.get(ACTIVE)
        musica = f"C:/Users/Mateus/Downloads/{musica}"
        pygame.mixer.music.load(musica)
        pygame.mixer.music.play(loops=0)
    except:
        pass
def pause():
    try:
        musica = listareproducao.get(ACTIVE)
        musica = f"C:/Users/Mateus/Downloads/{musica}"
        pygame.mixer.music.load(musica)
        pygame.mixer.music.stop()
    except:
        pass
def skip():
    proxima_musica = listareproducao.curselection()
    proxima_musica = proxima_musica[0] + 1
    musica = listareproducao.get(proxima_musica)
    musica = f"C:/Users/Mateus/Downloads/{musica}"
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play(loops=0)

    listareproducao.selection_clear(0, END)
    listareproducao.activate(proxima_musica)
    listareproducao.selection_set(proxima_musica, last=None)
def back():
    proxima_musica = listareproducao.curselection()
    proxima_musica = proxima_musica[0] - 1
    musica = listareproducao.get(proxima_musica)
    musica = f"C:/Users/Mateus/Downloads/{musica}"
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play(loops=0)

    listareproducao.selection_clear(0, END)
    listareproducao.activate(proxima_musica)
    listareproducao.selection_set(proxima_musica, last=None)

canvas = Canvas(window,)
canvas.create_rectangle(0,0,400,550,fill="purple")
canvas.pack()


barramenu = Menu(window)
window.config(menu=barramenu)

MenuAdicionar = Menu(barramenu, tearoff=0)

barramenu.add_cascade(label="Config",menu=MenuAdicionar)

MenuAdicionar.add_command(label="Adicionar",command=adicionar_musica)

MenuAdicionar.add_command(label="Deletar Som",command=deletar_som)

MenuAdicionar.add_command(label="Deletar Todos os Sons",command=deletar_tudo)

MenuAdicionar.add_command(label="Sair",command=sair)

listareproducao = Listbox(canvas,width=50,height=20,bg="black",fg="cyan")
listareproducao.pack(pady=10)







frame = Frame(window)
frame.pack()

play_icone = PhotoImage(file="play3.png")
play_icone = play_icone.zoom(12)
play_icone = play_icone.subsample(30)
botao_play = Button(frame, command=play, image=play_icone, borderwidth=0)
botao_play.grid(row=0, column=1)

pause_icone = PhotoImage(file="stop.png")
pause_icone = pause_icone.zoom(12)
pause_icone = pause_icone.subsample(30)
botao_pause = Button(frame, command=pause, image=pause_icone, borderwidth=0)
botao_pause.grid(row=0, column=2)

previous_icone = PhotoImage(file="previous.png")
previous_icone = previous_icone.zoom(12)
previous_icone = previous_icone.subsample(30)
botao_previous = Button(frame, command=back, image=previous_icone, borderwidth=0)
botao_previous.grid(row=0, column=0)

skip_icone = PhotoImage(file="skip2.png")
skip_icone = skip_icone.zoom(12)
skip_icone = skip_icone.subsample(30)
botao_skip = Button(frame, command=skip, image=skip_icone, borderwidth=0)
botao_skip.grid(row=0, column=3)






window.mainloop()
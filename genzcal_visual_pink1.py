import customtkinter as ctk


#Configuración

ctk.set_appearance_mode("light")

#Ventana

app =ctk.CTk()
app.title("Gen Z Calculator")
app.geometry("400x600")

app.configure(
    fg_color="#FFE6F2"
)

#Variables

operacion = ""

#Funciones

def agregar(valor):
    global operacion

    operacion += str(valor)

    pantalla.configure(
        text=operacion
    )

def limpiar():
    global operacion

    operacion = ""

    pantalla.configure(
        text="0"
    )    

def calcular():
    global operacion
    
    try:

        resultado = eval(operacion)

        pantalla.configure(
            text=str(resultado)
        )

        operacion = str(resultado)

    except:

        pantalla.configure(
            text="No mames MariaJose"
        )    

        operacion = ""

#Titulo

titulo = ctk.CTkLabel(
    app,
    text="Gen Z Calculator",
    font=("Arial", 22, "bold"),
    text_color="#A13D6D"
)

titulo.pack(
    pady=20
)


#Pantalla

pantalla = ctk.CTkLabel(

    app,

    text="0",

    width=320,

    height=90,

    font=("Arial", 35, "bold"),

    fg_color="#FFD1E6",

    text_color="#8B2F5C",

    corner_radius=25

)

pantalla.pack(
    pady=10
)


#Marco botones

frame = ctk.CTkFrame(
    app,
    fg_color="#FFE6F2"
)

frame.pack(
    pady=20
)

#Botones Numericos

botones = [
    ("7",0,0),
    ("8",0,1),
    ("9",0,2),
    ("/",0,3),

    ("4",1,0),
    ("5",1,1),
    ("6",1,2),
    ("*",1,3),

    ("1",2,0),
    ("2",2,1),
    ("3",2,2),
    ("-",2,3),

    ("0",3,0),
    (".",3,1),
    ("+",3,2),

]

for texto, fila, columna in botones:

    boton = ctk.CTkButton(

        frame,

        text=texto,

        width=70,

        height=60,

        font=("Arial", 20, "bold"),

        fg_color="#FF9FCb",

        hover_color="#FF6FAE",

        text_color="white",

        corner_radius=18,

        command=lambda t=texto: agregar(t)

    )

    boton.grid(

    row=fila,

    column=columna,

    padx=6,

    pady=6

    )


#Igual

igual = ctk.CTkButton(

    frame,

    text="=",

    width=70,

    height=60,

    font=("Arial", 20, "bold"),

    fg_color="#FF5FA2",

    hover_color="#E94B8C",

    text_color="white",

    corner_radius=18,

    command=calcular

)

igual.grid(

    row=3,

    column=3,

    padx=6,

    pady=6
)


#Limpiar

clear = ctk.CTkButton(

    app,

    text="Clear",

    width=160,

    height=45,

    font=("Arial", 16, "bold"),

    fg_color="#FFC0CB",

    hover_color="#FF8FAB",

    text_color="#8B2F5C",

    corner_radius=20,

    command=limpiar

)

clear.pack(
    pady=20
)


#Ejecutar

app.mainloop()
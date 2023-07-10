import sqlite3
import pygame
from colores import *

def crear_base_de_datos():
    with sqlite3.connect("Recuperar/bd_score.db") as conexion:
        try:
            sentencia = ''' create  table puntajes
            (
            id integer primary key autoincrement,
            nombre text,
            score integer
            )
            '''
            conexion.execute(sentencia)
            print("Se creo la tabla puntajes")                       
        except sqlite3.OperationalError:
            print("La tabla puntajes ya existe")
            
def insertar_nombre_score(nombre:str, score:int):
    with sqlite3.connect("Recuperar/bd_score.db") as conexion:    
        try:
            conexion.execute("insert into puntajes(nombre,score) values (?,?)", (nombre, score)) 
            conexion.commit()
        except:
            print("Error. Vuelve a intentarlo.")


def ranking():
    with sqlite3.connect("Recuperar/bd_score.db") as conexion:
        cursor = conexion.execute("SELECT id, nombre, score FROM puntajes ORDER BY score DESC")
        lista = cursor.fetchall()
        if len(lista) > 5: 
            for index,element in enumerate(lista):
                if index > 4:
                    sentencia = "DELETE FROM puntajes WHERE id= (?)"
                    id = lista[index][0]
                    caso = conexion.execute(sentencia, (id,))
                    conexion.commit()
        


pygame.init()
top_img = pygame.image.load("Recuperar/imagenes/top.png")#llamo a la imagen
top_img = pygame.transform.scale(top_img,(678,720))
#screen = pygame.display.set_mode((800, 600))
def pantalla_puntajes(screen):

    # Establecer conexión con la base de datos
    conexion = sqlite3.connect("Recuperar/bd_score.db")
    cursor = conexion.cursor()

    # Ejecutar consulta para obtener los datos
    cursor.execute("SELECT id, nombre, score FROM puntajes ORDER BY score DESC")
    resultados = cursor.fetchall()

    # Cerrar la conexión con la base de datos
    conexion.close()

    # Inicializar Pygame
    pygame.init()

    # Configurar la ventana de visualización
    screen = pygame.display.set_mode((1200, 700))

    # Fuente y tamaño del texto
    fuente = pygame.font.SysFont("Arial", 20)

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Llenar la pantalla con un color
        screen.fill(BLANCO)
        screen.blit(top_img,(230,2))
        y = 250
        num = 1
        # Mostrar los datos en pantalla
        for resultado in resultados:
            # Convertir los datos a cadenas de texto
            #texto = ", ".join(str(dato) for dato in resultado)
            nombre = resultado[1]
            score = resultado[2]
            texto = f"#{num}-{nombre} {score}"

            # Renderizar el texto
            texto_renderizado = fuente.render(texto, True, NEGRO)

            # Mostrar el texto en pantalla
            screen.blit(texto_renderizado, (550, y))
            y += 25
            num += 1

        # Actualizar la ventana
        pygame.display.flip()

    # Cerrar Pygame
    pygame.quit()
#pantalla_puntajes(screen)
        


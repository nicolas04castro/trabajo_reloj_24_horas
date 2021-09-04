# trabajo_reloj_24_horas
Código y link de el proyecto de un reloj con minutos, segundos, y horas desarrollado en processing

## Explicación
Se va a presentar el código de un reloj gráfico, sin números, el cual fue desarrollado en processing.

Este código está divido en 3 sección las cuales hacen la representación de un reloj:

La primera sección (parte izquierda) es la sección que representa los segundos, y su fondo cambia progresivamente.
La sección 2 es la que está ubicada en el medio con un color celeste y esta representa los minutos.
La última sección la del lado derecho y representada con un color azul oscuro es la que representa las horas. En esta sección se puede evidenciar un sol y la luna hora en la que se estima sale cada uno el sol cuando amanece y la luna cuando se empieza a oscurecer.

### Codigo desarrollado

vertical_minutes = 0
vertical_position = 0
vertical_hour = 0


def setup():
    size(400, 700)

def draw():

    global vertical_position

    background(map(second(),0,59,0,255))
    noStroke()
    fill(map(second(),0, 59, 255, 0))
    
            
    ellipse(70, vertical_position, 59, 50)
    if vertical_position > height:
        vertical_position = 0
    else:
        vertical_position = map(second(),0,59,0,height)
        
        
    global vertical_minutes
    
    fill(0, 255, 255)    
    rect(140, 0, 120, 700)    
    
    fill(map(minute(),0, 59, 255, 0))
    ellipse(200, vertical_minutes, 59, 50)
    if vertical_minutes > height:
        vertical_minutes = 0
    else:
        vertical_minutes = map(minute(),0,59,0,height)
        
                
    global vertical_hour
    
    fill(0, 0, 139)
    rect(260, 0, 140, 700)
    
    fill(map(hour(),0, 23, 255, 0))
    ellipse(340, vertical_hour, 60, 50)
    if vertical_hour > height:
        vertical_hour = 0
    else:
        vertical_hour = map(hour(),0,23,0,height)


    fill(255, 99, 71)   
    circle(280,200,48) 
    fill(255, 215, 0)    
    circle(280,200,40)    
    
    fill(253, 245, 230)
    circle(280,520,40)
    fill(0, 0, 139)
    circle(290,520,25)
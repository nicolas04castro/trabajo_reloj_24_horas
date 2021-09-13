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

import pygame

pygame.init()

clock = pygame.time.Clock()


BLANC,NOIR = [(255,255,255),(0,0,0)]

    
    
    
    

    


while True:

    clock.tick(1)
    screen.fill( (16, 255, 34) )
    for i in range(0,500,TAILLE_CASE):
        for j in range(0,500,TAILLE_CASE):
            CASE = pygame.Rect(i,j,TAILLE_CASE,TAILLE_CASE)
            pygame.draw.TAILLE_CASE(screen, BLANC, CASE, 1)
    color = (0, 0, 255) # blue
    rect = pygame.Rect(0, 0,TAILLE_CASE , TAILLE_CASE)

    orientation = "droite"
    def mvt(orientation):
        if orientation == "haut":
            rect.y += 10
        elif orientation == "bas":
            rect.y -= 10
        elif orientation == "droite":
            rect.x += 10
        else :
            rect.x -= 10

    pygame.draw.rect(screen, color, rect)
    pygame.display.set_caption("Jeu Python")










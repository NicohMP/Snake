import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))

TAILLE_CASE = 25

while True:
    clock.tick(1)

    BLANC,NOIR = [(255,255,255),(0,0,0)]

    screen.fill( (16, 255, 34) )
    for i in range(0,500,TAILLE_CASE):
        for j in range(i,500+i,2*TAILLE_CASE):
            CASE = pygame.Rect(i,j%500,TAILLE_CASE,TAILLE_CASE)
            pygame.draw.rect(screen, BLANC, CASE)
    
    positions = [(10*TAILLE_CASE,10*TAILLE_CASE),(10*TAILLE_CASE,11*TAILLE_CASE),(10*TAILLE_CASE,12*TAILLE_CASE)]
    color = (0, 0, 255) # blue
    def afficher(positions):
        for coord in positions:
            rect = pygame.Rect(coord[0], coord[1],  TAILLE_CASE, TAILLE_CASE)
            pygame.draw.rect(screen,color,rect)

    orientation = "droite"
    def mvt(orientation):
        if orientation == "haut":
            positions.append((positions[0][0],positions[0][0]-TAILLE_CASE))
        elif orientation == "bas":
            positions.append((positions[0][0],positions[0][0]+TAILLE_CASE))
        elif orientation == "droite":
            positions.append((positions[0][0]+TAILLE_CASE,positions[0][0]))
        else :
            positions.append((positions[0][0]-TAILLE_CASE,positions[0][0]))
        positions.pop(-1)
        afficher(positions)
        print(positions)
    
    pygame.display.set_caption("Jeu Python")

    for event in pygame.event.get():
        if event.type ==pygame.KEYDOWN:
            if event.type == pygame.K_p:
                pygame.quit()
            elif event.key == pygame.K_z:
                orientation = "haut"
            elif event.key == pygame.K_s:
                orientation = "bas"
            elif event.key == pygame.K_q:
                orientation = "gauche"
            elif event.key == pygame.K_d:
                orientation = "droite"
    
    mvt(orientation)
    pygame.display.update()

    pygame.display.flip()
    













pygame.quit()

import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode( (500,500) )
BLANC = (255,255,255)
TAILLE_CASE = 25
positions = [(10*TAILLE_CASE,10*TAILLE_CASE),(10*TAILLE_CASE,11*TAILLE_CASE),(10*TAILLE_CASE,12*TAILLE_CASE)]
orientation = "haut"
while True:

    clock.tick(10)
    screen.fill( (16, 255, 34) )
    for i in range(0,500,TAILLE_CASE):
        for j in range(i,500+i,2*TAILLE_CASE):
            CASE = pygame.Rect(i,j%500,TAILLE_CASE,TAILLE_CASE)
            pygame.draw.rect(screen, BLANC, CASE)
    
    
    color = (0, 0, 255) # couleur du corps
    head_color = (100,100,255)

    def afficher(positions):
        for coord in positions[:-1]:
            rect = pygame.Rect(coord[0], coord[1],  TAILLE_CASE, TAILLE_CASE)
            pygame.draw.rect(screen,color,rect)
        tête = pygame.Rect(positions[-1][0],positions[-1][1],TAILLE_CASE,TAILLE_CASE)
        pygame.draw.rect(screen,head_color,tête)
    

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

        
    def mvt(orientation):
        nouvelle_tête = (0,0)
        if orientation == "haut":
            nouvelle_tête = (positions[-1][0],positions[-1][1]-TAILLE_CASE)
        if orientation == "bas":
            nouvelle_tête = (positions[-1][0],positions[-1][1]+TAILLE_CASE)
        if orientation == "droite":
            nouvelle_tête = (positions[-1][0]+TAILLE_CASE,positions[-1][1])
        if orientation == "gauche" :
            nouvelle_tête = (positions[-1][0]-TAILLE_CASE,positions[-1][1])
        positions.append(nouvelle_tête)
        positions.pop(0)
        afficher(positions)
        print(positions)
    
    pygame.display.set_caption("Jeu Python")
    
    mvt(orientation)
    pygame.display.update()

    pygame.display.flip()
    








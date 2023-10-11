import time
import pygame
import numpy as np

COLOR_BG = '#163850'
 
# dark grey
COLOR_GRID ='#5C6970'
# still dark grey but lighter than the previous one
COLOR_DIE_NEXT ='#FFFF00'
# light grey
COLOR_ALIVE_NEXT ='#FFFF00'
# pure white
SIZE =20

def update(screen,cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    
    for row, col in np.ndindex(cells.shape):
        alive =np.sum(cells[row-1:row+2, col-1:col+2]) -cells[row,col]
        color =COLOR_BG if cells[row,col] == 0 else COLOR_ALIVE_NEXT


        if cells[row,col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color =COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row,col]= 1
                if with_progress:
                    color=COLOR_ALIVE_NEXT
        else:
            if alive ==3:
                updated_cells[row,col] =1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        
        pygame.draw.rect(screen,color, (col * size, row * size, size - 1, size -1))

    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    cells = np.zeros((36, 64))
    screen.fill(COLOR_GRID)
    update(screen, cells, 20)

    pygame.display.flip()
    pygame.display.update()

    running = False
    
    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 20)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 20, pos[0] //20] = 1
                update(screen,cells,20)
                pygame.display.update()

        screen.fill(COLOR_GRID)


        if running:
            cells = update(screen, cells, 20, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)


if __name__ =='__main__':
    main()



 

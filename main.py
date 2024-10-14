import pygame

#  Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))#width, height

#Title and Icon
pygame.display.set_caption("Stack visualizer")
icon = pygame.image.load('layers.png')
pygame.display.set_icon(icon)

display_font = pygame.font.Font('Quicksand-VariableFont_wght.ttf', 20)
title_font = pygame.font.Font('DancingScript-VariableFont_wght.ttf', 20)

#Stack
# stack = ["M&M", "Snickers", "Haribo", "Skittles", "Cardbury", "Mars", "TicTac"]
stack = []
max_size = 7
popped_candies = []

containerX = 300
containerY = 100

candyX = 303
candyY = 360

springX = 390
springY = 403
spring_width = 200
spring_height = 190

is_empty_text = ""
candy_no=1
top_text = ""
len_text = ""
container_full_text = "Add to your Candy dispenser"

def draw_logo():
  candyshopImage = pygame.image.load('candy-shop.png')
  candyshopX = 100
  candyshopY = 20
  screen.blit(candyshopImage, (candyshopX, candyshopY))
  
def draw_spring(screen, x, y, width, height, coils):
  points = []
  amplitude = width // 4 # how far spring will zigzag
  
  for i in range(coils + 1):
    # calculate x and y position for each coil
    y_pos = y + i * (height // coils)
    if i % 2 == 0:
      x_pos = x + amplitude
    else:
      x_pos = x - amplitude
    points.append((x_pos, y_pos))
    
  pygame.draw.lines(screen, (238, 202, 213), False, points, 5)

def draw_button(screen, color, rect, text):
  #Font
  label_font = pygame.font.Font('Dosis-VariableFont_wght.ttf', 25)
  pygame.draw.rect(screen, color, rect, border_radius=28)
  label = label_font.render(text, True, (0, 0, 0))
  label_rect = label.get_rect(center=rect.center)
  screen.blit(label, label_rect)

def draw_container(x, y, width, height):
  #left border
  pygame.draw.line(screen, (209, 233, 246), (x, y), (x, y+height), 5)
  #right border
  pygame.draw.line(screen, (209, 233, 246), (x+width, y), (x+width, y+height), 5)
  #bottom border
  pygame.draw.line(screen, (209, 233, 246), (x, y+height), (x+width, y+height), 5)
  
def draw_candies(stack, candyX, candyY):
  for i in range(len(stack)):
    candy_font = pygame.font.Font('Quicksand-VariableFont_wght.ttf', 20)
    rect  = pygame.Rect(candyX, candyY-i*40, 195, 40)
    pygame.draw.ellipse(screen, (246, 234, 203), rect, 5)
    candy_label = candy_font.render(stack[i], True, (0, 0, 0))
    candy_label_rect = candy_label.get_rect(center=rect.center)
    screen.blit(candy_label, candy_label_rect)
  
def push(stack, candy, candy_no):
  if len(stack) < max_size:
    stack.append(candy + str(candy_no))
  
  draw_candies(stack, candyX, candyY)

def pop(stack):
  if stack:
    return stack.pop()
    
  draw_candies(stack, candyX, candyY)
    
def is_empty(stack):
  return len(stack) == 0
  
def top(stack):
  if(stack):
    return stack[-1]
  
def display_result(screen, text, x, y, font):
  result_label = font.render(text, True, (0, 0, 0))
  screen.blit(result_label, (x, y))

      
# Game loop
running = True
while running:   
  screen.fill((254, 249, 242))
  
  push_button = pygame.Rect(100, 150, 100, 50)
  pop_button = pygame.Rect(100, 250, 100, 50)
  is_empty_button = pygame.Rect(550, 100, 100, 50)
  len_button = pygame.Rect(550, 200, 100, 50)
  top_button = pygame.Rect(550, 300, 100, 50)
  
  mouse_pos = pygame.mouse.get_pos()
  
  if (push_button.collidepoint(mouse_pos) or pop_button.collidepoint(mouse_pos) or
  is_empty_button.collidepoint(mouse_pos) or len_button.collidepoint(mouse_pos) or
  top_button.collidepoint(mouse_pos)):
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
  else:
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
    if event.type == pygame.MOUSEBUTTONDOWN:
      if push_button.collidepoint(event.pos):#returns true if given point is inside a rectangle
        push(stack, "Candy ", candy_no)
        if(len(stack) < 7):
          candy_no += 1
          containerY += 15 
          candyY += 15
          spring_height -= 15
          springY += 15
          
        if len(stack) == 7:
          container_full_text = "Candy dispenser is full :("
        is_empty_text = ""
        top_text = ""
        len_text = ""
        
        
        
      if pop_button.collidepoint(event.pos):
        popped_candy = pop(stack)
        container_full_text = "Add to your Candy dispenser"
        if(popped_candy != None):
          popped_candies.append(popped_candy)
          containerY -= 15 
          candyY -= 15
          spring_height += 15
          springY -= 15
        is_empty_text = ""
        top_text = ""
        len_text = ""
        
      if is_empty_button.collidepoint(event.pos):
        is_empty_text = str(is_empty(stack))
  
      if top_button.collidepoint(event.pos):
        top_text = str(top(stack))
  
      if len_button.collidepoint(event.pos):
        len_text = str(len(stack))
        

  draw_logo()
  display_result(screen, container_full_text, 300, 50, title_font)
  draw_container(containerX, containerY, 200, 300)
  draw_candies(stack, candyX, candyY)  
  draw_spring(screen, springX, springY, spring_width, spring_height, 10)
  
  draw_button(screen, (137, 138, 166), push_button, "Push")
  draw_button(screen, (137, 138, 166), pop_button, "Pop")
  draw_button(screen, (137, 138, 166), is_empty_button, "Is Empty")
  draw_button(screen, (137, 138, 166), len_button, "Len")
  draw_button(screen, (137, 138, 166), top_button, "Top")
  
  display_result(screen, is_empty_text, 700, 120, display_font)
  display_result(screen, len_text, 700, 220, display_font)
  display_result(screen, top_text, 700, 315, display_font)
  
  draw_candies(popped_candies, 550, 530)
  
  pygame.display.update()
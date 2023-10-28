import math, pygame

# TODO: Mejorar la deteccion de colision entre elementos
def is_collision(x1, y1, s1, x2, y2, s2, distance_collision):
    r1 = s1 / 2
    r2 = s2 / 2
    distance = math.sqrt(math.pow((x1 + r1) - (x2 + r2), 2) + math.pow((y1 + r1) - (y2 + r2), 2))
    
    return distance < r1 + r2

def scale(image, percentage):
    return pygame.transform.scale(image, (percentage, percentage))

def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    
    return rot_image
import pygame


class Entity(pygame.Surface):
    air_threshold = 4

    def __init__(self, x, y, w, h, movement=None, image_path=None, size=None):
        super(Entity, self).__init__(x, y, w, h)

        if image_path is None:
            self.image =
        if movement is None:
            self.movement = [0, 0]
        else:
            self.movement = movement
        self.air_time = 0

    def process_physics(self):
        pass

    def move_x(self):
        self.get_rect().x += self.movement[0]

    def move_y(self):
        self.get_rect().y += self.movement[1]

    def handle_collisions(self, collidable_tiles):
        collisions = {'top':False, 'right':False, 'bottom':False, 'left':False}
        collide_indices = self.get_rect().collidelistall(collidable_tiles)
        self.move_x()
        for index in collide_indices:
            if self.movement[0] > 0:
                self.get_rect().right = collidable_tiles[index].left
                collisions['right'] = True
            else:
                self.get_rect().left = collidable_tiles[index].right
                collisions['left'] = True

        self.move_y()

        for index in collide_indices:
            if self.movement[1] > 0:
                self.get_rect().bottom = collidable_tiles[index].top
                collisions['bottom'] = True
            else:
                self.get_rect().top = collidable_tiles[index].bottom
                collisions['top'] = True

        return collisions

    def draw(self, display):
        display.blit()


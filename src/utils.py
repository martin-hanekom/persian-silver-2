import pygame

def offset(
    size: (float, float) = None,
    pos: (float, float) = (0, 0),
    rect: pygame.Rect = None,
    offset: (float, float) = (0, 0),
    center: (bool, bool) = (False, False)
) -> (float, float):
    '''
    returns the 2D offset from the shape, optionally from the center
    requires either size or rect
    '''
    if rect:
        return (rect.x + center[0] * rect.w / 2 + offset[0], rect.y + center[1] * rect.h / 2 + offset[1])
    return (pos[0] + center[0] * size[0] / 2 + offset[0], pos[1] + center[1] * size[1] / 2 + offset[1])

import pygame

def key_handle():
    # How does this work? 
    # How do we deal with keys?

    # poll for events
    # pygame.QUIT event means the user 
    # clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # TASK A: When the user presses a key,
        # print out the key they pressed
        if event.type == pygame.KEYDOWN:
            print(f"{pygame.key.name(event.key)} has been pressed!")

        # TASK B: When the user left clicks,
        # create a new ball where they clicked

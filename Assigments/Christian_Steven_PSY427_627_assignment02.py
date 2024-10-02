# Steven Christian Code assignment 2

# %% Start

from psychopy import visual, core
import numpy as np

# open a window
win = visual.Window([800, 600], color="grey")

# create a pair of colors based on a hue and a distance from the hue
def generate_color_pair(hue_distance):
    
    #set base hue to random
    hue_base = np.random.uniform(0, 1)
    
    
    #Set the Color
    # color 1 is based on the randomized hue, saturation, and lightness
    color1 = [hue_base, 1, 1]
    
    # color 2 is based on a variation of color 1 shifted by the randomized distance of the block type
    color2 = [(hue_base + hue_distance) % 1, 1, 1]
    return color1, color2

# Convert the colors from HSL to RGB 
def hsl_to_rgb(hsl):
    from colorsys import hsv_to_rgb
    return hsv_to_rgb(hsl[0], hsl[1], hsl[2])

# Define the color based on hue space (near, medium, far)
# set the hue space from a random number in the Min/Max range

hue_distance_ranges = {
    "Near": (0.0, 0.1),
    "Medium": (0.1, 0.2),
    "Far": (0.4, 0.5)
}


# Create Timing Variables

# set 1s per Color block
color_display_duration = 1.0

# set .25s gap between Color Block
gap_duration = 0.25

# set 20s duration per Color block
block_duration = 20.0

# set 3s between blocks
block_gap = 3.0

# Create visuals for the color patches
color_1 = visual.Rect(win, width=0.2, height=0.2, pos=[-0.2, 0])
color_2 = visual.Rect(win, width=0.2, height=0.2, pos=[0.2, 0])

# Create visual for text to display hue distance
message = visual.TextStim(win, text='', pos=(0, 0), color='white')


# Start the experiment loop
for block_type, hue_range in hue_distance_ranges.items():
    print(f"Presenting {block_type} block...")
    
    # Start presenting pairs of colors
    block_timer = core.CountdownTimer(block_duration)
    while block_timer.getTime() > 0:
        
        # Set the hue distance by the random range of the hues for the color block and distance from the hue
        hue_distance = np.random.uniform(hue_range[0], hue_range[1])
        
        # print and display some text above and below the color blocks
        print("Presenting {block_type} block with Hue: {hue_range}...")
        messageTop = visual.TextStim(win, text=f"Presenting Block: {block_type}",pos=(0, 0.4), color='white')
        messageBottom = visual.TextStim(win, text=f"Hue: {hue_distance}...",pos=(0, -0.4), color='white')
        
        # Generate a color block pair
        color1, color2 = generate_color_pair(hue_distance)
        color_1.fillColor = hsl_to_rgb(color1)
        color_2.fillColor = hsl_to_rgb(color2)

        # Present the color block pair and block type message
        color_1.draw()
        color_2.draw()
        messageTop.draw()
        messageBottom.draw()
        win.flip()

        # hold the visual for a set time before clearing
        core.wait(color_display_duration)

        # Clear the screen for the next visual
        win.flip()
        core.wait(gap_duration)

    # show text after a block finished
    print(f"Block complete. Waiting {block_gap} seconds before next block.")
    message = visual.TextStim(win, text=f"Block complete. Waiting {block_gap} seconds before next block.")
    message.draw()
    win.flip()
    core.wait(block_gap)

# Close the window
win.close()
core.quit()


# %% End
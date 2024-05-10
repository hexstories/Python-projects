import sys
import time

def print_lyrics():

    lines = [
        "...",
        "I just laugh when they say that I can't go higher, I'm a frequent flyer",
        "My last album's cold, but my new one's fire, I might call it Maya",
        "I got back pain and I got neck pain 'cah I got the weight of the game on my shoulder",
        "Kept sayin' that it weren't no fluke, I was young like Luke, now I gotta be Yoda"
        "...."
    ]
    delays = [0.08, 0.08, 0.08, 0.08]


    for line, delay in zip(lines, delays):
        print_line_with_delay(line, delay)

def print_line_with_delay(line, delay):

    for char in line:
        print(char, end='', flush=True)
        time.sleep(delay)
    print('')

if __name__ == "__main__":
    print_lyrics()  # Call the function to print the lyrics

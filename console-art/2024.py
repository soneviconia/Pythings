# Pixel Art for "2024" in the console
def print_pixel_art():
    art = [
        "  #####     #####    #####    ##   ##    ",
        " ##    ##  ##   ##  ##    ##  ##   ##    ",
        "      ##   ##   ##       ##   ##   ##    ",
        "    ###    ##   ##     ###    #######    ",
        "   ##      ##   ##    ##           ##    ",
        "  ##       ##   ##   ##            ##    ",
        " #######    #####   #######        ##    "
    ]
    
    # Print each line of the pixel art
    for line in art:
        print(line)

# Call the function to display the art
if __name__ == "__main__":
    print_pixel_art()

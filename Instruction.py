from ImageCaptionModel_2 import predict_step
def BrailleTypeWritter(fname):

    # Define G-code parameters for the 3D printer
    X_START = 0       # Starting X coordinate
    Y_START = 200       # Starting Y coordinate
    DOT_SPACING = 3   # Space between dots in a character
    CHAR_SPACING = 9 # Space between characters
    LINE_SPACING = 9 # Space between lines
    DOT_SIZE = 1      # Size of the dot
    FEEDRATE = 500   # Speed of the printer head movement

    # Define the Braille dot pattern for each character
    dots = {
        " ": [0,0,0, 0,0,0],
        "a": [0,0,0, 1,0,0],
        "b": [0,0,0, 1,1,0],
        "c": [1,0,0, 1,0,0],
        "d": [1,1,0, 1,0,0],
        "e": [0,1,0, 1,0,0],
        "f": [1,0,0, 1,1,0],
        "g": [1,1,0, 1,1,0],
        "h": [0,1,0, 1,1,0],
        "i": [1,0,0, 0,1,0],
        "j": [1,1,0, 0,1,0],
        "k": [0,0,0, 1,0,1],
        "l": [0,0,0, 1,1,1],
        "m": [1,0,0, 1,0,1],
        "n": [1,1,0, 1,0,1],
        "o": [0,1,0, 1,0,1],
        "p": [1,0,0, 1,1,1],
        "q": [1,1,0, 1,1,1],
        "r": [0,1,0, 1,1,1],
        "s": [1,0,0, 0,1,1],
        "t": [1,1,0, 0,1,1],
        "u": [0,0,1, 1,0,1],
        "v": [0,0,1, 1,1,1],
        "w": [1,1,1, 0,1,0],
        "x": [1,0,1, 1,0,1],
        "y": [1,1,1, 1,0,1],
        "z": [0,1,1, 1,0,1],
        ",": [0,0,0, 0,1,0],
        ".": [0,0,0, 0,0,1],
        "_": [1,1,1, 0,0,0],
        "-": [0,0,1, 0,0,1],
        ":": [0,1,0, 0,1,0],
        "?": [0,0,1, 0,1,0],
        "!": [0,1,0, 0,1,1],
        "(": [0,1,1, 0,1,1],
        ")": [0,1,1, 0,1,1],
        "•": [1,1,1, 1,1,1],
        "\\": [0,0,1, 0,1,0],
    }

    def addN(text):
        text = text.split()
        l = len(text)
        out = text[0]
        out += ' '
        length = len(out)
        for i in range(1,l):
            if(length +  len(text[i])> 20):
                if length<20:
                    for j in range(20-length):
                        out += ' '
                out += '\n'
                length = 0
            length += len(text[i])
            length += 1
            out += text[i]
            out += ' '
        return out

    def reflect(text):
        str = ''
        output = ''
        for t in text:
            if(t=='\n'):
                output+=str[::-1]
                output+=t
                str = ''
            else:
                str+=t
        return output

    def generate_gcode(braille_dots):
        gcode = ["G28 ; home all axes", "G1 Z5 F5000 ; lift nozzle", "G21 ; Set units to millimeters", "G90 ; Use absolute positioning", "G92 E0", "G1 Z1.5 F7800", "G1 E-2 F2400", "G92 E0", ""]
        x, y = X_START, Y_START

        for char in braille_dots:
            gcode.append(f';{char}')
            if(char == '\n'):
                y-=LINE_SPACING
                x = X_START
                gcode.append(f"G0 X{x} Y{y}")
            else:
                for row in range(3):
                    for col in range(2):
                        if dots[char][row + col*3] == 1:

                            gcode.append(f"G1 X{x + col * DOT_SPACING} Y{y - row * DOT_SPACING} F{FEEDRATE}")
                            gcode.append(f"G1 Z-3.5 F1000 ; Emboss dot")
                            gcode.append(f"G4 P100 ; Emboss dot")
                            gcode.append(f"G1 Z1.5 F1000 ; Lift printer head")
                        else:

                            gcode.append(f"G1 X{x + col * DOT_SPACING} Y{y - row * DOT_SPACING} F{FEEDRATE}")
                x += CHAR_SPACING

                gcode.append(f"G1 X{x} Y{y} F5000")

        gcode.append("G92 E0\nG28 X0  ; home X axis\nM84     ; disable motors")
        
        return gcode


    descriptions = predict_step([f'{fname}'])
    for description in descriptions:
        print(addN(description))
        gcode_commands = generate_gcode(reflect(addN(description.lower())))
        gcode_filename = f'{fname[:-4]}.gcode'
        with open(gcode_filename, 'w') as file:
            for command in gcode_commands:
                file.write(command + '\n')

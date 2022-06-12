v_red   = 0
while v_red <= 255:
    v_green = 0
    while v_green <= 255:
        v_blue  = 0
        while v_blue <= 255:
            h_red   = hex(v_red)
            h_green = hex(v_green)
            h_blue  = hex(v_blue)
            print(f'A Cor RGB({v_red},{v_green},{v_blue}) em Hexadecimal é ({h_red},{h_green},{h_blue})')
            v_blue += 1
        v_green += 1
    v_red += 1 


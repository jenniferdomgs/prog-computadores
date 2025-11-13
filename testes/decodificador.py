def binario_gray(bin):
    code_gray = bin[0] # o primeiro bit não muda
    for i in range(1, len(bin)): # percorre a partir do segundo até o último
        bit_atual = int(bin[i]) 
        bit_anterior = int(bin[i-1])

        bit_gray = bit_anterior ^ bit_atual # cada bit (a partir do 2) é o XOR dele com o anterior

        code_gray += str(bit_gray) # incrementa o bit ao resultado atual 

    return code_gray

def binario_gray4(bin_4_bits):
    G1 = bin_4_bits[0]  # o gray 1 é igual o bit 1

    # cada gray é o bit atual XOR bit anterior
    G2 = str(int(bin_4_bits[0]) ^ int(bin_4_bits[1]))  
    G3 = str(int(bin_4_bits[1]) ^ int(bin_4_bits[2]))  
    G4 = str(int(bin_4_bits[2]) ^ int(bin_4_bits[3])) 

    return G1 + G2 + G3 + G4




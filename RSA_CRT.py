import numpy as np

def main():   
    # Create Public Key and Private Key
    public_key ,private_key = generate_keys()
    print()
    print("Public Key: (e, n) = ", public_key)
    print("Private Key: (p, q, d_1, d_2, delta_inverse) = ", private_key, "\n")

    # Get Message
    message = input("Message: ")
    print()
        
    # Encode
    code = encode(message)
    
    # Encrypt
    encrypted = []
    for k in code:
        encrypted.append(encrypt(k, public_key))
    
    # Decrypt
    decrypted = []
    for h in encrypted:
        decrypted.append(decrypt(h, private_key))
        
    # Decode
    decoded = decode(decrypted) #(decrypted)
    
    # Print Results
    print("Message:   ", message) 
    print("Encoded:   ", code)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted)
    print("Decoded:   ", decoded) 
    print()
    

def generate_keys():
    # Pick two primes p and q
    p = 1021
    q = 10211
    
    # Calculate n and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Pick e (where gcd(e, phi(n)) = 1 and 1 < e < phi(n))
    e = 10213 #int(input("Give e: "))

    # e1 = e mod phi(p)
    # e2 = e mod phi(q)
    e1 = e % (p - 1)
    e2 = e % (q - 1)
    
    # d_1 = e1 ^ -1 mod phi(p)
    # d_2 = e2 ^ -1 mod phi(q)
    ta, d_1 = extended_euclidean_algorithm( e1, p - 1 )
    ta, d_2 = extended_euclidean_algorithm( e2, q - 1 )
    
    # Calculate Delta Inverse
    r, s = extended_euclidean_algorithm(p, q)
    delta_inverse = (q * r, p * s)
    
    # Create Public Key and Private Key
    return (e, n), (p, q, d_1, d_2, delta_inverse)
 
 
def encode(message):
    return [ord(c) for c in message]


def encrypt(k, public_key):
    #Extract Public Key Data
    e, n = public_key
    
    # Encryption h = k ^ e mod n
    h = modular_exponentiation(k, e, n);

    return h


def decrypt(h, private_key):
    # Extract Private Key Data
    p, q, d_1, d_2, delta_inverse = private_key

    # Delta Function
    h = ( h % p, h % q )
    
    # Decryption Function k = ( h_1 ^ d_1 mod p, h_2 ^ d_2 mod q )
    k = ( modular_exponentiation(h[0], d_1, p), modular_exponentiation(h[1], d_2, q) )

    # Delta Inverse k = qrk_1 * psk_2 mod n
    qr, ps = delta_inverse
    k = ( qr * k[0] + ps * k[1] ) % ( p * q )

    return k


def decode(code):
    message_array = [chr(k) for k in code]
    return ''.join(message_array)


def modular_exponentiation(k, e, n):
    # Find the largest power where 2 ^ power < e
    power = 0
    while (2 ** (power + 1)) < e:
        power += 1
    
    # Find all powers p_i where 2^p_1 + 2^p_2 +...+ 2^p_m = e
    # This is the binary expansion of e
    binary_expansion = []
    while power >= 0:
        binary_expansion.append(power)
        e -= 2 ** power
        while 2 ** power > e:
            power -= 1
    
    # Create square and reduce list
    # (This follows the bottom row of the table we looked at,
    # k squared and reduced again and again untill we reach 
    # the largest possible exponent, remember that we stored
    # the largest possible exponent in binary_expansion[0])
    square_and_reduce = [k]
    for i in range(binary_expansion[0]):
        square_and_reduce.append((square_and_reduce[i] ** 2) % n)
    
    # Multiply Correct squares, the powers in our binary
    # expansion array correspond with the index of the 
    # correct number to include
    product = 1
    for i in binary_expansion:
        product *= square_and_reduce[i]
 
    # Reduce mod n and return
    return product % n


def extended_euclidean_algorithm(a, b):
    # If a was larger than b, switch them
    switched = False
    if a > b:
        switched = True
        temp = a
        a = b
        b = temp
        
    # save the initial values to be used as modulo
    a_initial = a
    b_initial = b
    
    # Euclidean Algorithm while saving each divisor
    quotients = []
    while(a != 0):
        quotient = b // a
        remainder = b % a

        b = a
        a = remainder

        if remainder != 0:
            quotients.append(quotient)
    
    quotients.reverse()

    # Extended part assembles modulo inverse
    V = [1, -quotients[0]]
    for i in quotients[1:]:
        M = [ [0, 1] , [1, -i] ]
        V = np.dot(M, V)
    
    # If we switched a and b initially, then switch back
    if switched:
        temp = V[0]
        V[0] = V[1]
        V[1] = temp
        
    # return ( b inverse mod a, a inverse mod b )
    return V[0] % a_initial, V[1] % b_initial
    
    


if __name__ == "__main__":
    main()
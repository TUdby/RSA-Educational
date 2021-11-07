import numpy as np

def main():   
    # Create Public Key and Private Key
    public_key ,private_key = generate_keys()
    print("Public Key: (e, n) = ", public_key)
    print("Private Key: (p, q, d_1, d_2, delta_inverse) = ", private_key, "\n")

    # get message
    message = input("Message: ")

    # Encrypt and Decrypt
    encrypted = encrypt(message, public_key)
    decrypted = decrypt(encrypted, private_key)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted)


def generate_keys():
    # Pick two primes p and q
    p = 247273562562983703932645522280043300350115796258804294661702066527462061094107046906844683501306787615112143772098532442517907056314381627193134898937143458429341755551511526425737515481224442566433111765795303333197851253771657298477647495085310074366017782891542793428687785265028645168562745631033 #int(input("Give p: "))
    q = 337608748916340101811691066634494654153594349778675742255619077364120327333985156345338641678427021403856401280329327687295815598012919499583361861744945163914633712757538180325597716074242384514914993340226657091260233699583016165261369149277606108839682040016359719662891330673549563654018173357073 #int(input("Give q: "))

    # Calculate n and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Calculate Delta Inverse
    r, s = extended_euclidean_algorithm(p, q)
    delta_inverse = (q * r, p * s)

    # Pick e (where gcd(e, phi(n)) = 1 and 1 < e < phi(n))
    e = 674080373174519198114371334527 #int(input("Give e: "))

    # Calculate d1 and d2
    throw_away, d_1 = extended_euclidean_algorithm(
        e % (p - 1), #e1 = e mod phi(p)
        p - 1        #phi(p)
    )
    
    throw_away, d_2 = extended_euclidean_algorithm(
        e % (q - 1), #e2 = e mod phi(q)
        q - 1        #phi(q)
    )
    
    # Create Public Key and Private Key
    return (e, n), (p, q, d_1, d_2, delta_inverse)


def extended_euclidean_algorithm(k, n):
    switched = False
    if k > n:
        switched = True
        temp = k
        k = n
        n = temp
        
    quotients = []
    remainder = 1
    n_final = n
    
    # Euclidean Algorithm while saving each divisor
    while(remainder != 0):
        quotient = n // k
        remainder = n % k

        n = k
        k = remainder

        if remainder != 0:
            quotients.append(quotient)
    
    # Extended part assembles modulo inverse
    V = [1, -quotients[0]]
    for i in quotients[1:]:
        M = [ [0, 1] , [1, -i] ]
        V = np.dot(M, V)
    
    # Return the inverse expressed within the modulo number
    if switched:
        temp = V[0]
        V[0] = V[1]
        V[1] = temp
    
    return V[0] % n_final, V[1] % n_final
    

def encrypt(message, public_key):
    #Extract Public Key Data
    e, n = public_key
    
    # Encode message to array of ascii values
    values = [ord(char) for char in message]
    
    # Encrypt and return message
    encrypted_message = []
    for k in values:
        code = modular_exponentiation(k, e, n) # (k ** d) % n
        encrypted_message.append(code)

    return encrypted_message


def decrypt(encrypted_message, private_key):
    # Extract Private Key Data
    p, q, d_1, d_2, delta_inverse = private_key
    
    # Split by chinese remainder theorem
    encrypted_message_1 = [h % p for h in encrypted_message]
    encrypted_message_2 = [h % q for h in encrypted_message]
    
    # Decrypt Encrypted Message
    message_1 = []
    for h in encrypted_message_1:
        code = modular_exponentiation(h, d_1, p) # (k ** d) % n
        message_1.append(code)
    
    message_2 = []
    for h in encrypted_message_2:
        code = modular_exponentiation(h, d_2, q)
        message_2.append(code)
       
    # Recombine code
    qr, ps = delta_inverse
    message = []
    n = p * q
    for i in range(len(encrypted_message)):
        k1 = message_1[i]
        k2 = message_2[i]
        k = qr * k1 + ps * k2
        
        # k % n
        while k > 0:
            k -= n
        k += n
        
        # append as character
        print("k: ", k)
        message.append(chr(k))
    
    # Rejoin chars into message and return
    return ''.join(message)


def modular_exponentiation(k, e, n):
    # Find binary expansion (list of indices where 1's would be)
    exp = 1
    count = 1
    while (exp * 2) < e:
        exp *= 2
        count += 1

    binary_expansion = []
    while e != 0:
        binary_expansion += [count]
        e -= exp 
        while exp > e:
            exp //= 2
            count -= 1

    # Create square and reduce list
    square_and_reduce = [k]
    for i in range(1, binary_expansion[0]):
        square_and_reduce += [(square_and_reduce[i - 1] ** 2) % n]
    
    # Multiply Correct squares together according to binary expansion
    mult = 1
    for i in binary_expansion:
        mult *= square_and_reduce[i - 1]
 
    # Reduce mod n and return
    return mult % n


main()
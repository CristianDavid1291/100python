import day8_modul 

alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

func = input("Type 'encode' to encode a message or 'decode' to decode a message: ").lower()

message = input("Type your message: ").lower()

shift = int(input("Type the shift number: ")) 

if func == "encode":
    print(f"The encoded message is: {day8_modul.encrypt_message(message, shift, alphabet)}")
elif func == "decode":
    print(f"The decoded message is: {day8_modul.desencrypt_message(message, shift, alphabet)}")


 



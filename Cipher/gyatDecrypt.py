from PIL import Image

def gyatDecrypt(image_path, key):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    text = []
    delimiter = chr(key[-1])  

    found_delimiter = False
    for i in range(0, len(pixels), 3):
        if found_delimiter:
            break
        for j in range(3):
            if i + j < len(pixels):
                pixel = pixels[i + j]
                character = chr((pixel[j] - key[j]) % 256)
                if character == delimiter:
                    found_delimiter = True
                    break
                text.append(character)

    return ''.join(text)



key = [4, 1, 2, 3]

decrypted_text = gyatDecrypt('output.png', key)
print(f"Decrypted text: '{decrypted_text}'")
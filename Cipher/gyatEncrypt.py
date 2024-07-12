from PIL import Image

def gyatEncrypt(image_path, text, key):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    width, height = img.size
    text_index = 0

    for i in range(0, len(pixels), 3):
        if text_index >= len(text):
            break
        for j in range(3):
            if i + j < len(pixels):
                pixel = list(pixels[i + j])
                # Adjust pixel value based on key[j]
                pixel[j] = (ord(text[text_index]) + key[j]) % 256
                pixels[i + j] = tuple(pixel)
                text_index += 1
                if text_index >= len(text):
                    break

    img.putdata(pixels)
    img.save('output.png')


plaintext = 'AHHH MUJHE MAAF KRDO'
# every 4th pixels 1 means R value.. adding 2 to it and using 3 as delimiter 
key = [4, 1, 2, 3]  
image_path = 'test.jpg'


gyatEncrypt(image_path, plaintext + chr(key[-1]), key)
print(f"Text '{plaintext}' encrypted and hidden in image.")




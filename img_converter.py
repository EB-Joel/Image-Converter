from PIL import Image
import os

# TODO create GUI,
#   add function to search OS
#   Update convert_images function to get image path from GUI
#   add button to activate updated function

# gets os path
path = os.getcwd()


def convert_images(img_to_convert, file_type):
    global path
    ext_img = img_to_convert
    no_ext_img = str(ext_img).rsplit('.',1)[0]
    img = Image.open( path +f'\images-to-convert\{img_to_convert}').convert("RGB")
    img.save(path +f'\converted-images\{no_ext_img}.{file_type}' , (file_type))

print('Hello, which image would you like me to convert?')

while True:
    
   
    img_to_convert = input('Please include the file ext with the image name: ')
    

    print('Ok, which file type would you like to convert it into?')

    file_type = input('jpg, png, or webp?  ') 

    try:
        convert_images(img_to_convert,file_type)
        break
    except FileNotFoundError: 
        print('file was not found, try again, make sure the image you want to convert is in the Images-to-convert folder.')
    except KeyError:
        print('The file type you entered is not supported by this converter. please use either jpg, png, or webp')
    

print('Ok, everything should be in order now, Thank you for your patience.')

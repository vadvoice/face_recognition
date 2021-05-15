import face_recognition
from PIL import Image, ImageDraw
import os

# base variables
base_img_path = 'res'
detected_faces_path = f'{base_img_path}/detected_faces'

def init():
    # create folder for detected faces
    if not os.path.exists(base_img_path):
        os.mkdir(base_img_path)
    if not os.path.exists(detected_faces_path):
        os.mkdir(detected_faces_path)
    print('Hello. I\'m ready to serve!\n')

def face_rec(file_location):
    face_img = face_recognition.load_image_file(file_location)
    face_img_locations = face_recognition.face_locations(face_img)
    original_file_base = os.path.basename(file_location)

    memory_img = Image.fromarray(face_img)
    draw_img = ImageDraw.Draw(memory_img)
    for (top, right, bottom, left) in face_img_locations:
        draw_img.rectangle([(left, top), (right, bottom)], outline='red', width=4)
    del draw_img

    memory_img.save(f'{detected_faces_path}/cropped_{original_file_base}')
    return f'Face(s) amount found: {len(face_img_locations)}'

def extract_faces(file_location):
    faces = face_recognition.load_image_file(file_location)
    faces_locations = face_recognition.face_locations(faces)
    count = 0
    for face_location in faces_locations:
        top, right, bottom, left = face_location
        face_img = faces[top: bottom, left: right]
        pil_img = Image.fromarray(face_img)
        original_file_base = os.path.basename(file_location)
        pil_img.save(f'{detected_faces_path}/{count}_{original_file_base}')
        count += 1
    return f'Face(s) found: {count}'

def compare_faces(person):
    pass

def main():
    # setup & greeting
    init()

    photo_location = input('Give me file location to detect persons on the photo: ')
    if os.path.exists(photo_location):
        print(face_rec(photo_location))
    else:
        print('Dude! File path is invalid or not exists ¯\_(๑❛ᴗ❛๑)_/¯')

if (__name__ == '__main__'):
    main()
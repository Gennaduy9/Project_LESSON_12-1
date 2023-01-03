def save_picture(picture):
    filename = picture.filename
    file_type = filename.lower().split('.')[-1]

    if file_type not in ('BMP', 'ECW', 'GIF', 'JPEG', 'JPEG 2000', 'PCX', 'PNG', 'PSD', 'TIFF', 'JFIF', 'HD Photo', 'PNM', 'PDF', 'jpg'):
        return

    picture.save(f'./uploads/images{filename}')
    return f'uploads/images{filename}'
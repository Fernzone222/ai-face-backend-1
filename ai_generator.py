def generate_profile_pictures(file_url, style):
    return [file_url.replace('original', style + '_1'), file_url.replace('original', style + '_2')]

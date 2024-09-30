def write(data, filename):
    try:
        with open("Uploads/" + filename, 'w') as f:
            f.write(data)
    except IOError:
        print("An error occurred during the text upload, please try again.")
        return False
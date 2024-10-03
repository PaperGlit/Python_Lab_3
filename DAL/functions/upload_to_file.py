def file_upload(data):
    while True:
        file_name = input("Enter file name: ")
        if file_name.strip() != "":
            if not file_name.endswith(".txt"):
                file_name += ".txt"
            try:
                with open("Uploads/" + file_name, 'w') as f:
                    f.write(data)
                print("The art was uploaded successfully")
            except IOError:
                print("An error occurred during file upload, please try again")
            return
        else:
            print("Please enter a valid file name")

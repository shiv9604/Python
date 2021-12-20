def readfile(filename):
    try:
        with open(filename) as f:
            print(f.read())
    # # except Exception as e:
    #     print(f"File {filename} is not there soo plz create it first..")
    except FileNotFoundError:
        print(f"File {filename} is not there soo plz create it first..")

    # --> both can be used...

readfile("1.txt")
readfile("2.txt")
readfile("3.txt")

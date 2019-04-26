with open("words.txt","r")as input_file, open("caps-words.txt","w") as output_file:
    for line in input_file:
        capsline = line.upper()
        print(capsline, file=output_file, end="")
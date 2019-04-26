def readcurrency(filename):
  with open (filename) as input_file, open ("new_file.txt", "w") as output_file:
    final_list = []
    for line in input_file:
      no_new_line_char = line.replace("\n", "")
      symbol_rate = no_new_line_char.split(" ")
      symbol_rate_dict = {}
      for line in symbol_rate:
        symbol_rate_dict["symbol"] = symbol_rate[0]
        symbol_rate_dict["rate"] = symbol_rate[1]
        final_list.append(symbol_rate_dict)
    print(final_list, file=output_file)
    return final_list

readcurrency("currency.txt")

def save(filename,data):
  import json
  dictionary = {}
  dictionary["data"] = data
  with open(filename, "w") as output_file:
    json.dump(dictionary, output_file) 

save("new_file.txt",readcurrency("currency.txt"))
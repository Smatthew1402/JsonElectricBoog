import json as js



if __name__ == "__main__":
    test = {"Name":'grade'}
    with open ("data_file.json", 'w') as write_file:
        js.dump(test, write_file)
    json_string = js.dump(test)

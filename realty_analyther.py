import sys

def get_frequently_sold_property(realty_file):

    with open('result.csv', 'w') as result:
        with open(realty_file, 'r') as f:
            hash_dict = {}
            for line in f:
                list_line = line.strip().split(',')
                adress_list = [list_line[7], list_line[8], list_line[9], list_line[11], list_line[13]]
                adress = ", ".join(adress_list).replace('"', '') + "\n"
                object_hash = hash(tuple(adress_list))
                if hash_dict.get(object_hash, 0) == 1:
                    result.write(adress)
                    hash_dict[object_hash] += 1
                elif hash_dict.get(object_hash, 0) == 2:
                    continue
                else:
                    hash_dict[object_hash] = 1


if __name__ == "__main__":

    realty_file = sys.argv[1]
    get_frequently_sold_property(realty_file)



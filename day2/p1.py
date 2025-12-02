with open("./input.txt", "r") as f :
    data = f.read()

id_ranges = data[0:len(data)-1].split(",")
id_ranges = [(i.split("-")[0], i.split("-")[1]) for i in id_ranges]
print(id_ranges)


def is_len_odd(num):
    if(len(str(num))%2 != 0):
        return True
    return False

def nxt_even_len(curr):
    len_curr = len(str(curr))
    nxt = '1'
    for i in range(len_curr):
        nxt += '0'

    return int(nxt)
    

invalid_ids = []
for i,j in id_ranges:
    start = int(i)
    end  = int(j)
    while start  <=  end:
        if is_len_odd(start):
            start = nxt_even_len(start)
            continue

        curr = str(start)
        mid = int(len(curr) / 2)
        print(mid)
        first_half = curr[0:mid]
        second_half = curr[mid:]
        if first_half == second_half:
            invalid_ids.append(start)

        start +=1

        
result = sum(invalid_ids)
print(result)

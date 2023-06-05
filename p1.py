# in find function of this code we are passing unnecessary parameters/arguments.
# class is not used in this code so prefer new code in which class is used .

size = 10
linear_hashtable = []
quadratic_hashtable = []
linear_visited = []
quadratic_visited = []

# Initialize the hash tables and visited arrays
for i in range(size):
    linear_hashtable.append(0)
    quadratic_hashtable.append(0)
    linear_visited.append(False)
    quadratic_visited.append(False)


def linear_probing(num):
    index = num % size
    if linear_visited[index]:
        while linear_visited[index]:
            index = (index + 1) % size

    linear_hashtable[index] = num
    linear_visited[index] = True


def quadratic_probing(num):
    index = num % size
    if not quadratic_visited[index]:
        quadratic_hashtable[index] = num
        quadratic_visited[index] = True
    else:
        k = 1
        for k in range(size):
            t = (index + k * k) % size
            if not quadratic_visited[t]:
                quadratic_hashtable[t] = num
                quadratic_visited[t] = True
                break


def find(num, hash_table, visited, probing_type):
    index = num % size
    redflag = index
    if probing_type == "linear":
        if hash_table[index] == num:
            print("Found", num)
        else:
            index = (index + 1) % size
            while visited[index]:
                if hash_table[index] == num:
                    print("Found", num)
                    break
                elif index==redflag:
                    print("Not found")
                    break

                index = (index + 1) % size
            else:
                print("Not found", num)

    elif probing_type == "quadratic":
        if hash_table[index] == num:
            print("Found", num)
        else:
            k = 1
            for k in range(size):
                t = (index + k * k) % size
                if hash_table[t] == num:
                    print("Found", num)
                    break
            else:
                print("Not found", num)

    else:
        print("Invalid probing type")


def main():
    probing_mode = 0
    while True:
        print("1. Linear probing.")
        print("2. Quadratic probing.")
        print("3. Find element.")
        print("4. Exit.")

        choice = int(input("Enter your choice: "))
        

        if choice == 1:
            num_elements = int(input("Enter the number of elements: "))
            for _ in range(num_elements):
                phone_num = int(input("Enter phone number: "))
                linear_probing(phone_num)
                print("Hashtable using linear probing:", linear_hashtable)
                probing_mode = 1

        elif choice == 2:
            num_elements = int(input("Enter the number of elements: "))
            for _ in range(num_elements):
                phone_num = int(input("Enter phone number: "))
                quadratic_probing(phone_num)
                print("Hashtable using quadratic probing:", quadratic_hashtable)
                probing_mode = 2

        elif choice == 3:
            num_to_find = int(input("Enter the number to be found: "))
            if(probing_mode==1):
                find(num_to_find, linear_hashtable, linear_visited,"linear")
            elif(probing_mode == 2):
                find(num_to_find, quadratic_hashtable,quadratic_visited,"quadratic")
        elif choice == 4:
            print("End of Program")
            break
        else:
            print("Enter a valid choice")


main()




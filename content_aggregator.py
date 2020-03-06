import time
from categories import main

if __name__ == '__main__':
    part_cat = input("Enter Part Category: ")
    part_name = input("Enter part name: ")
    start_time = time.time()
    part_name = part_name.strip().lower()
    part_list = main.get_part_list(part_name, part_cat)
    if(part_list == []):
        print(f"No part named '{part_name}' was found!")
    for part in part_list:
        print("\n")
        print(part)
    print("\n")
    print("Time Taken", time.time()-start_time)

# ##### ToDO
lst = []
while True:
    print(lst)
    print("Add your Todo enter 1, Remove Todo Enter 2, Update Todo Enter 3, exit Enter 0")
    a = int(input("Enter a numbre: "))
    if a== 0:
       break
    elif a == 1:
      add_todo = input("Enter a Todo:")
      lst.append(add_todo)
    elif a == 2:
        remove_todo = int(input("Enter remove todo item index:"))
        if remove_todo > len(lst):
           print("You can't enter index out of range")
        else:
            lst.pop(remove_todo)
    elif a == 3:
        print(lst)
        update_todo = int(input("Enter update index number:"))
        if len(lst) < update_todo:
            print("You Can't enter lst index out of range:")
        else:
            update_value = input("Enter update_value:")
            if update_value >= '0' and update_value <= '9':
                update_value = int(update_value)
            lst[update_todo] = update_value


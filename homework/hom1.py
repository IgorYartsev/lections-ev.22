with open('task1.txt', 'w') as file:
  file.writelines(['1', '\n2', '\n3', '\n4', '\n5', '\n6', '\n7', '\n8', '\n9', '\n10'])
  for line in file.writelines(1):
    print(line)
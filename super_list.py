class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

len(super_list1)
print(issubclass(SuperList, list))

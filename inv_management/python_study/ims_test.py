import inv_mng_study as ims

potion = ims.Object('Potion',(1,1),True,0.1,1,99)
sword = ims.Object('Sword',(4,2),False,2,2,1)

player = ims.Inventory(10,10)

player.add_object(potion)
print(player.area)
print('#############################')
player.add_object(sword)
print(player.area)
print('#############################')
player.add_object(potion)
print(player.area)
print('#############################')

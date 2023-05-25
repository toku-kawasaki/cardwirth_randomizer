from glob import glob
import os
import shutil
import random as rand

scenario_name = input("シナリオの名前を入力してください：")

Mate_lis = glob(f"./{scenario_name}/Mate*.wid")
Item_lis = glob(f"./{scenario_name}/Item*.wid")
Info_lis = glob(f"./{scenario_name}/Info*.wid")
Skill_lis = glob(f"./{scenario_name}/Skill.wid")

for Mate in Mate_lis:
    Mate_file = os.path.basename(Mate)
    new_Mate_lis = glob(f"../*/*/{Mate_file}") + glob(f"../*/*/*/{Mate_file}")
    shutil.copy(rand.choice(new_Mate_lis),f"./{scenario_name}")

for Item in Item_lis:
    Item_file = os.path.basename(Item)
    new_Item_lis = glob(f"../*/*/{Item_file}") + glob(f"../*/*/*/{Mate_file}")
    shutil.copy(rand.choice(new_Item_lis),f"./{scenario_name}")

for Info in Info_lis:
    Info_file = os.path.basename(Info)
    new_Info_lis = glob(f"../*/*/{Info_file}") + glob(f"../*/*/*/{Mate_file}")
    shutil.copy(rand.choice(new_Info_lis),f"./{scenario_name}")

for Skill in Skill_lis:
    Skill_file = os.path.basename(Skill)
    new_Skill_lis = glob(f"../ask/*/{Skill_file}") + glob(f"../*/*/*/{Skill_file}")
    shutil.copy(rand.choice(new_Skill_lis),f"./{scenario_name}")
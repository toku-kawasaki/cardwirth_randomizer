from glob import glob
import os
import shutil
import random as rand

scenario_lis = glob("./*/Summary.wsm")

for scenario in scenario_lis:

    scenario_name = os.path.basename(os.path.dirname(scenario))

    Mate_lis = glob(f"./{scenario_name}/Mate*.wid")
    Item_lis = glob(f"./{scenario_name}/Item*.wid")
    Info_lis = glob(f"./{scenario_name}/Info*.wid")
    Skill_lis = glob(f"./{scenario_name}/Skill*.wid")

    for Mate in Mate_lis:
        Mate_file = os.path.basename(Mate)
        new_Mate_lis = glob(f"../ask/*/{Mate_file}") + glob(f"../サンプルダンジョン/モンスター図鑑+/{Mate_file}")
        shutil.copy(rand.choice(new_Mate_lis),f"./{scenario_name}")

    for Item in Item_lis:
        Item_file = os.path.basename(Item)
        new_Item_lis = glob(f"../ask/*/{Item_file}") + glob(f"../サンプルダンジョン/モンスター図鑑+/{Item_file}")
        shutil.copy(rand.choice(new_Item_lis),f"./{scenario_name}")

    for Info in Info_lis:
        Info_file = os.path.basename(Info)
        new_Info_lis = glob(f"../ask/*/{Info_file}") + glob(f"../サンプルダンジョン/モンスター図鑑+/{Info_file}")
        shutil.copy(rand.choice(new_Info_lis),f"./{scenario_name}")

    for Skill in Skill_lis:
        Skill_file = os.path.basename(Skill)
        new_Skill_lis = glob(f"../ask/*/{Skill_file}") + glob(f"../サンプルダンジョン/モンスター図鑑+/{Skill_file}")
        shutil.copy(rand.choice(new_Skill_lis),f"./{scenario_name}")

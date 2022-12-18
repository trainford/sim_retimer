import os
import shutil

num_splashes = 20

for i in range(num_splashes):

    source = "C:/aggie_projects/rain_scene_winter/geo/water_splashes/splash_{num}/splash".format(num = i)
    destination = "C:/aggie_projects/rain_scene_winter/geo/water_splashes/splash_{num}/splash_sped_up".format(num = i)
    
    try:
        os.mkdir(destination)
    except OSError as error:
        shutil.rmtree(destination)
        os.mkdir(destination)
        print("Folder exists. Deleting existing folder.")

    files = os.listdir(source)

    j = 0

    for f in files:
        if j % 4 == 0:
            src_path = os.path.join(source, f)
            dst_path = os.path.join(destination, f)
            shutil.copy(src_path, dst_path)
        j += 1

    os.remove(f"{destination}/splash.0001.bgeo.sc")
    sped_files = os.listdir(destination)

    k = 1

    for sf in sped_files:
        dst = f"{destination}/splash.{k:04}.bgeo.sc"
        src = f"{destination}/{sf}"
        os.rename(src, dst)
        k += 1
        


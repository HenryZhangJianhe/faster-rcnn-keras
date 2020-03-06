import glob
import os
import shutil

def makedir(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)



def copy(dst_dir,data_dir,tail):
    for root,dirs,files in os.walk(data_dir,topdown=True):
        for sDir in dirs:
            imgs_list = glob.glob(os.path.join(root,sDir,tail))
            print('共有'+tail,len(imgs_list))

            for imagepath in imgs_list:
                shutil.copy(imagepath,dst_dir)

def gen_txt(txt_path,img_dir,tail):
    f=open(txt_path,'w')
    for root,dirs,files in os.walk(img_dir,topdown=True):
        for sDir in dirs:
            imgs_list = glob.glob(os.path.join(root,sDir,tail))
            print('共有'+tail,len(imgs_list))
            for i in range(len(imgs_list)):
                name=os.path.split(imgs_list[i])[-1].split('.')[0]
                line=name+'\n'
                f.write(line)
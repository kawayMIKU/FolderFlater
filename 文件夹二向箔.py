import os
import shutil
import json
import os.path
def flat(folder_name):
    root = os.path.basename(folder_name)
    folder_struct = {
        '文件夹': [root],
        '文件': []
    }
    try:
        shutil.rmtree('展平')  
    except:
        pass
    try:
        os.mkdir('展平')
    except:
        pass 
    count = 0
    root += '/'
    for path_,folders,files in os.walk(folder_name):
        path_ = path_.replace('\\','/')+'/'
        for i in folders:
            folder_struct['文件夹'].append(root+os.path.relpath(path_+i, folder_name))
        for i in files:
            from_ = path_+i
            to = i+' - '+str(count)+'.flat'
            folder_struct['文件'].append([to,root+os.path.relpath(from_, folder_name)])
            shutil.copyfile(from_,'展平/'+to)
            count += 1
    with open('展平/文件夹结构.json', 'w', encoding='utf-8') as f:
        json.dump(folder_struct, f, ensure_ascii=False, indent=2)
def deflat(folder_name):
    with open(folder_name+'/文件夹结构.json', 'r', encoding='utf-8') as f:
        folder_struct = json.load(f)
    try:
        shutil.rmtree('还原')  
    except:
        pass
    try:
        os.mkdir('还原')
    except:
        pass

    for i in folder_struct['文件夹']:
        os.mkdir('还原/'+i)
    folder_name_ = folder_name+'/'
    for i in folder_struct['文件']:
        shutil.copyfile(folder_name_+i[0],'还原/'+i[1])
if __name__ == '__main__':
    import menu
    choice = menu.menu(['1. 展平文件夹','2. 还原文件夹'])
    path = input('输入文件夹目录? ').replace('\\','/')
    if path[-1] == '/':
        path = path[:-1]
    if choice == 0:
        flat(path)
    elif choice == 1:
        deflat(path)
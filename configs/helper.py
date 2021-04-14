import yaml
import os

def write_yaml(cwd, classes, output='custom'):
    dict_file = [
        'train : {}'.format(os.path.join(cwd, 'tools_dataset', 'train_images')),
        'val : {}'.format(os.path.join(cwd, 'tools_dataset', 'val_images')),
        'nc : {}'.format(len(classes)),
        'names : {}'.format(classes)]
    
    # write train file
    f = open(r'.\data\{}.yaml'.format(output), 'w')
    for i in dict_file:
        f.write("{}\n".format(i))
    f.close()

def write_imagesets(cwd, list_images, train_partition=0.75):
    img_len = len(list_images)
    tr_len = int(img_len * train_partition)
    
    # write train file
    f = open(r'.\data\train_images.txt', 'w+')
    for i in range(tr_len):
        f.write("{}\n".format(list_images[i]))
    f.close()

    # write test file
    f = open(r'.\data\test_images.txt', 'w+')
    for i in range(tr_len, img_len):
        f.write("{}\n".format(list_images[i]))
    f.close()

    # write test file
    f = open(r'.\data\val_images.txt', 'w+')
    for i in range(tr_len, img_len):
        f.write("{}\n".format(list_images[i]))
    f.close()

def read_classes(class_file_dir='.\data\image\classes.txt'):
    f = open(class_file_dir, 'r')
    contents = f.read().splitlines()
    f.close()
    return contents


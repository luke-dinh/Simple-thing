import numpy as np
import matplotlib.pyplot as plt
def concat_images(imga,imgb):
    ha,wa = imga.shape[:2]
    hb,wb = imgb.shape[:2]
    max_height = np.max([ha,hb])
    total_width = wa+wb
    new_img = np.zeros(shape=(max_height, total_width, 3))
    new_img[:ha,:wa]=imga
    new_img[:hb,wa:wa+wb]=imgb
    return new_img
def concat_n_image(image_path_list):
    output = None
    for i,img_path in enumerate(image_path_list):
        img = plt.imread(img_path)[:,:,:3]
        if i==0:
            output = img
        else:
            output = concat_images(output, img)
    return output
images = ["d:/1.jpg","d:/2.jpg","d:/3.jpg"]
output = concat_n_image(images)
import matplotlib.pyplot as plt
plt.imshow(output)
plt.show()





import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from generate_xml import write_xml

# global constants
img = None
tl_list = []
br_list = []
object_list = []

# constantsq
image_folder = 'images'
savedir = 'annotations'
objlist= ['durak', 'hiz30', 'girilmez', 'mecburisag', 'mecburisol', 'solyasak', 'park', 'trafikisik', 'parkyasak']
obj ="durak"

def line_select_callback(clk, rls):
    global tl_list
    global br_list
    global object_list
    global obj
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(obj)

def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img,obj
    if event.key == 'q':
        print(object_list)
        write_xml(image_folder, img, object_list, tl_list, br_list, savedir)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        plt.close()
    if event.key in ["1","2","3","4","5","6","7","8","9"]:
        obj = objlist[int(event.key )-1]
        print(event.key,obj)

def toggle_selector(event):
    toggle_selector.RS.set_active(True)


if __name__ == '__main__':
    for n, image_file in enumerate(os.scandir(image_folder)):
        img = image_file
        fig, ax = plt.subplots(1)
        mngr = plt.get_current_fig_manager()
        #mngr.window.setGeometry(250, 120, 1280, 1024)
        image = cv2.imread(image_file.path)
        if(image is not None):
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            ax.imshow(image)

            toggle_selector.RS = RectangleSelector(
                ax, line_select_callback,
                drawtype='box', useblit=True,
                button=[1], minspanx=5, minspany=5,
                spancoords='pixels', interactive=True
            )
            bbox = plt.connect('key_press_event', toggle_selector)
            key = plt.connect('key_press_event', onkeypress)
            plt.show()
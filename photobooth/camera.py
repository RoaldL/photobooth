import gphoto2 as gp
import threading

import os
from os import listdir
from os.path import isfile, join

class CameraController:

    def __init__(self, mypath):
        print('init')
        self._dir = mypath
        self.pictures = sorted([os.path.join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))])

    def get_picture(self):
        if 'capture_thread' in locals():
            self.capture_thread.join()
        self.capture_thread = threading.Thread(target=self._get_picture).start()

    def _get_picture(self):

        print('get picture')
        camera = gp.check_result(gp.gp_camera_new())
        gp.check_result(gp.gp_camera_init(camera))
        
        print('Capturing image')
        file_path = gp.check_result(gp.gp_camera_capture(
            camera, gp.GP_CAPTURE_IMAGE))
        
        print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
        target = os.path.join(self._dir, file_path.name)
        self.pictures.append(target)
        
        print('Copying image to', target)
        camera_file = gp.check_result(gp.gp_camera_file_get(
                camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
        
        gp.check_result(gp.gp_file_save(camera_file, target))
        gp.check_result(gp.gp_camera_exit(camera))

    def wait_for_camera(self):
        if 'capture_thread' in locals():
            self.capture_thread.join()

    def get_preview(self):
        print('get preview')

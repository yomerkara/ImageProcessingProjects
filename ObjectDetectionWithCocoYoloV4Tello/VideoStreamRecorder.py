import datetime
import os
import pathlib
import time
import cv2

class VideoStreamRecorder(object):

	def __init__(self, root=None):
		self.running = False # Very Impt !!!!!!!!!
		self.root = root
		self.filename = None

	def record_video(self, videofeed=None, fps = 75):
		self.filename = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S") + ".avi"
		self.root = self.root if self.root else pathlib.Path(os.getcwd()).root
		record_path = os.path.abspath(os.path.join(self.root,'Vid_Recordings'))
		if not os.path.exists(record_path):
			os.makedirs(record_path)
		self.filename = os.path.abspath(os.path.join(record_path, self.filename))
		self.videofeed = videofeed
		self.running = True
		frame = self.videofeed.frame
		self.video_writer = cv2.VideoWriter(
			self.filename, 
			cv2.VideoWriter_fourcc(*'MJPG'),
			fps,
			(int(self.videofeed.cap.get(3)),int(self.videofeed.cap.get(4))))
		while self.running:
			frame = self.videofeed.frame
			self.video_writer.write(frame)
		return None

	def record_stop(self):
		time.sleep(2)
		self.video_writer.release()
		return self.filename
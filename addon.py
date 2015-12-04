import time
import xbmc

if __name__ == '__main__':
	monitor = xbmc.Monitor()

	while not monitor.abortRequested():
		# Sleep/wait for abort for 10 seconds
		if monitor.waitForAbort(10):
			# Abort requested while waiting. Should exit
			break
		xbmc.log("Hello service! %s" % time.time(), level=xbmc.LOGNOTICE)
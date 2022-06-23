#from vicon_dssdk import ViconDataStream
import cv2
import os
import time

def getViconData(client):
    #override to get the cordinates
    return "{}"








#client = ViconDataStream.Client()
# define a video capture object
vid = cv2.VideoCapture(0)


print("Press any Enter to Start the Recoring")
input()

current_directory = os.getcwd()

final_directory_frames = os.path.join(current_directory, r'Frames')
if not os.path.exists(final_directory_frames):
   os.makedirs(final_directory_frames)


final_directory_viconData = os.path.join(current_directory, r'ViconData')
if not os.path.exists(final_directory_viconData):
   os.makedirs(final_directory_viconData)


FileCounter = 1

while (True):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    #Capture ViconData Farme
    client.GetFrame()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imwrite(os.path.join(final_directory_frames,  str(FileCounter) + '.jpg'), frame)

    json = getViconData(client)
    with open(os.path.join(final_directory_viconData,  str(FileCounter) + '.json'), "w") as f:  # Opens file and casts as f
        f.write(json)  # Writing
        # File closed automatically


    FileCounter = FileCounter + 1
    time.sleep(0.1)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
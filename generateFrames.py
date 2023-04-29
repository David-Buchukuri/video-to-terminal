import cv2
import os
import shutil


def generateFrames(path):
    capture = cv2.VideoCapture(path)

    frameNumber = 0

    if os.path.exists('./frames'):
        shutil.rmtree('./frames')

    os.makedirs('./frames')

    while (True):
        success, frame = capture.read()

        if success:
            resizedFrame = cv2.resize(frame, (120, 90))

            cv2.imwrite(
                f'./frames/frame-' + str(frameNumber) + '.png', resizedFrame
            )

        else:
            break

        frameNumber += 1

    capture.release()


generateFrames('./bad-apple.mp4')

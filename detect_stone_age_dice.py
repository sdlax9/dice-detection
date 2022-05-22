import cv2
import detect_dice

FOOD_DENOMINATOR = 2
WOOD_DENOMINATOR = 3
BRICK_DENOMINATOR = 4
STONE_DENOMINATOR = 5
GOLD_DENOMINATOR = 6

LEFT_OFFSET = 50
RIGHT_OFFSET = 570
TOP_OFFSET = 100
BOTTOM_OFFSET = 50

def overlay_info(frame, dice, blobs, frame_width=0, frame_height=0):
    # Overlay blobs
    for b in blobs:
        pos = b.pt
        r = b.size / 2

        cv2.circle(frame, (int(pos[0]), int(pos[1])),
                   int(r), (255, 0, 0), 2)

    # Overlay dice number
    for d in dice:
        # Get textsize for text centering
        textsize = cv2.getTextSize(
            str(d[0]), cv2.FONT_HERSHEY_PLAIN, 3, 2)[0]

        cv2.putText(frame, str(d[0]),
                    (int(d[1] - textsize[0] / 2),
                     int(d[2] + textsize[1] / 2)),
                    cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

    pip_count = len(blobs)
    dice_count = len(dice)
    cv2.putText(
        frame, 'Dice: ' + str(dice_count), (LEFT_OFFSET, frame_height-(BOTTOM_OFFSET*2)), 
        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2
    )
    cv2.putText(
        frame, 'Roll: ' + str(pip_count), (LEFT_OFFSET, frame_height-BOTTOM_OFFSET), 
        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2
    )

    # Overlay Stone Age info
    # Title
    cv2.putText(
        frame, 'Stone Age Resources', (frame_width-RIGHT_OFFSET, frame_height-(BOTTOM_OFFSET*6)), 
        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2
    )
    # Food
    cv2.putText(
        frame, 'Food: ' + str(int(pip_count/FOOD_DENOMINATOR)), (frame_width-RIGHT_OFFSET, frame_height-(BOTTOM_OFFSET*5)), 
        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2
    )
    # Wood
    cv2.putText(
        frame, 'Wood: ' + str(int(pip_count/WOOD_DENOMINATOR)), (frame_width-RIGHT_OFFSET, frame_height-(BOTTOM_OFFSET*4)), 
        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2
    )
    # Brick
    cv2.putText(
        frame, 'Brick: ' + str(int(pip_count/BRICK_DENOMINATOR)), (frame_width-RIGHT_OFFSET, frame_height-(BOTTOM_OFFSET*3)), 
        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2
    )
    # Stone
    cv2.putText(
        frame, 'Stone: ' + str(int(pip_count/STONE_DENOMINATOR)), (frame_width-RIGHT_OFFSET, frame_height-(BOTTOM_OFFSET*2)), 
        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2
    )
    # Gold
    cv2.putText(
        frame, 'Gold: ' + str(int(pip_count/GOLD_DENOMINATOR)), (frame_width-RIGHT_OFFSET, frame_height-(BOTTOM_OFFSET)), 
        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2
    )

if __name__ == '__main__':
    detect_dice.overlay_info = overlay_info
    detect_dice.detect_dice(1)
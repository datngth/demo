import cv2

pikachu = cv2.imread("data\pikachu.png", cv2.IMREAD_COLOR)
conan = cv2.imread("data\Edogawa-Conan-.jpg", cv2.IMREAD_COLOR)

pikachu = cv2.resize(pikachu, (conan.shape[1], conan.shape[0]))

H = pikachu.shape[0]
W = pikachu.shape[1]
for d in range(0, W+1):
    view = pikachu.copy()
    view[0:H, 0:W-d] = pikachu[0:H, d:W]
    view[0:H, W-d:W] = conan[0:H, 0:d]
    cv2.imshow("View", view)
    cv2.waitKey(1)
print("hello")

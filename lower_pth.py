import cv2
import torch
from models import RCAN

# models init
model = RCAN(scale=2, num_rcab=10)
model_params = torch.load("./model/pretrain.pth", map_location=torch.device('cpu'))
model.load_state_dict(model_params)

model.eval()
img = cv2.imread("./convert/img.png", 0)
print(img.shape)
sr_img = model(torch.from_numpy(img).unsqueeze(0).unsqueeze(0).float()).detach().squeeze().numpy()
cv2.imshow("sr", sr_img / 255)
cv2.waitKey()
cv2.destroyAllWindows()

# for pytorch 1.4.0 and Vitis-AI 1.4.0
torch.save(model_params, "./model/pretrain_low.pth", _use_new_zipfile_serialization=False)

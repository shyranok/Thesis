# super-resolve an LR image (x2) using the model trained on noise-free degradations with isotropic Gaussian blurs
python quick_test.py --img_dir='/content/drive/MyDrive/Thesis/DASR/test.png' \
                     --scale='2' \
                     --resume=2 \
                     --blur_type='iso_gaussian'

cmd /k

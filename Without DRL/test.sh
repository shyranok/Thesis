# noise-free degradations with isotropic Gaussian blurs
python test.py --test_only \
               --dir_data='/content/drive/MyDrive/Thesis' \
               --data_test='Set14' \
               --model='blindsr' \
               --scale='2' \
               --resume=125 \
               --blur_type='iso_gaussian' \
               --noise=0.0 \
               --sig=2.6
cmd /k
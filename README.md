# MGHF: Multi-Granular High-Frequency Perceptual Loss for Image Super-Resolution
Welcome! This is the official implementation of the paper "MGHF: Multi-Granular High-Frequency Perceptual Loss for Image Super-Resolution."
We thanks authors of SinSR and ResShift for their github repository

## :turtle: Requirements
* Python 3.10, Pytorch 2.1.2, [xformers](https://github.com/facebookresearch/xformers) 0.0.23
* More detail (See [environment.yml](environment.yml))
A suitable [conda](https://conda.io/) environment named `SinSR` can be created and activated with:

```
conda env create -n HF-Diff python=3.10
conda activate HF-Diff
pip install -r requirements.txt
```
or
```
conda env create -f environment.yml
conda activate HF-Diff
```

## :rocket: Fast Testing
```sh
python3 inference.py -i [image folder/image path] -o [result folder] --ckpt weights/HF-Diff.pth --scale 4 --one_step
```
## :dolphin: Reproducing the results in the paper
### Results in Table 1
- Real data for image super-resolution: [RealSet65](testdata/RealSet65) | [RealSR](testdata/RealSR)
- Test the model
```sh
# Results on RealSet65
python inference.py -i testdata/RealSet65 -o results/HF-Diff/RealSet65 --scale 4 --ckpt weights/HF-Diff.pth --one_step

# Results on RealSR
python inference.py -i testdata/RealSet65 -o results/HF-Diff/RealSR --scale 4 --ckpt weights/HF-Diff.pth --one_step

```
If you are running on a GPU with limited memory, you could reduce the patch size by setting ```--chop_size 256``` to avoid out of memory. However, this will slightly degrade the performance.
```sh
# Results on RealSet65
python inference.py -i testdata/RealSet65 -o results/HF-Diff/RealSet65 --scale 4 --ckpt weights/HF-Diff.pth --one_step --chop_size 256 --task SinSR

# Results on RealSR
python inference.py -i testdata/RealSR -o results/HF-Diff/RealSR --scale 4 --ckpt weights/HF-Diff.pth --one_step --chop_size 256 --task SinSR
```

### Results in Table 1,2,3
- Download the Super-resolution results on RealSet65 (raw dataset Collected from SinSR reposityory)[(Link)](https://drive.google.com/file/d/1ibnoC_eqWxT4ssU_NRe5MZhixbBDBnr0/view?usp=sharing).
- Download the Super-resolution results on RealSR (raw dataset Collected from SinSR reposityory) [(Link)](https://drive.google.com/file/d/1hb3CGz5MwoY9hYxNmYCwWs_igB9CggoH/view?usp=sharing).
- Download the image ImageNet-Test [(Link)](https://drive.google.com/file/d/1NhmpON2dB2LjManfX6uIj8Pj_Jx6N-6l/view?usp=sharing) to the [testdata](testdata) folder.
- Download the Super-resolution results on ImageNet (raw dataset Collected from SinSR reposityory) [(Link)](https://drive.google.com/file/d/1wRgwsBA6-JAmTifqAl4No7zgZKF93job/view?usp=sharing).
- Download the Super-resolution results on RealSR (raw dataset Collected from OSEDiff reposityory) [(Link)](https://drive.google.com/file/d/1aKgeXeILuNPdY1tQ-jpXo91SWjUjUgIN/view?usp=sharing).
- Download the Super-resolution results on Div2K_Val (raw dataset Collected from OSEDiff reposityory) [(Link)](https://drive.google.com/file/d/1clLM-HvEkTj_3hJ4GhCmwALO5STwUZU4/view?usp=sharing).

- Unzip the downloaded dataset.
- Test the model
```sh
python inference.py -i testdata/imagenet256/lq/ -o results/HF-Diff/imagenet  -r testdata/imagenet256/gt/ --scale 4 --ckpt weights/HF-Diff.pth --one_step

```

## :airplane: Training
### Preparing stage
1. Download the necessary pre-trained model, i.e., pretrained HF-Diff.pth, and inn_pretrained.pt. 
- Download the HF-Diff.pth [(Link)](https://drive.google.com/file/d/12sRBlIObbrmskInfx7bvExd76puXbUhx/view?usp=drive_link).
-Plese copy "HF-Diff.pth" file in the "weights" folder
- Download the high-frequecy perceptual loss (inn_pretrained.pt) [(Link)](https://drive.google.com/file/d/1UQzd5og3YvZkIJ3IfgykCctLpULFUzHU/view?usp=drive_link)

2. Adjust the data path in the config file. Specifically, correct and complete paths in files of [traindata](./traindata/)
3. Adjust batchsize according your GPUS.
    + configs.train.batch: [training batchsize, validation btatchsize]
    + configs.train.microbatch: total batchsize = microbatch * #GPUS * num_grad_accumulation
### Train the model
```sh
 python3 -m torch.distributed.run --nproc_per_node=2 main_distill.py --cfg_path configs/HF-Diff.yaml --save_dir logs/HF-Diff

```
We find that the model can converge very quickly, e.g., a few thousand iterations. Therefore, we believe that the proposed method could be applied to other diffuson-based SR models and encourage a try if you are interested.

## :heart: Acknowledgement

This project is based on [SinSR](https://github.com/wyf0912/SinSR.git). Thanks for the help from the author.

This project is based on [ResShift](https://github.com/zsyOAOA/ResShift). Thanks for the help from the author.



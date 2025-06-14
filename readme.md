
---

# Mediastinal Lymph Node Detection and Segmentation Using Deep Learning

This repository contains code for automatic detection and segmentation of mediastinal lymph nodes from CT images using a modified UNet++ architecture. The method enhances the segmentation accuracy by integrating bilinear interpolation and a total generalized variation (TGV) based upsampling strategy.

The system was trained and tested using CT image data from TCIA, 5-patient dataset, and the ELCAP public dataset. The modified UNet++ achieved superior performance compared to existing state-of-the-art methods.

## 🔬 Paper

If you use this code or find it helpful in your research, **please cite** our IEEE Access publication:

> **A. -A. Nayan, B. Kijsirikul and Y. Iwahori**, "Mediastinal Lymph Node Detection and Segmentation Using Deep Learning," in *IEEE Access*, vol. 10, pp. 89289-89307, 2022, doi: [10.1109/ACCESS.2022.3198996](https://doi.org/10.1109/ACCESS.2022.3198996).

---

## 📁 Repository Contents

* `convert.py` – Converts DICOM series to NIfTI format using `dicom2nifti`.
* `nii.py` – Contains utilities related to NIfTI processing.
* `process_data.py` – Converts raw images and JSON annotations into image-mask pairs.
* `P1.ipynb`, `P2.ipynb`, `P3.ipynb` – Notebooks for training, evaluation, and experiments.
* `README.md` – This file.

---

## 🛠️ Setup Guide

### 1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

If not already installed, download and install Miniconda for your OS.

### 2. Create and Activate Environment

Open terminal (or Anaconda Prompt) and run:

```bash
conda create -n lymphnode python=3.8 -y
conda activate lymphnode
```

### 3. Install Required Packages

Install required dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install these manually:

```bash
pip install numpy opencv-python tqdm pydicom matplotlib imageio nibabel scikit-image dicom2nifti
```

---

## ▶️ How to Run

### Step 1: Convert DICOM to NIfTI

```bash
python convert.py
```

This will convert DICOM directories to `.nii` files.

### Step 2: Convert `.nii` files and annotations to image-mask pairs

```bash
python process_data.py
```

Make sure the dataset structure is as expected, and that JSON annotation files are correctly paired.

### Step 3: Run Experiments

Open the provided notebooks:

* `P1.ipynb` – Preprocessing and setup.
* `P2.ipynb` – Model training.
* `P3.ipynb` – Evaluation and metrics.

You can run these using Jupyter:

```bash
jupyter notebook
```

---

## 🧠 Model Highlights

* Modified UNet++ with:

  * Bilinear interpolation
  * TGV-based upsampling
* Preserves image resolution and texture discontinuities
* Trained on combination datasets with expert annotation

### 📊 Best Performance (COMBO\_3)

* **Accuracy**: 94.8%
* **Jaccard Index**: 91.9%
* **Recall**: 94.1%
* **Precision**: 93.1%

---

## 📢 Citation Request

If this work contributes to your research, **please cite us**:

```bibtex
@article{nayan2022mediastinal,
  title={Mediastinal Lymph Node Detection and Segmentation Using Deep Learning},
  author={Nayan, A-A and Kijsirikul, Boonserm and Iwahori, Yutaka},
  journal={IEEE Access},
  volume={10},
  pages={89289--89307},
  year={2022},
  publisher={IEEE},
  doi={10.1109/ACCESS.2022.3198996}
}
```

---

## 📬 Contact

For questions or collaborations, feel free to reach out to the authors via the publication link.

---


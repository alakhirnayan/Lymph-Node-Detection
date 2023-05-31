import dicom2nifti
import os
from glob import glob

path = '/home/al-akhir/Music/DcmtoNii/input/*'
path_out_data = '/home/al-akhir/Music/DcmtoNii/Output'
path_one_patient = ''

#dicom2nifti.dicom_series_to_nifti(path_one_patient, os.path.join(path_out_data, 'output_1.nii.gz'))

for i, patient in enumerate(glob(path)):
	dicom2nifti.dicom_series_to_nifti(patient, os.path.join(path_out_data, 'output_'+ str(i+1)+'.nii'))

# Student Exam Performance Predictor

The Student Exam Performance Indicator is a machine learning model developed to predict and analyze student performance based on various factors. This model takes into account the following input parameters:

- **Gender**: The gender of the student, which can be either male or female.<br>
- **Race or Ethnicity**: The race or ethnicity of the student, capturing diverse cultural backgrounds.<br>
- **Parental Level of Education**: The highest level of education completed by the student's parents or guardians.<br>
- **Lunch Type**: The type of lunch the student receives, indicating socio-economic status.<br>
- **Test Preparation Course**: Whether or not the student completed a test preparation course.<br>
- **Writing Score:** The student's score in the writing section of the exam.<br>
- **Reading Score**: The student's score in the reading section of the exam.

By analyzing these parameters along with the subject scores, the model aims to predict and provide insights into student performance. It identifies patterns, correlations, and trends among the factors and academic outcomes, helping educators, policymakers, and researchers understand the influences on student success.

## Installation

1. First clone the repository or download the zip by clicking on the code dropdown.
2. Open **Anaconda Prompt Powershell** <code>Hello</code>or **Anaconda Prompt (Anaconda3)** from your startup. It should show something like this: 
```bash
(base) PS C:\Users\User_Name >
```

3. Change the directory by copying and pasting the folder path where you cloned the repository by using the following command:
```bash
(base) PS C:\Users\User_Name > cd cloned_repo_path
```

4. Open the repository in **Vs Code** by using the following command:
```bash
(base) PS C:\Users\User_Name\cloned_repo_path > code .
```

5. Open **Bash** or **Powershell** in **Vs Code**.

6. Create a conda environment by using the following command:
```bash
conda create -p venv python==3.8 -y
```    

7. Activate the conda environment by using the following command:
```bash
conda activate venv/
```    

8. Install all the necessary packages by using the following command:
```bash
pip install -r requirements.txt
```    

9. Now run **Flask Application** by running this command:
```bash
python application.py
```    

## Deployment

The Project is deployed on **Aws Cloud** using **Aws Beanstalk** and **Aws CodePipeline**.

Any and all changes in the repository will be 
reflected on the main **Aws Cloud App** when released.

Live Website: http://studentperformance.ap-southeast-2.elasticbeanstalk.com/

## Demo

<p align="center">
  <img src="https://github.com/MuhammadBilal848/Portfolio-Website/blob/portfolio/icons/studentperformance.gif" alt="Image description" style="border-radius: 10px;">
</p>

**Youtube**: https://www.youtube.com/watch?v=ByN2PAirFNM

## Authors

- [@MuhammadBilal848](https://github.com/MuhammadBilal848)
    - Implemented End-to-End Project.
- [@AraibKhan](https://github.com/AraibKhan)
    - Handled Front-End.

## Dataset

The dataset is taken from **Kaggle**.

**Dataset Link**: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
## License

[MIT](https://choosealicense.com/licenses/mit/)


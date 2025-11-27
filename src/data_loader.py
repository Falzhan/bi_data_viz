import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_student_survey(path=None):
    """Load student survey data from XLSX."""
    if path is None:
        path = os.path.join(BASE_DIR, 'data', 'student_survey.xlsx')
    df = pd.read_excel(path, sheet_name='data')
    # Basic cleaning: drop fully empty rows, reset index
    df = df.dropna(how='all').reset_index(drop=True)
    # Assume first column is country (rename if unnamed or adjust)
    if df.columns[0] == 'Unnamed: 0':
        df = df.rename(columns={'Unnamed: 0': 'country'})
    # Preview
    print(f"Student survey shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    return df

def load_teacher_burnout(path=None):
    """Load teacher burnout data from XLSX."""
    if path is None:
        path = os.path.join(BASE_DIR, 'data', 'teacher_burnout.xlsx')
    # Skip first 2 rows (metadata)
    df = pd.read_excel(path, sheet_name='Data base', skiprows=2)
    # Basic cleaning: drop fully empty rows, reset index, strip column names
    df.columns = df.columns.str.strip().str.replace(':', '', regex=False)
    df = df.dropna(how='all').reset_index(drop=True)
    # Preview
    print(f"Teacher burnout shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    return df

def load_all_data():
    """Load raw XLSX data."""
    student_df = load_student_survey()
    teacher_df = load_teacher_burnout()
    return {'students': student_df, 'teachers': teacher_df}

def load_clean_data():
    """Load cleaned CSV data."""
    students_path = os.path.join(BASE_DIR, 'data', 'processed', 'student_survey_clean.csv')
    teachers_path = os.path.join(BASE_DIR, 'data', 'processed', 'teacher_burnout_clean.csv')
    students = pd.read_csv(students_path)
    teachers = pd.read_csv(teachers_path)
    print(f"Clean students shape: {students.shape}")
    print(f"Clean teachers shape: {teachers.shape}")
    return {'students': students, 'teachers': teachers}

def clean_and_export_student():
    """Clean student data and export to CSV."""
    df = load_student_survey()
    out_path = os.path.join(BASE_DIR, 'data', 'processed', 'student_survey_clean.csv')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Cleaned student data saved to {out_path}")
    return df

def clean_and_export_teacher():
    """Clean teacher data and export to CSV."""
    df = load_teacher_burnout()
    out_path = os.path.join(BASE_DIR, 'data', 'processed', 'teacher_burnout_clean.csv')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Cleaned teacher data saved to {out_path}")
    return df

def clean_and_export_all():
    """Clean and export both datasets to CSV."""
    clean_and_export_student()
    clean_and_export_teacher()

if __name__ == '__main__':
    clean_and_export_all()
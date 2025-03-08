from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from recommender import recommend_jobs, format_recommendations
from course import recommend_courses

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

CORS(app)  

# Load datasets
jobs_df = pd.read_csv(r"C:\Users\Asus\Contacts\Desktop\data sci projects\career path recommendation\processed_naukri.csv")
courses_df = pd.read_csv(r"C:\Users\Asus\Contacts\Desktop\data sci projects\career path recommendation\coursea_data.csv")

@app.route('/')
def home():
    return "Welcome to the Career Path Recommendation API!"

@app.route('/recommend_jobs', methods=['POST'])
def job_recommendation():
    try:
        data = request.get_json()
        user_skills = data.get('skills', [])
        top_n = data.get('top_n', 10)
        
        if not user_skills:
            return jsonify({"error": "No skills provided"}), 400
        
        recommended_jobs = recommend_jobs(user_skills, top_n)
        
        # Convert recommended_jobs to a simple list of strings
        formatted_jobs = [
            f"Job Title: {job['Job Title']}, Role: {job['Role']}, Industry: {job['Industry']}, Match: {job['Match Percentage']}%, Missing Skills: {', '.join(job['Missing Skills']) if job['Missing Skills'] else 'None'}"
            for job in recommended_jobs
        ]
        
        return jsonify({"recommended_jobs": formatted_jobs})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/recommend_courses', methods=['POST'])
def course_recommendation():
    try:
        data = request.get_json()
        missing_skills = data.get('missing_skills', '')
        top_n = data.get('top_n', 5)
        
        if not missing_skills:
            return jsonify({"error": "No missing skills provided"}), 400
        
        # Split the input string into a list of skills if it's not already a list
        missing_skills_list = missing_skills.split(',') if isinstance(missing_skills, str) else missing_skills
        
        missing_skills_str = ', '.join(missing_skills_list)
        recommended_courses = recommend_courses(missing_skills_str)
        
        # Format the output to include rating and enrollment
        formatted_courses = []
        for _, row in recommended_courses.iterrows():
            # Access columns only if they exist
            course_title = row.get('course_title', '')
            course_org = row.get('course_organization', '')
            course_diff = row.get('course_difficulty', '')
            
            # Get rating and enrollment if available
            rating_str = f", Rating: {row['course_rating']}" if 'course_rating' in row else ''
            
            # Format enrollment if available
            enrolled_str = ''
            if 'course_students_enrolled' in row:
                num = row['course_students_enrolled']
                if isinstance(num, (int, float)) and num >= 1000:
                    enrolled_str = f", Enrolled: {num/1000:.1f}k".replace('.0k', 'k')
                else:
                    enrolled_str = f", Enrolled: {num}"
            
            formatted_course = f"{course_title} by {course_org} (Difficulty: {course_diff}{rating_str}{enrolled_str})"
            formatted_courses.append(formatted_course)
        
        return jsonify({"recommended_courses": formatted_courses})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

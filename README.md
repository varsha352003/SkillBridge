# SkillBridge-Job-Course-Recommender

In today's competitive job market, finding the right career path and identifying skill gaps can be overwhelming. Our project, Career Navigator, is a powerful AI-driven tool that helps users discover top job opportunities, analyze their skill gaps, and receive tailored course recommendations to upskill efficiently. This system leverages TF-IDF and Cosine Similarity to provide personalized career insights and learning pathways.

### Technologies Used
- **Backend:** Python Flask
- **Frontend:** React.js
- **Machine Learning Techniques:** TF-IDF, Cosine Similarity

### How It Works

#### 1. Job & Career Recommendation with Skill Gap Analysis
The user inputs their current skills (e.g., Python, SQL, Machine Learning). Using **TF-IDF and Cosine Similarity**, the system compares the entered skills with a database of job descriptions to calculate a **matching score** for various job roles. The system then:
- Identifies the best-fit jobs based on similarity scores.
- Highlights missing skills required for each role.
- Provides a **skill gap analysis**, showing which skills the user lacks and needs to learn to qualify for their desired roles.

#### 2. Course Recommendation Based on Skill Gaps
After identifying missing skills, the user can enter them into the system. The system then scans a **course dataset** and recommends the most relevant courses using **TF-IDF and Cosine Similarity** to match course titles with the missing skills. The recommendations are ranked based on:
- **Relevance** to the missing skills.
- **Course rating** to ensure high-quality learning materials.
- **Difficulty level** to suit learners of all stages.
- **Student enrollment numbers** to indicate popularity and reliability.

With **Career Navigator**, users can efficiently bridge their skill gaps and pursue their ideal job opportunities with confidence.


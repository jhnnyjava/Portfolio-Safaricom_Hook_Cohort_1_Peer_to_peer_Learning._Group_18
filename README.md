# Portfolio-Safaricom_Hook_Cohort_1_Peer_to_peer_Learning._Group_18
# John Khaemba - Portfolio

This is the personal portfolio of John Khaemba, a Frontend Developer, Mechanical Engineering student, AI prompt Engineer, Volunteer, and Environmental enthusiast. This portfolio showcases various aspects of my skills, projects, education, and experience. It is designed to provide a comprehensive view of my professional background, abilities, and personal interests.

**Features**
**Personalized Introduction**: "Hello, it’s me" section, introducing who I am and what I do.
**Responsive Design**: Optimized for both mobile and desktop devices.
**Hover Effects**: Interactive hover effects on elements like the profile image, with smooth transitions.
**Dark Mode Toggle**: A dark mode option to switch between light and dark themes for better accessibility.
**Navigation Bar**: Links to different sections such as About, Skills, Education, Contact, and Social Media (Twitter, LinkedIn).
**Profile Image**: A circular image with a border and shadow effect, which enlarges slightly when hovered over.
**Social Media Links**: Direct access to my professional profiles on social media.
**Smooth Transitions**: Interactive transitions for various elements for a polished look and feel.
**Backend Integration**: Contact form functionality using Python's Flask framework to handle form submissions.


## Technologies Used

- **HTML5**: Structure and content for the webpage.
- **Python**: Use as the backend language.(Flask framework)
- **CSS3**: Styling, layout design, transitions, and responsiveness.
- **JavaScript**: Interactive elements, including the dark mode toggle functionality.
- **Flexbox**: Layout system used for centering elements and creating flexible layouts.
- **Media Queries**: For making the portfolio responsive on various screen sizes.
- **Git**: Version control for managing the project.

**Project Structure**
**templates/**: Contains the index.html file (required for Flask backend).
**static/**: Contains CSS, JavaScript, and image assets.
**app.py**: Flask backend to handle dynamic functionality, such as form submissions.
**messages.txt**: Stores contact form submissions locally (during testing).

## Setup Instructions

Follow these instructions to run this project locally on your machine.

### Prerequisites

Ensure you have the following installed:

- [Git](https://git-scm.com/)
- [Visual Studio Code (or any other code editor)](https://code.visualstudio.com/)
- A browser like Chrome or Firefox to preview the website.

### Steps to Run Locally

1. **Clone the repository**:
   
   First, clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/portfolio.git
Navigate to the project folder:

Change to the project directory:

bash
Copy code
cd portfolio
Open the project in your code editor:

Open the project in Visual Studio Code (or your preferred editor):

bash
Copy code
code .

**Deployment Instructions**
**Option 1: Deploy as a Static Website on GitHub Pages**
If you don't require backend functionality (e.g., the contact form):

Extract the Rendered HTML:

Run the Flask app locally using python app.py.
Open the app in your browser (http://127.0.0.1:5000/) and save the page as static index.html.
Organize Files:

Place index.html in the root of your repository.
Move CSS and other assets to the root directory (e.g., style.css).
Push to GitHub:

Commit the changes and push to your GitHub repository.
Enable GitHub Pages:
Go to Settings > Pages.
Select the main branch and the / (root) folder.
Access Your Website:

Your site will be live at https://<your-username>.github.io/<repository-name>/.
**Option 2: Deploy as a Flask Application**
If you need backend functionality (e.g., the contact form):

Choose a Hosting Platform:

Use platforms like Render, PythonAnywhere, or Heroku.
Set Up the Deployment:

Push your entire project (including app.py, templates, and static folders) to GitHub.
On the hosting platform:
Connect your GitHub repository.
Set the Start Command to gunicorn app:app.
Ensure that all environment variables (if any) are configured.
Test Your Deployment:

After the deployment is complete, the platform will provide you with a URL where your Flask app is live.
**Hybrid Approach**
If you want to use GitHub Pages for the static version and Flask for the backend:

Deploy the static version on GitHub Pages (as described in Option 1).
Deploy the Flask backend (as described in Option 2).
Use AJAX or fetch requests in your static site to interact with the Flask API for dynamic features like the contact form.
Known Issues
Contact Form on GitHub Pages: The contact form will not work on GitHub Pages since it requires Flask to process submissions.
Gmail SMTP Authentication: Ensure you use an App Password for Gmail (not your primary Gmail password). Follow these instructions to generate an App Password for secure email sending.
Future Improvements
Deploy a fully dynamic version of the portfolio on a Flask-compatible host.
Add more animations and interactivity.


bash
Copy code
python -m http.server
Or use Node.js-based servers like http-server.

Customization:

To customize the portfolio, simply modify the HTML in the index.html file and the styles in style.css.
Update the content sections, including your About, Skills, Education, and Contact information.
Screenshots


**Contributing**
Feel free to fork this repository and make improvements! If you would like to contribute to this project, follow the instructions below.

**Steps for Contribution**
Fork the repository.
Create a feature branch (git checkout -b feature-name).
Commit your changes (git commit -m 'Add feature').
Push to the branch (git push origin feature-name).
Open a pull request.
License
This project is open source and available under the MIT License.

**Contact**
LinkedIn: John Khaemba Sumba
Twitter: @johnkhaemba16
Email: johnkhaemba710@example.com
Thank you for checking out my portfolio! I hope it provides insight into my skills, projects, and passion for development. Feel free to reach out to me for any inquiries or collaboration opportunities.

markdown
Copy code

### Key Sections in the README:
1. **Features**: Lists the key features of your portfolio.
2. **Technologies Used**: Specifies the technologies used to build the portfolio.
3. **Setup Instructions**: A clear guide on how others can set up and run the portfolio locally.
4. **Contributing**: Provides instructions for anyone who wants to contribute to the project.
5. **License**: Mentions the open-source license (MIT by default).
6. **Contact**: Your contact details for networking or collaboration.








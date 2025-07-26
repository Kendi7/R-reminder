

**Project Title**: Rent Reminder Automation via GitHub Actions

**Project Description**:
This project automates the process of sending daily rent reminder emails using GitHub Actions and Python. Instead of running scripts manually on a local machine or server, this solution leverages GitHub’s CI/CD infrastructure to run a Python script on a scheduled basis (daily at a set time) and send email notifications through Gmail to specified recipients.

---

**Features**:

* Sends daily rent reminder emails.
* Uses GitHub Actions to run automatically at a specified time (UTC-based).
* Credentials and email targets are securely managed using GitHub Secrets.
* No need for local deployment – the entire workflow runs in the cloud.

---

**Technologies Used**:

* Python 3.11
* GitHub Actions
* Gmail (with app-specific password)
* dotenv for environment variable management
* `smtplib` and `email` libraries for sending emails

---

**How It Works**:

1. A GitHub Actions workflow is defined in `.github/workflows/rent_reminder.yml`.
2. The workflow is triggered:

   * Automatically at the scheduled time (`cron`) using UTC.
   * Manually using the `workflow_dispatch` feature, if needed.
3. The workflow sets up Python, installs required dependencies from `requirements.txt`, creates a `.env` file from GitHub Secrets, and runs the `rent_reminder.py` script.
4. The script logs in to the Gmail server using credentials stored securely in GitHub and sends the email reminder.

---

**Setup Instructions**:

1. **Clone the Repository**
   Clone this repository to your local machine if you want to test or modify locally.

2. **Set Up GitHub Secrets**
   Go to your GitHub repository > Settings > Secrets and variables > Actions. Add the following secrets:

   * `EMAIL_ADDRESS`: The sender’s Gmail address (e.g., [yourname@gmail.com](mailto:yourname@gmail.com))
   * `EMAIL_PASSWORD`: Gmail app password (not your regular Gmail password; generate it via [Google’s App Passwords](https://myaccount.google.com/apppasswords))
   * `TO_EMAIL`: The recipient’s email address

3. **Schedule Automation (UTC Time)**
   The script runs based on a cron expression defined in the GitHub Actions file. By default:

   * `cron: "37 10 * * *"` — this runs at 10:37 AM UTC every day (1:37 PM EAT).
     You can adjust the cron time if needed.

4. **Run Manually (Optional)**
   Navigate to the GitHub repo’s Actions tab and manually trigger the workflow using the **"Run workflow"** button under **Rent Reminder**.

---

**Security Notes**:

* Gmail credentials are not stored in the codebase; they are encrypted and stored as GitHub Secrets.
* The `.env` file is created temporarily during workflow execution and not committed to the repository.
* It is recommended to use app-specific passwords for sending emails via Gmail.

---

**License**:
This project is open for personal or internal use. Modify and extend it as needed.

---

**Future Improvements**:

* Add support for multiple recipients.
* Integrate with databases to track who has paid and who hasn’t.
* Customize message content dynamically (e.g., add tenant name or rent amount).
* Support for SMS or WhatsApp notification integration.

---


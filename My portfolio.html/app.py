from flask import Flask, request, jsonify, render_template
import smtplib

# Define the Flask app with an explicit template folder
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")  # Renders the index.html from templates folder

@app.route("/send-message", methods=["POST"])
def send_message():
    try:
        # Get form data
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Process or save the data (e.g., log to a file, send an email, etc.)
        with open("messages.txt", "a") as file:
            file.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n\n")

        # Optionally, send an email (replace with your SMTP server details)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "your-email@gmail.com"  # Your email here
        sender_password = "your-password"  # Your email password or app password
        recipient_email = "recipient-email@gmail.com"  # Recipient's email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            subject = "New Message from Portfolio"
            body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            email_message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, recipient_email, email_message)

        return jsonify({"message": "Message sent successfully!"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "An error occurred while sending the message."}), 500

if __name__ == "__main__":
    app.run(debug=True)

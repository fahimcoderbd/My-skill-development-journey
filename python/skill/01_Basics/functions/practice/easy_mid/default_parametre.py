def send_email(receiver: str, subject: str = "No Subject") -> None:
    print(f"Sending email to {receiver}")
    print(f"Subject: {subject}")

send_email("fahim@gmail.com")
send_email("fahim@gmail.com", "Interview")
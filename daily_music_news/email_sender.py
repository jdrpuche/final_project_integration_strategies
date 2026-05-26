"""Send emails via Gmail."""

import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config

logger = logging.getLogger(__name__)


class GmailSender:
    """Sends emails via Gmail using SMTP."""

    def __init__(self):
        """Initialize the Gmail sender."""
        self.smtp_server = Config.SMTP_SERVER
        self.smtp_port = Config.SMTP_PORT
        self.sender_email = Config.GMAIL_ADDRESS
        self.sender_password = Config.GMAIL_APP_PASSWORD

    def send_email(
        self,
        recipient: str,
        subject: str,
        body_html: str,
        body_text: str = None,
    ) -> bool:
        """Send an email via Gmail.

        Args:
            recipient: Recipient email address
            subject: Email subject
            body_html: HTML body of the email
            body_text: Plain text fallback (auto-generated if not provided)

        Returns:
            True if successful, False otherwise
        """
        try:
            logger.info(f"Preparing email for {recipient}...")

            # Create message
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = self.sender_email
            message["To"] = recipient

            # Plain text fallback
            if not body_text:
                body_text = "Please view this email in HTML format"

            part_text = MIMEText(body_text, "plain")
            part_html = MIMEText(body_html, "html")

            message.attach(part_text)
            message.attach(part_html)

            # Send email
            logger.info("Connecting to Gmail SMTP server...")
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                logger.info("Logging in...")
                server.login(self.sender_email, self.sender_password)
                logger.info(f"Sending email to {recipient}...")
                server.sendmail(self.sender_email, recipient, message.as_string())

            logger.info(f"✅ Email sent successfully to {recipient}")
            return True

        except smtplib.SMTPAuthenticationError:
            logger.error(
                "Gmail authentication failed. Check your email and app password."
            )
            return False
        except smtplib.SMTPException as e:
            logger.error(f"SMTP error occurred: {e}")
            return False
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            return False

    def send_music_news_digest(self, summary_html: str, recipient: str = None) -> bool:
        """Send the music news digest.

        Args:
            summary_html: HTML formatted summary
            recipient: Recipient email (uses Config if not provided)

        Returns:
            True if successful
        """
        recipient = recipient or Config.RECIPIENT_EMAIL
        subject = "🎵 Your Daily Music News Digest"
        return self.send_email(recipient, subject, summary_html)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Test email sender
    sender = GmailSender()
    test_html = """
    <h2>Test Music News</h2>
    <p>This is a test email from the Daily Music News Bot.</p>
    """
    sender.send_music_news_digest(test_html)

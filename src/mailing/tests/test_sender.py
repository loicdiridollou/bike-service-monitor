"""Test functions for the mailing.sender module"""
import mailing.sender as ms


def test_email_sender():
    """Test function for the email_sender"""
    ms.email_sender(message="Random message", test_mode=True)

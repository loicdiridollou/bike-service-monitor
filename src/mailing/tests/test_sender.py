"""Test functions for the mailing.sender module"""
import pytest
import mailing.sender as ms


@pytest.mark.skip(reason="Password issues")
def test_email_sender():
    """Test function for the email_sender"""
    ms.email_sender(message="Random message", test_mode=True)

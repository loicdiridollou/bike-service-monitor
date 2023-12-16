"""Test functions for the mailing.sender module."""
import pytest

import src.mailing.sender as ms
import src.mailing.ses_sender as mses


@pytest.mark.skip(reason="Password issues")
def test_email_sender():
    """Test function for the email_sender."""
    ms.email_sender(message="Random message", test_mode=True)


@pytest.mark.skip(reason="Not passing credentials yet to Github")
def test_ses_sender():
    """Test function for the SES email sender."""
    mses.send_email(recipients=["ld.app.testing@gmail.com"])

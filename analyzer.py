import re
from urllib.parse import urlparse
import ipaddress


def is_ip(domain):
    try:
        ipaddress.ip_address(domain)
        return True
    except:
        return False


def analyze_url(url):
    score = 100
    reasons = []

    parsed = urlparse(url)

    # Check HTTPS
    if parsed.scheme != "https":
        score -= 20
        reasons.append("URL is not using HTTPS.")

    domain = parsed.netloc

    # Check IP address
    if is_ip(domain):
        score -= 30
        reasons.append("Using IP address instead of domain name.")

    # Long URL
    if len(url) > 75:
        score -= 15
        reasons.append("URL is unusually long.")

    # Suspicious words
    suspicious_words = [
        "login",
        "verify",
        "update",
        "secure",
        "bank",
        "paypal",
        "free",
        "winner",
        "gift",
        "claim"
    ]

    found = [
        word for word in suspicious_words
        if word in url.lower()
    ]

    if found:
        score -= len(found) * 5
        reasons.append(
            f"Contains suspicious words: {', '.join(found)}"
        )

    # Too many subdomains
    if domain.count(".") > 3:
        score -= 15
        reasons.append("Too many subdomains.")

    # Special characters
    special_chars = len(
        re.findall(r'[@!#$%^&*()+={}|<>]', url)
    )

    if special_chars > 3:
        score -= 10
        reasons.append("Contains excessive special characters.")

    # Final verdict
    if score >= 80:
        verdict = "SAFE"
    elif score >= 50:
        verdict = "SUSPICIOUS"
    else:
        verdict = "DANGEROUS"

    if not reasons:
        reasons.append(
            "No suspicious indicators detected."
        )

    return {
        "verdict": verdict,
        "score": score,
        "reasons": reasons
    }
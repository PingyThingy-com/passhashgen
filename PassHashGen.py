import sys
import secrets
from werkzeug.security import generate_password_hash

# ==============================================================================
# PingyThingy Automated Credential Generator
#
# This script is designed to be called from an automated bash script.
# It takes a password as a command-line argument and prints a new password
# hash and a new secret key to standard output, each on a new line.
#
# Usage (from bash):
# python3 password_generator.py "the-password-to-hash"
#
# Output:
# pbkdf2:sha256:1000000$salt$hash
# a_long_hex_secret_key
# ==============================================================================

def generate_credentials(password):
    """
    Generates a password hash and a secret key from the provided password.
    Prints the hash and key to standard output on separate lines.
    """
    # Generate the password hash using a strong method.
    # The method string includes the algorithm, salt, and hash,
    # making it self-contained.
    try:
        password_hash = generate_password_hash(
            password,
            method='pbkdf2:sha256:1000000',  # High number of iterations for security
            salt_length=16
        )

        # Generate a new, cryptographically secure secret key for JWT signing.
        secret_key = secrets.token_hex(32)

        # Print the raw values, each on a new line, for easy capture by a script.
        print(password_hash)
        print(secret_key)

    except Exception as e:
        # Print any errors to stderr to avoid polluting the output
        print(f"Error generating credentials: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    # Check if the password argument was provided
    if len(sys.argv) < 2:
        print("Usage: python3 password_generator.py '<password>'", file=sys.stderr)
        sys.exit(1)

    # The first argument (index 0) is the script name,
    # so the password is at index 1.
    user_password = sys.argv[1]
    
    generate_credentials(user_password)


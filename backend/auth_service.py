from passlib.context import CryptContext
import os
from typing import Optional
import logging

logger = logging.getLogger(__name__)

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Hash a password"""
    return pwd_context.hash(password)

def verify_admin_credentials(username: str, password: str) -> bool:
    """
    Verify admin credentials against environment variables
    Returns True if credentials are valid
    """
    admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
    admin_password_hash = os.environ.get('ADMIN_PASSWORD_HASH')
    
    # If no hash is set, use default password (only for development)
    if not admin_password_hash:
        logger.warning("Using default admin password. Please set ADMIN_PASSWORD_HASH in production!")
        admin_password_hash = get_password_hash('admin123')
    
    # Check username
    if username != admin_username:
        return False
    
    # Verify password
    return verify_password(password, admin_password_hash)

def change_admin_password(old_password: str, new_password: str, username: str) -> tuple[bool, str]:
    """
    Change admin password
    Returns (success: bool, message: str)
    """
    # Verify old password first
    if not verify_admin_credentials(username, old_password):
        return False, "Current password is incorrect"
    
    # Hash new password
    new_hash = get_password_hash(new_password)
    
    # Return the new hash (caller should update .env file)
    return True, new_hash

def get_default_password_hash() -> str:
    """Get hash for default password (admin123)"""
    return get_password_hash('admin123')

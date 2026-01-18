# Admin Password Reset Guide

## If You Forgot Your Admin Password

Don't worry! There are two ways to reset your admin password:

### Method 1: Reset to Default Password (Easiest)

1. **Stop the backend server**:
   ```bash
   sudo supervisorctl stop backend
   ```

2. **Edit the .env file**:
   ```bash
   nano /app/backend/.env
   ```

3. **Comment out or remove the ADMIN_PASSWORD_HASH line**:
   ```env
   # ADMIN_PASSWORD_HASH=$2b$12$...
   ```

4. **Restart the backend**:
   ```bash
   sudo supervisorctl start backend
   ```

5. **Login with default credentials**:
   - Username: `admin`
   - Password: `admin123`

6. **Immediately change your password** using the "Change Password" button in admin panel

---

### Method 2: Generate New Password Hash (For Custom Password)

If you want to set a specific password without logging in:

1. **Run this Python script** in the backend directory:
   ```bash
   cd /app/backend
   python3 -c "from auth_service import get_password_hash; print(get_password_hash('your-new-password'))"
   ```

2. **Copy the generated hash**

3. **Update .env file**:
   ```bash
   nano /app/backend/.env
   ```

4. **Replace the ADMIN_PASSWORD_HASH value**:
   ```env
   ADMIN_PASSWORD_HASH=<paste-the-hash-here>
   ```

5. **Restart backend**:
   ```bash
   sudo supervisorctl restart backend
   ```

---

## How to Change Password (When Logged In)

1. Login to admin panel
2. Click "Change Password" button in the header
3. Enter:
   - Current password
   - New password (minimum 6 characters)
   - Confirm new password
4. Click "Change Password"
5. Copy the new password hash from the alert
6. Update the ADMIN_PASSWORD_HASH in /app/backend/.env
7. Restart backend: `sudo supervisorctl restart backend`

---

## Security Best Practices

✅ **DO**:
- Change default password immediately after deployment
- Use strong passwords (mix of letters, numbers, symbols)
- Keep your .env file secure and private
- Never commit .env file to version control
- Regularly update your password

❌ **DON'T**:
- Share your admin credentials
- Use simple passwords like "password123"
- Keep default password in production
- Share your password hash publicly

---

## Troubleshooting

**"Invalid credentials" error after changing password?**
- Check if you updated the ADMIN_PASSWORD_HASH in .env file
- Verify you restarted the backend server
- Make sure there are no extra spaces in the hash

**Backend won't start after changing password?**
- Check backend logs: `tail -f /var/log/supervisor/backend.err.log`
- Verify the hash format is correct (should start with $2b$)
- Try resetting to default password using Method 1

**Forgot to save the password hash?**
- Change password again through the admin panel
- Or use Method 2 to generate a new hash

---

## Need Help?

If you're still having issues:
1. Check backend logs for errors
2. Verify all environment variables are set correctly
3. Try resetting to default password
4. Contact support if problem persists

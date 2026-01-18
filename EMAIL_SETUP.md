# Email Configuration Guide

## Setting Up Email Notifications

The appointment confirmation email system is ready but requires SMTP credentials to be configured after deployment.

### For Gmail SMTP:

1. **Enable 2-Factor Authentication** on your Gmail account
   - Go to: https://myaccount.google.com/security
   - Enable 2-Step Verification

2. **Generate App Password**
   - Go to: https://myaccount.google.com/apppasswords
   - Select "Mail" and your device
   - Copy the generated 16-character password

3. **Update Environment Variables** in `/app/backend/.env`:
   ```env
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_EMAIL=your-email@gmail.com
   SMTP_PASSWORD=your-16-char-app-password
   ```

4. **Restart Backend Server**:
   ```bash
   sudo supervisorctl restart backend
   ```

### For Other Email Providers:

#### **Outlook/Office365**:
```env
SMTP_SERVER=smtp.office365.com
SMTP_PORT=587
SMTP_EMAIL=your-email@outlook.com
SMTP_PASSWORD=your-password
```

#### **Custom SMTP Server**:
```env
SMTP_SERVER=your-smtp-server.com
SMTP_PORT=587
SMTP_EMAIL=your-email@domain.com
SMTP_PASSWORD=your-password
```

### Testing Email Notifications:

1. Book an appointment from the website with a valid email
2. Login to admin panel
3. Confirm the appointment
4. Check backend logs: `tail -f /var/log/supervisor/backend.err.log`
5. Patient should receive confirmation email

### Email Content Includes:

- ✅ Appointment confirmation message
- ✅ Service details
- ✅ Date and time
- ✅ Clinic address and contact number
- ✅ Business hours
- ✅ Important instructions (arrive 10 mins early, cancellation policy)

### Troubleshooting:

**Email not sending?**
- Check if SMTP credentials are correct
- Verify 2FA is enabled and App Password is generated
- Check backend logs for error messages
- Test SMTP credentials with a simple email client

**"SMTP credentials not configured" in logs?**
- Environment variables are not set or commented out
- Uncomment the SMTP_ variables in .env file
- Restart backend server

### Security Notes:

- ✅ App Passwords are safer than regular passwords
- ✅ Credentials stored in .env file (not in code)
- ✅ .env file should be in .gitignore
- ✅ System gracefully handles missing credentials (won't crash)

---

**Current Status**: System is ready. Add credentials when you're ready to enable email notifications!

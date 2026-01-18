# Production Deployment Checklist

## ✅ Pre-Deployment Checklist

### 1. Content Verification
- [ ] Clinic name, address, and phone number are correct
- [ ] Business hours are accurate
- [ ] All service descriptions are finalized
- [ ] Gallery images are uploaded (your clinic photos)
- [ ] Google Maps location is showing correctly
- [ ] Email address for notifications is correct

### 2. Functionality Testing
- [ ] Test appointment booking form
- [ ] Verify all navigation links work
- [ ] Test "Learn More" buttons for each service
- [ ] Check admin login works (username: admin, password: admin123)
- [ ] Test password change in admin panel
- [ ] Verify appointment confirmation in admin dashboard
- [ ] Test mobile responsiveness

### 3. Admin Panel Setup
- [ ] Change default admin password immediately after deployment
- [ ] Test appointment management (confirm/cancel)
- [ ] Test gallery image upload/delete
- [ ] Verify email notifications are configured

### 4. Email Configuration (Important!)
Before deployment, add these to your environment variables:
```
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=your-clinic-email@gmail.com
SMTP_PASSWORD=your-gmail-app-password
```

**How to get Gmail App Password:**
1. Go to Google Account → Security
2. Enable 2-Factor Authentication
3. Search "App Passwords"
4. Generate password for "Mail"
5. Copy the 16-character password

### 5. Security
- [ ] Change admin password from default
- [ ] Review admin credentials security
- [ ] Ensure SMTP password is set securely

## 🚀 Deployment Steps

### Step 1: Preview & Test
1. Click "Preview" in Emergent
2. Test all features thoroughly
3. Check on mobile device

### Step 2: Deploy
1. Click "Deploy" button
2. Click "Deploy Now"
3. Wait 10-15 minutes
4. Get your live URL

**Cost:** 50 credits/month per deployed app

### Step 3: Domain Setup (Optional but Recommended)

**Purchase Domain:**
- Recommended: Namecheap, GoDaddy, Domain.com
- Suggested domains:
  - happyteethkharar.com
  - happyteethdentalclinic.com
  - bestdentistkharar.com

**Connect Domain in Emergent:**
1. Click "Link domain" in deployment settings
2. Enter your domain name
3. Follow Entri instructions
4. Update DNS settings (remove all A records)
5. Wait 5-15 minutes

**SSL Certificate:** Automatic (HTTPS enabled by default)

## 📧 Post-Deployment Configuration

### Email Setup (Critical!)
1. Add SMTP credentials in Emergent environment variables
2. Test by booking an appointment
3. Confirm appointment in admin panel
4. Check if patient receives email

### Test Production Site
- [ ] Book a test appointment
- [ ] Receive confirmation email
- [ ] Login to admin panel
- [ ] Confirm the appointment
- [ ] Verify email sent successfully

## 🎯 Go-Live Steps

### 1. Final Checks
- [ ] All contact information correct
- [ ] Email notifications working
- [ ] Admin access working
- [ ] Mobile responsive
- [ ] Fast loading speed

### 2. Marketing & SEO
- [ ] Add site to Google Search Console
- [ ] Submit sitemap
- [ ] Set up Google My Business
- [ ] Link from social media profiles
- [ ] Add to online directories

### 3. Inform Patients
- [ ] Update social media with website link
- [ ] Send email/SMS to existing patients
- [ ] Update Google My Business
- [ ] Print website on business cards

## 📊 Monitoring & Maintenance

### Regular Tasks
- [ ] Check admin panel daily for new appointments
- [ ] Respond to appointment requests within 24 hours
- [ ] Update gallery with new clinic photos
- [ ] Keep business hours updated
- [ ] Monitor email notifications

### Monthly Tasks
- [ ] Review and respond to all appointments
- [ ] Update any changed information
- [ ] Check website loading speed
- [ ] Backup important data

## 🆘 Troubleshooting

### Website Not Loading?
- Check DNS settings (remove all A records)
- Wait up to 24 hours for DNS propagation
- Contact Emergent support

### Emails Not Sending?
- Verify SMTP credentials in environment variables
- Check Gmail App Password is correct
- Restart backend after adding credentials
- Test with your own email first

### Forgot Admin Password?
- See `/app/PASSWORD_RESET_GUIDE.md`
- Option 1: Reset to default (admin123)
- Option 2: Generate new hash via Python script

### Domain Issues?
- Remove all existing A records
- Re-link domain through Emergent
- Wait 15 minutes for propagation
- Clear browser cache

## 📞 Important Contacts

**Your Website Admin:**
- Username: admin
- Password: (change immediately after deployment)
- Admin URL: yoursite.com/admin

**Emergent Support:**
- For deployment issues
- For domain setup help
- For technical problems

## 💰 Ongoing Costs

- **Deployment:** 50 credits/month
- **Domain Name:** ~$10-15/year (separate purchase)
- **Email Service:** Free (Gmail) or paid options

## ✨ Optional Enhancements (After Launch)

- [ ] Add Google Analytics for visitor tracking
- [ ] Set up Facebook Pixel
- [ ] Add WhatsApp chat widget
- [ ] Integrate online payment for deposits
- [ ] Add patient testimonials section
- [ ] Create blog for dental tips
- [ ] Add before/after gallery

---

## 🎉 Ready to Go Live?

Once all checkboxes above are complete:
1. ✅ Content verified
2. ✅ Email configured
3. ✅ Admin password changed
4. ✅ Deployed successfully
5. ✅ Domain connected (if applicable)
6. ✅ All features tested

**Your professional dental clinic website is ready for patients!**

---

**Need Help?** Contact Emergent support or refer to the documentation in:
- `/app/EMAIL_SETUP.md` - Email configuration
- `/app/PASSWORD_RESET_GUIDE.md` - Password recovery
- Support chat in Emergent platform

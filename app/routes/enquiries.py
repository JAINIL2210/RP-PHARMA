import os
import uuid
import re
from flask import Blueprint, request, jsonify, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from app.models import db, Enquiry

enquiries_bp = Blueprint('enquiries', __name__)

def is_valid_email(email):
    """Validate email pattern."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email.strip()))

def allowed_file(filename):
    """Check if file extension is allowed."""
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in current_app.config['ALLOWED_EXTENSIONS']

@enquiries_bp.route('/enquiry/submit', methods=['POST'])
def submit_enquiry():
    """Handle all B2B and general enquiry submissions."""
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.is_json
    
    # Honeypot Anti-Spam Check (hidden field in HTML)
    honeypot = request.form.get('website_hp', '').strip()
    if honeypot:
        # Bot detected
        if is_ajax:
            return jsonify({'success': False, 'message': 'Spam detected.'}), 400
        flash('Spam submission detected.', 'danger')
        return redirect(request.referrer or url_for('main.contact'))
        
    enquiry_type = request.form.get('enquiry_type', 'business_partnership').strip()
    full_name = request.form.get('full_name', '').strip()
    company_name = request.form.get('company_name', '').strip()
    business_type = request.form.get('business_type', '').strip()
    email = request.form.get('email', '').strip()
    phone = request.form.get('phone', '').strip()
    country = request.form.get('country', '').strip()
    product_name = request.form.get('product_name', '').strip()
    category = request.form.get('category', '').strip()
    subject = request.form.get('subject', '').strip()
    message = request.form.get('message', '').strip()
    
    # Simple Math Anti-Spam Check if present
    captcha_answer = request.form.get('captcha_answer', '').strip()
    captcha_expected = request.form.get('captcha_expected', '').strip()
    if captcha_expected and captcha_answer != captcha_expected:
        msg = 'Incorrect anti-spam verification code. Please try again.'
        if is_ajax:
            return jsonify({'success': False, 'message': msg}), 400
        flash(msg, 'danger')
        return redirect(request.referrer or url_for('main.business_enquiry'))

    # Validation
    if not full_name:
        msg = 'Please provide your full name.'
        if is_ajax:
            return jsonify({'success': False, 'message': msg}), 400
        flash(msg, 'danger')
        return redirect(request.referrer or url_for('main.contact'))

    if not email or not is_valid_email(email):
        msg = 'Please provide a valid email address.'
        if is_ajax:
            return jsonify({'success': False, 'message': msg}), 400
        flash(msg, 'danger')
        return redirect(request.referrer or url_for('main.contact'))

    if not message:
        msg = 'Please enter your message or enquiry requirements.'
        if is_ajax:
            return jsonify({'success': False, 'message': msg}), 400
        flash(msg, 'danger')
        return redirect(request.referrer or url_for('main.contact'))

    # Handle File Upload (optional)
    uploaded_filename = None
    if 'document' in request.files:
        file = request.files['document']
        if file and file.filename != '':
            if allowed_file(file.filename):
                original_name = secure_filename(file.filename)
                unique_filename = f"{uuid.uuid4().hex[:12]}_{original_name}"
                upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'enquiries', unique_filename)
                file.save(upload_path)
                uploaded_filename = unique_filename
            else:
                msg = 'Invalid file type. Allowed formats: PDF, DOC, DOCX, JPG, PNG.'
                if is_ajax:
                    return jsonify({'success': False, 'message': msg}), 400
                flash(msg, 'danger')
                return redirect(request.referrer or url_for('main.business_enquiry'))

    # Save to Database
    try:
        new_enquiry = Enquiry(
            enquiry_type=enquiry_type,
            full_name=full_name,
            company_name=company_name,
            business_type=business_type,
            email=email,
            phone=phone,
            country=country,
            product_name=product_name,
            category=category,
            subject=subject,
            message=message,
            file_attachment=uploaded_filename,
            status='new',
            ip_address=request.remote_addr
        )
        db.session.add(new_enquiry)
        db.session.commit()
        
        success_msg = 'Thank you. Your enquiry has been received. Our international business team will contact you shortly.'
        if is_ajax:
            return jsonify({
                'success': True,
                'message': success_msg,
                'enquiry_id': new_enquiry.id
            }), 200
            
        flash(success_msg, 'success')
        return redirect(request.referrer or url_for('main.contact'))
        
    except Exception as e:
        db.session.rollback()
        error_msg = 'An error occurred while saving your enquiry. Please try again later.'
        if is_ajax:
            return jsonify({'success': False, 'message': error_msg}), 500
        flash(error_msg, 'danger')
        return redirect(request.referrer or url_for('main.contact'))

<?php
/**
 * RP PHARMA — Form Submission Handler
 */
require_once __DIR__ . '/../includes/functions.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: ../contact.php');
    exit;
}

// 1. Honeypot check (Bots fill hidden field)
if (!empty($_POST['website_hp'])) {
    // Silent drop for spam bot
    header('Location: ../contact.php?status=success');
    exit;
}

// 2. Simple Math Security Question
$captcha_expected = trim($_POST['captcha_expected'] ?? '');
$captcha_answer = trim($_POST['captcha_answer'] ?? '');

if ($captcha_expected !== '' && $captcha_answer !== $captcha_expected) {
    if (!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) === 'xmlhttprequest') {
        header('Content-Type: application/json');
        echo json_encode(['status' => 'error', 'message' => 'Incorrect security question answer.']);
        exit;
    }
    header('Location: ../contact.php?status=captcha_error');
    exit;
}

// 3. Sanitize and Extract Fields
$enquiry_data = [
    'full_name' => sanitize_input($_POST['full_name'] ?? ''),
    'company_name' => sanitize_input($_POST['company_name'] ?? ''),
    'email' => filter_var(trim($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL),
    'phone' => sanitize_input($_POST['phone'] ?? ''),
    'country' => sanitize_input($_POST['country'] ?? ''),
    'enquiry_type' => sanitize_input($_POST['enquiry_type'] ?? 'general_contact'),
    'product_name' => sanitize_input($_POST['product_name'] ?? ''),
    'subject' => sanitize_input($_POST['subject'] ?? ''),
    'message' => sanitize_input($_POST['message'] ?? '')
];

// Validation
if (empty($enquiry_data['full_name']) || empty($enquiry_data['email']) || empty($enquiry_data['message'])) {
    if (!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) === 'xmlhttprequest') {
        header('Content-Type: application/json');
        echo json_encode(['status' => 'error', 'message' => 'Please fill in all required fields.']);
        exit;
    }
    header('Location: ../contact.php?status=required_missing');
    exit;
}

// 4. Save Enquiry
$saved = save_enquiry($enquiry_data);

// 5. Response
if (!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) === 'xmlhttprequest') {
    header('Content-Type: application/json');
    echo json_encode([
        'status' => 'success',
        'message' => 'Thank you. Your message has been received. Our export desk will respond promptly.'
    ]);
    exit;
}

header('Location: ../contact.php?status=success');
exit;

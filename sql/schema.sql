-- ============================================================================
-- RP PHARMA — Database Schema and Seed Data
-- Compatible with MySQL 5.7+, MySQL 8.0+, MariaDB, and SQLite
-- ============================================================================

CREATE DATABASE IF NOT EXISTS `rp_pharma` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `rp_pharma`;

-- ----------------------------------------------------------------------------
-- Table: site_settings
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `site_settings` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `key` VARCHAR(100) NOT NULL UNIQUE,
  `value` TEXT NULL,
  `description` VARCHAR(255) NULL,
  `group` VARCHAR(50) DEFAULT 'general',
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------------------------------------------------------
-- Table: categories
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `categories` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(150) NOT NULL,
  `slug` VARCHAR(150) NOT NULL UNIQUE,
  `type` ENUM('pharmaceutical', 'nutraceutical') NOT NULL,
  `description` TEXT NULL,
  `icon` VARCHAR(100) DEFAULT 'fa-pills',
  `display_order` INT DEFAULT 0,
  `is_active` TINYINT(1) DEFAULT 1,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------------------------------------------------------
-- Table: products
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `products` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(255) NOT NULL,
  `slug` VARCHAR(255) NOT NULL UNIQUE,
  `type` ENUM('pharmaceutical', 'nutraceutical') NOT NULL,
  `category_id` INT NULL,
  `composition` TEXT NOT NULL,
  `dosage_form` VARCHAR(150) NOT NULL,
  `strength` VARCHAR(150) NULL,
  `packaging` VARCHAR(255) NULL,
  `description` TEXT NULL,
  `indications` TEXT NULL,
  `available_markets` VARCHAR(255) NULL,
  `dossier_status` VARCHAR(255) DEFAULT 'Available on Request',
  `stability_status` VARCHAR(255) DEFAULT 'ICH Zone IVb Stability Tested',
  `validation_status` VARCHAR(255) DEFAULT 'Validated Process',
  `coa_status` VARCHAR(255) DEFAULT 'Certificate of Analysis Available',
  `image_url` VARCHAR(255) NULL,
  `is_featured` TINYINT(1) DEFAULT 0,
  `is_active` TINYINT(1) DEFAULT 1,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`category_id`) REFERENCES `categories`(`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------------------------------------------------------
-- Table: enquiries
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `enquiries` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `full_name` VARCHAR(150) NOT NULL,
  `company_name` VARCHAR(150) NULL,
  `email` VARCHAR(150) NOT NULL,
  `phone` VARCHAR(50) NOT NULL,
  `country` VARCHAR(100) NOT NULL,
  `enquiry_type` VARCHAR(50) DEFAULT 'general',
  `product_name` VARCHAR(255) NULL,
  `message` TEXT NOT NULL,
  `status` VARCHAR(50) DEFAULT 'new',
  `ip_address` VARCHAR(50) NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- SEED DATA: Site Settings
-- ============================================================================
INSERT INTO `site_settings` (`key`, `value`, `description`, `group`) VALUES
('company_name', 'RP PHARMA', 'Official Company Name', 'company'),
('tagline', 'Your Trusted Partner in Pharmaceuticals & Nutraceuticals', 'Brand Tagline', 'company'),
('office_address', '[Complete Corporate Office Address], India', 'Corporate Address', 'contact'),
('official_phone', '+91 84690 34869', 'Official Direct Phone Number', 'contact'),
('phone_digits', '918469034869', 'Raw digits phone number', 'contact'),
('whatsapp_number', '+91 84690 34869', 'WhatsApp Number Display', 'contact'),
('whatsapp_raw', '918469034869', 'WhatsApp Raw link number', 'contact'),
('official_email', 'info@rppharma.com', 'Official General Email', 'contact'),
('business_email', 'business@rppharma.com', 'Business Enquiries Email', 'contact'),
('export_email', 'export@rppharma.com', 'Export Department Email', 'contact'),
('working_hours', 'Monday – Saturday: 9:00 AM – 6:30 PM (IST)', 'Working Hours', 'contact'),
('stat_experience', '15+', 'Years Experience', 'metrics'),
('stat_countries', '25+', 'Countries Served', 'metrics'),
('stat_categories', '10+', 'Product Categories', 'metrics'),
('stat_manufacturing_partners', '10+', 'Partner Facilities', 'metrics'),
('stat_global_markets', '5', 'Global Regions', 'metrics')
ON DUPLICATE KEY UPDATE `value`=VALUES(`value`);

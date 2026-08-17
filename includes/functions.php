<?php
/**
 * RP PHARMA — Helper Functions & Data Providers
 */

require_once __DIR__ . '/db.php';

/**
 * Get Site Settings
 */
function get_site_settings(): array {
    $pdo = DB::getConnection();
    if ($pdo) {
        try {
            $stmt = $pdo->query("SELECT `key`, `value` FROM `site_settings`");
            $db_settings = [];
            while ($row = $stmt->fetch()) {
                $db_settings[$row['key']] = $row['value'];
            }
            if (!empty($db_settings)) {
                return $db_settings;
            }
        } catch (Exception $e) {}
    }
    return DB::getJsonData('settings.json');
}

/**
 * Get Categories
 */
function get_categories(?string $type = null): array {
    $pdo = DB::getConnection();
    if ($pdo) {
        try {
            if ($type) {
                $stmt = $pdo->prepare("SELECT * FROM `categories` WHERE `type` = ? AND `is_active` = 1 ORDER BY `display_order` ASC");
                $stmt->execute([$type]);
            } else {
                $stmt = $pdo->query("SELECT * FROM `categories` WHERE `is_active` = 1 ORDER BY `display_order` ASC");
            }
            $cats = $stmt->fetchAll();
            if (!empty($cats)) return $cats;
        } catch (Exception $e) {}
    }
    
    $cats = DB::getJsonData('categories.json');
    if ($type) {
        return array_values(array_filter($cats, fn($c) => ($c['type'] ?? '') === $type));
    }
    return $cats;
}

/**
 * Get Products with optional filters
 */
function get_products(array $filters = []): array {
    $pdo = DB::getConnection();
    if ($pdo) {
        try {
            $sql = "SELECT p.*, c.name as category_name, c.slug as category_slug FROM products p LEFT JOIN categories c ON p.category_id = c.id WHERE p.is_active = 1";
            $params = [];

            if (!empty($filters['type'])) {
                $sql .= " AND p.type = ?";
                $params[] = $filters['type'];
            }
            if (!empty($filters['category_slug'])) {
                $sql .= " AND c.slug = ?";
                $params[] = $filters['category_slug'];
            }
            if (!empty($filters['is_featured'])) {
                $sql .= " AND p.is_featured = 1";
            }

            $stmt = $pdo->prepare($sql);
            $stmt->execute($params);
            $prods = $stmt->fetchAll();
            if (!empty($prods)) return $prods;
        } catch (Exception $e) {}
    }

    $products = DB::getJsonData('products.json');
    
    return array_values(array_filter($products, function($p) use ($filters) {
        if (!empty($filters['type']) && ($p['type'] ?? '') !== $filters['type']) {
            return false;
        }
        if (!empty($filters['category_slug']) && ($p['category_slug'] ?? '') !== $filters['category_slug']) {
            return false;
        }
        if (!empty($filters['is_featured']) && empty($p['is_featured'])) {
            return false;
        }
        return true;
    }));
}

/**
 * Get Single Product by Slug
 */
function get_product_by_slug(string $slug): ?array {
    $pdo = DB::getConnection();
    if ($pdo) {
        try {
            $stmt = $pdo->prepare("SELECT p.*, c.name as category_name, c.slug as category_slug FROM products p LEFT JOIN categories c ON p.category_id = c.id WHERE p.slug = ? LIMIT 1");
            $stmt->execute([$slug]);
            $prod = $stmt->fetch();
            if ($prod) return $prod;
        } catch (Exception $e) {}
    }

    $products = DB::getJsonData('products.json');
    foreach ($products as $p) {
        if (($p['slug'] ?? '') === $slug) {
            return $p;
        }
    }
    return null;
}

/**
 * Get Featured Products
 */
function get_featured_products(?string $type = null, int $limit = 4): array {
    $products = get_products([
        'type' => $type,
        'is_featured' => true
    ]);
    return array_slice($products, 0, $limit);
}

/**
 * Sanitize User Input
 */
function sanitize_input(string $data): string {
    return htmlspecialchars(stripslashes(trim($data)), ENT_QUOTES, 'UTF-8');
}

/**
 * Save B2B Enquiry
 */
function save_enquiry(array $data): bool {
    $pdo = DB::getConnection();
    if ($pdo) {
        try {
            $stmt = $pdo->prepare("
                INSERT INTO `enquiries` 
                (`full_name`, `company_name`, `email`, `phone`, `country`, `enquiry_type`, `product_name`, `message`, `ip_address`)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ");
            return $stmt->execute([
                $data['full_name'] ?? '',
                $data['company_name'] ?? '',
                $data['email'] ?? '',
                $data['phone'] ?? '',
                $data['country'] ?? '',
                $data['enquiry_type'] ?? 'general',
                $data['product_name'] ?? '',
                $data['message'] ?? '',
                $_SERVER['REMOTE_ADDR'] ?? '127.0.0.1'
            ]);
        } catch (Exception $e) {}
    }

    // Save to inquiries JSON storage
    $enquiries = DB::getJsonData('enquiries.json');
    $data['id'] = count($enquiries) + 1;
    $data['ip_address'] = $_SERVER['REMOTE_ADDR'] ?? '127.0.0.1';
    $data['created_at'] = date('Y-m-d H:i:s');
    $enquiries[] = $data;
    return DB::saveJsonData('enquiries.json', $enquiries);
}

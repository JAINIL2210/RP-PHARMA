<?php
/**
 * RP PHARMA — Products JSON REST API
 */
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');

require_once __DIR__ . '/../includes/functions.php';

$type = isset($_GET['type']) ? trim($_GET['type']) : null;
$category = isset($_GET['category']) ? trim($_GET['category']) : null;
$search = isset($_GET['search']) ? strtolower(trim($_GET['search'])) : null;
$featured = isset($_GET['featured']) && $_GET['featured'] == '1';

$filters = [];
if ($type && in_array($type, ['pharmaceutical', 'nutraceutical'])) {
    $filters['type'] = $type;
}
if ($category) {
    $filters['category_slug'] = $category;
}
if ($featured) {
    $filters['is_featured'] = true;
}

$products = get_products($filters);

if ($search) {
    $products = array_values(array_filter($products, function($p) use ($search) {
        $name = strtolower($p['name'] ?? '');
        $comp = strtolower($p['composition'] ?? '');
        $ind = strtolower($p['indications'] ?? '');
        $dosage = strtolower($p['dosage_form'] ?? '');
        return str_contains($name, $search) || str_contains($comp, $search) || str_contains($ind, $search) || str_contains($dosage, $search);
    }));
}

echo json_encode([
    'status' => 'success',
    'count' => count($products),
    'data' => $products
], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);

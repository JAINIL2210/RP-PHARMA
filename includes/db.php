<?php
/**
 * RP PHARMA — Database & Data Layer
 * Connects to MySQL via PDO if configured, with automatic JSON fallback.
 */

// MySQL Database Credentials (Defaults for local development/cPanel)
define('DB_HOST', getenv('DB_HOST') ?: '127.0.0.1');
define('DB_NAME', getenv('DB_NAME') ?: 'rp_pharma');
define('DB_USER', getenv('DB_USER') ?: 'root');
define('DB_PASS', getenv('DB_PASS') ?: '');
define('DB_PORT', getenv('DB_PORT') ?: '3306');

class DB {
    private static ?PDO $pdo = null;
    private static bool $connected = false;

    /**
     * Get PDO MySQL Connection or return null if not configured
     */
    public static function getConnection(): ?PDO {
        if (self::$pdo === null && !self::$connected) {
            self::$connected = true;
            try {
                $dsn = "mysql:host=" . DB_HOST . ";port=" . DB_PORT . ";dbname=" . DB_NAME . ";charset=utf8mb4";
                self::$pdo = new PDO($dsn, DB_USER, DB_PASS, [
                    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                    PDO::ATTR_TIMEOUT => 2
                ]);
            } catch (Exception $e) {
                // MySQL not available; system will seamlessly use data/*.json
                self::$pdo = null;
            }
        }
        return self::$pdo;
    }

    /**
     * Helper to read JSON data file safely
     */
    public static function getJsonData(string $filename): array {
        $path = __DIR__ . '/../data/' . $filename;
        if (file_exists($path)) {
            $content = file_get_contents($path);
            $data = json_decode($content, true);
            return is_array($data) ? $data : [];
        }
        return [];
    }

    /**
     * Helper to write JSON data file safely
     */
    public static function saveJsonData(string $filename, array $data): bool {
        $path = __DIR__ . '/../data/' . $filename;
        return (bool) file_put_contents($path, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));
    }
}

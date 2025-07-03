<?php
require_once __DIR__ . '/ISSService.php';

class App {
    private $service;

    public function __construct() {
        $this->service = new ISSService();
    }

    public function run() {
        $uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
        if ($uri === '/') {
            $this->helloWorld();
        } elseif ($uri === '/iss') {
            $this->issEndpoint();
        } else {
            $this->notFound();
        }
    }

    private function helloWorld() {
        header('Content-Type: text/plain');
        echo 'Hello World';
        exit;
    }

    private function issEndpoint() {
        header('Content-Type: application/json');
        try {
            echo json_encode($this->service->getIssPositionWithCountry());
        } catch (Exception $e) {
            http_response_code(502);
            echo json_encode(['error' => 'Failed to fetch ISS position']);
        }
        exit;
    }

    private function notFound() {
        http_response_code(404);
        echo 'Not Found';
        exit;
    }
}

$app = new App();
$app->run(); 
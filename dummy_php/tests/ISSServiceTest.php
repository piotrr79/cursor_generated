<?php
use PHPUnit\Framework\TestCase;
use GuzzleHttp\Psr7\Response;
use GuzzleHttp\Handler\MockHandler;
use GuzzleHttp\HandlerStack;
use GuzzleHttp\Client;

require_once __DIR__ . '/../ISSService.php';

class ISSServiceTest extends TestCase {
    public function testGetIssPositionWithCountry() {
        // Mock ISS API response
        $issResponse = new Response(200, [], json_encode([
            'iss_position' => ['latitude' => '10.0', 'longitude' => '20.0'],
            'message' => 'success',
            'timestamp' => 1234567890
        ]));
        // Mock Nominatim response
        $countryResponse = new Response(200, [], json_encode([
            'address' => ['country' => 'Testland']
        ]));
        $mock = new MockHandler([$issResponse, $countryResponse]);
        $handlerStack = HandlerStack::create($mock);
        $client = new Client(['handler' => $handlerStack]);

        $service = new ISSServiceTestable($client);
        $result = $service->getIssPositionWithCountry();
        $this->assertEquals('10.0', $result['latitude']);
        $this->assertEquals('20.0', $result['longitude']);
        $this->assertEquals('Testland', $result['country']);
    }
}

class ISSServiceTestable extends ISSService {
    public function __construct($client) {
        $this->client = $client;
    }
} 
<?php
require_once __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;

class ISSService {
    private $issApiUrl = 'http://api.open-notify.org/iss-now.json';
    private $nominatimUrl = 'https://nominatim.openstreetmap.org/reverse';
    private $client;

    public function __construct() {
        $this->client = new Client([
            'timeout' => 5.0,
            'headers' => [
                'User-Agent' => 'iss-php-app'
            ]
        ]);
    }

    public function getIssPosition() {
        $response = $this->client->get($this->issApiUrl);
        $data = json_decode($response->getBody(), true);
        $lat = $data['iss_position']['latitude'];
        $lon = $data['iss_position']['longitude'];
        return [$lat, $lon];
    }

    public function getCountryFromLatLon($lat, $lon) {
        try {
            $response = $this->client->get($this->nominatimUrl, [
                'query' => [
                    'format' => 'json',
                    'lat' => $lat,
                    'lon' => $lon,
                    'zoom' => 5,
                    'addressdetails' => 1
                ]
            ]);
            $data = json_decode($response->getBody(), true);
            return $data['address']['country'] ?? 'Unknown';
        } catch (Exception $e) {
            return 'Unknown';
        }
    }

    public function getIssPositionWithCountry() {
        list($lat, $lon) = $this->getIssPosition();
        $country = $this->getCountryFromLatLon($lat, $lon);
        return [
            'latitude' => $lat,
            'longitude' => $lon,
            'country' => $country
        ];
    }
} 
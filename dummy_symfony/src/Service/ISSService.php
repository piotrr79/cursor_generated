<?php
namespace App\Service;

use Exception;

class ISSService
{
    private $issApiUrl = 'http://api.open-notify.org/iss-now.json';
    private $nominatimUrl = 'https://nominatim.openstreetmap.org/reverse';
    private $userAgent = 'iss-symfony-app';

    public function getIssPosition(): array
    {
        $response = file_get_contents($this->issApiUrl);
        if ($response === false) {
            throw new Exception('Failed to fetch ISS position');
        }
        $data = json_decode($response, true);
        $lat = $data['iss_position']['latitude'] ?? null;
        $lon = $data['iss_position']['longitude'] ?? null;
        if (!$lat || !$lon) {
            throw new Exception('Invalid ISS position data');
        }
        return [$lat, $lon];
    }

    public function getLocationInfo(string $lat, string $lon): array
    {
        $params = http_build_query([
            'format' => 'json',
            'lat' => $lat,
            'lon' => $lon,
            'zoom' => 10,
            'addressdetails' => 1
        ]);
        $opts = [
            'http' => [
                'header' => "User-Agent: {$this->userAgent}\r\n"
            ]
        ];
        $context = stream_context_create($opts);
        $url = $this->nominatimUrl . '?' . $params;
        $response = file_get_contents($url, false, $context);
        if ($response === false) {
            return ['type' => 'unknown', 'name' => 'Unknown'];
        }
        $data = json_decode($response, true);
        $address = $data['address'] ?? [];
        if (isset($address['country'])) {
            return ['type' => 'country', 'name' => $address['country']];
        }
        foreach (['sea', 'ocean', 'water', 'river', 'lake'] as $key) {
            if (isset($address[$key])) {
                return ['type' => 'sea', 'name' => $address[$key]];
            }
        }
        return ['type' => 'unknown', 'name' => 'Unknown'];
    }

    public function getIssPositionWithLocation(): array
    {
        list($lat, $lon) = $this->getIssPosition();
        $location = $this->getLocationInfo($lat, $lon);
        return [
            'latitude' => $lat,
            'longitude' => $lon,
            'location_type' => $location['type'],
            'location_name' => $location['name']
        ];
    }
} 
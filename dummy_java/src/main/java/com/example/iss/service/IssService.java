package com.example.iss.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.*;
import java.util.*;

@Service
public class IssService {

    private final String ISS_API_URL = "http://api.open-notify.org/iss-now.json";
    private final String NOMINATIM_URL = "https://nominatim.openstreetmap.org/reverse";

    public Map<String, String> getIssPositionWithCountry() {
        RestTemplate restTemplate = new RestTemplate();

        // Get ISS position
        Map<String, Object> issResponse = restTemplate.getForObject(ISS_API_URL, Map.class);
        Map<String, String> issPosition = (Map<String, String>) issResponse.get("iss_position");
        String lat = issPosition.get("latitude");
        String lon = issPosition.get("longitude");

        // Get country from lat/lon
        String country = getCountryFromLatLon(lat, lon);

        Map<String, String> result = new HashMap<>();
        result.put("latitude", lat);
        result.put("longitude", lon);
        result.put("country", country);
        return result;
    }

    public String getCountryFromLatLon(String lat, String lon) {
        RestTemplate restTemplate = new RestTemplate();
        String url = NOMINATIM_URL + "?format=json&lat=" + lat + "&lon=" + lon + "&zoom=5&addressdetails=1";
        HttpHeaders headers = new HttpHeaders();
        headers.set("User-Agent", "iss-java-app");
        HttpEntity<String> entity = new HttpEntity<>(headers);

        try {
            ResponseEntity<Map> response = restTemplate.exchange(url, HttpMethod.GET, entity, Map.class);
            Map<String, Object> body = response.getBody();
            Map<String, String> address = (Map<String, String>) body.get("address");
            return address != null ? address.getOrDefault("country", "Unknown") : "Unknown";
        } catch (Exception e) {
            return "Unknown";
        }
    }
} 
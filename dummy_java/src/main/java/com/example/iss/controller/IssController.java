package com.example.iss.controller;

import com.example.iss.service.IssService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
public class IssController {

    @Autowired
    private IssService issService;

    @GetMapping("/")
    public String helloWorld() {
        return "Hello World";
    }

    @GetMapping("/iss")
    public ResponseEntity<Map<String, String>> getIssPosition() {
        try {
            return ResponseEntity.ok(issService.getIssPositionWithCountry());
        } catch (Exception e) {
            return ResponseEntity.status(502).body(Map.of("error", "Failed to fetch ISS position"));
        }
    }
} 
package com.example.iss.service;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class IssServiceTest {
    @Test
    public void testGetCountryFromLatLon() {
        IssService service = new IssService();
        String country = service.getCountryFromLatLon("40.7128", "-74.0060"); // Should be USA or Unknown
        assertNotNull(country);
    }
} 
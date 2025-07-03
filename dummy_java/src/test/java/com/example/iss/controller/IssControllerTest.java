package com.example.iss.controller;

import com.example.iss.service.IssService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;

import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

import java.util.Map;

@WebMvcTest(IssController.class)
public class IssControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private IssService issService;

    @Test
    public void testHelloWorld() throws Exception {
        mockMvc.perform(get("/"))
                .andExpect(status().isOk())
                .andExpect(content().string("Hello World"));
    }

    @Test
    public void testGetIssPosition() throws Exception {
        when(issService.getIssPositionWithCountry()).thenReturn(
                Map.of("latitude", "10.0", "longitude", "20.0", "country", "Testland")
        );
        mockMvc.perform(get("/iss"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.latitude").value("10.0"))
                .andExpect(jsonPath("$.longitude").value("20.0"))
                .andExpect(jsonPath("$.country").value("Testland"));
    }
} 
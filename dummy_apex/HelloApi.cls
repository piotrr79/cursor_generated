@RestResource(urlMapping='/hello')
global with sharing class HelloApi {
    @HttpGet
    global static String doGet() {
        return 'Hello World';
    }
} 
@RestResource(urlMapping='/iss')
global with sharing class IssApi {
    @HttpGet
global static IssService.IssPosition doGet() {
        return IssService.getIssPositionWithCountry();
    }
} 
@isTest
private class IssServiceTest {
    @isTest static void testGetIssPositionWithCountry() {
        // Mock ISS API response
        Test.startTest();
        HttpCalloutMock mock = new ISSMock();
        Test.setMock(HttpCalloutMock.class, mock);
        IssService.IssPosition pos = IssService.getIssPositionWithCountry();
        System.assertNotEquals(null, pos.latitude);
        System.assertNotEquals(null, pos.longitude);
        System.assertEquals('Testland', pos.country);
        Test.stopTest();
    }

    private class ISSMock implements HttpCalloutMock {
        public HTTPResponse respond(HTTPRequest req) {
            HttpResponse res = new HttpResponse();
            if (req.getEndpoint().contains('open-notify')) {
                res.setStatusCode(200);
                res.setBody('{"iss_position": {"latitude": "10.0", "longitude": "20.0"}, "message": "success", "timestamp": 1234567890}');
            } else if (req.getEndpoint().contains('nominatim')) {
                res.setStatusCode(200);
                res.setBody('{"address": {"country": "Testland"}}');
            } else {
                res.setStatusCode(404);
                res.setBody('');
            }
            return res;
        }
    }
} 
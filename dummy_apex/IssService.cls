public with sharing class IssService {
    public class IssPosition {
        public String latitude;
        public String longitude;
        public String country;
    }

    public static IssPosition getIssPositionWithCountry() {
        IssPosition pos = new IssPosition();
        // Get ISS position
        Http http = new Http();
        HttpRequest req = new HttpRequest();
        req.setEndpoint('http://api.open-notify.org/iss-now.json');
        req.setMethod('GET');
        HttpResponse res = http.send(req);
        if (res.getStatusCode() == 200) {
            Map<String, Object> issData = (Map<String, Object>) JSON.deserializeUntyped(res.getBody());
            Map<String, Object> issPos = (Map<String, Object>) issData.get('iss_position');
            pos.latitude = String.valueOf(issPos.get('latitude'));
            pos.longitude = String.valueOf(issPos.get('longitude'));
            pos.country = getCountryFromLatLon(pos.latitude, pos.longitude);
        } else {
            pos.latitude = null;
            pos.longitude = null;
            pos.country = 'Unknown';
        }
        return pos;
    }

    public static String getCountryFromLatLon(String lat, String lon) {
        Http http = new Http();
        HttpRequest req = new HttpRequest();
        req.setEndpoint('https://nominatim.openstreetmap.org/reverse?format=json&lat=' + lat + '&lon=' + lon + '&zoom=5&addressdetails=1');
        req.setMethod('GET');
        req.setHeader('User-Agent', 'iss-apex-app');
        HttpResponse res = http.send(req);
        if (res.getStatusCode() == 200) {
            Map<String, Object> data = (Map<String, Object>) JSON.deserializeUntyped(res.getBody());
            Map<String, Object> address = (Map<String, Object>) data.get('address');
            if (address != null && address.containsKey('country')) {
                return String.valueOf(address.get('country'));
            }
        }
        return 'Unknown';
    }
} 
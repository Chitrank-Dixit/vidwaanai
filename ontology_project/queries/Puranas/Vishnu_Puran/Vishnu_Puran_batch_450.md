# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vishnu Puran 0.8981)
- **Original**: 87 चसूदेवजीकी जो रोहिणी नामको दूसरी भार्या रहती है डसके उदरमें उस सातवें गर्भक्कों के जाकर तू इस प्रकार स्थापित कर देना जिससे वह उसीके जटरसे उत्पन्न हुएके समान जान पड़े
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8982)
- **Original**: उसके विषयमें संसार यहो भवसे देवकीका सातयाँ गर्थ गिर गया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8983)
- **Original**: वह श्वेत चौलशिखरके समान वीर पुरुष गर्भसे आकर्षण किये जानेके कारण संसारमें 'संकर्षण' नामसे प्रसिद्ध होगा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8984)
- **Original**: तदनन्तर, हे झुधे ! देवफोके आठवें गर्भमें मैं स्थित डोऊँगा। उस समय तू भी तुरैत ही यशोदाके गर्भमें चली जाना
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8985)
- **Original**: वर्षाक्रतुमें भादपद कृष्ण आश्मीको रात्रिके समय मैं जन्म रूँगा और तू नवमोको उत्पन्न होगी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8986)
- **Original**: है अनिन्दिते ! उस समय मेरी डाक्तिसे अपनी मति फिर जानेके कारण बसुदेवजी मुझे तो यज्ञोदाके और तुझे देवकोफे शयनगुहमें ले आयेंगे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8987)
- **Original**: तब हे देवि ! कंस तुझे फ्कड़ुकर पर्वत-शिलांपर पटक देंगा; उसके पटकते ही तू आकाशमें स्थित हो जायगी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8988)
- **Original**: उस समय मेरे गौरवसे सहस्ननयन इन्द्र सिर झुकाकर प्रणाय करनेके आउत्तर तुझे भगिनीरूपसे स्वीकार बत्रेगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8989)
- **Original**: तू भी शुम्भ, निशुम्भ आदि सहस्नों दैत्यॉँक्त्रीे मारकर अपने अनेक स्थानॉसे समस्त प्थित्रीको सुशोभित करेगी
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8990)
- **Original**: तू हो भूति, सन्नति, क्षान्ति और ऋान्ति है; तू हों आक्राश, पृथिनी, धृति, लूज्जा, पुष्टि और डपा है; इनके अतिरिक्त सेसारमें और भी जो कोई शक्ति है जह सब तू ही है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8991)
- **Original**: जो लोग प्रातःक्‍्क्छः और सायकाल्में अत्यत्त नप्रतापूर्वक तुझे आर्या, दुर्गा, वेदगर्भा, अम्बिका, भद्ठा, भद्गकाली, क्षेमदा और भाग्यदा आदि कहकर तेरी स्तुति करेंगे, उनकी समस्त कामनाएँ मेरी कृपासे पूर्ण हो जादँगी
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8992)
- **Original**: मदिय और मांसकी भेंट चढ़ानेसे तथा भक्ष्य और भोज्य पदार्थोद्टारा पूजा करनेसे प्रसन्न होकर तू मनष्योंकी सम्पूर्ण कापनाओंक् पूर्ण कर देगी
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8993)
- **Original**: हरे द्वारा दी हुई वे समस्त कामनाएँ मेरी ऊपासे निस्सन्‍दे पूर्ण होंगी । हे देवि ! अब तू मेरे बतलाये हुए स्थानकों जा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8994)
- **Original**: कम औ इतति श्रीविष्णुपुराणे पश्षमेंडशे प्रथमो ःध्यायः 9
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8995)
- **Original**: 314 श्रीविष्णुपुराण [ अब 2 दूसरा अध्याय भगवानका गर्भ-प्रवेश तथा देवगणद्वारा देवकीकी स्तुति श्रीपराशर उवाच अ्रीपराहरजी ओल्डे--हे मैत्रेय ! देवेदेव यथोक्ते सा जगद्धात्री देवदेवेन वै तथा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8996)
- **Original**: श्रीविष्णुभगवानतने जैसा कहा था उसके अनुसार जगद्धात्री बड्गर्भगर्भविन्यासं चक्रे चान्यस्य कर्षणम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8997)
- **Original**: योगमायाने छः गर्भाको देववीके उदरमें स्थित किया और सप्तमे रोहिणी गर्े प्राप्ते गर्भ ततो हरि: । सातवेंको उसमेंसे निकाल लिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8998)
- **Original**: इस प्रकार सातवें ल्त्रेकत्रयोपकाराय देवक्या: प्रविवेश ह
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8999)
- **Original**: 2 गर्भ! रेट्यीके: सदर: पहैच' जमेपर!औदरिग ही हैं लोकॉका उद्धार करनेकी इच्छासे देवकीके गर्भमें प्रवेश योगनिद्रा यशोदायास्तस्मिन्नेव तथा दिने। किया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9000)
- **Original**: भगवान्‌ परमेश्रस्के आज्ञानुसार योगमाया सम्भूता जठरे तद्दद्यथोक्ते परमेप्ठिला
- **Translation**: 

---


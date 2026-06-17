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

### Verse 1 (Vaivtpuran 543.15694)
- **Original**: हितकारी भगवान्‌ साध्य नहीं होते। जो ब्रह्मा अन्यथा यदि तुम असमर्थ हो तो अपने रास्ते
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15695)
- **Original**: वेदोंके उत्पादक, विधाता, फलदाता और सम्पूर्ण जाओ। तुम्हें यह सब पूछनेसे कया लाभ?
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15696)
- **Original**: सम्पत्तियोंके दाता हैं; बे प्रत्येक जन्ममें उन धर्मने कहा--वृन्दे ! जो इच्छारहित, तर्कणा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15697)
- **Original**: ब्रह्मस्वरूप अविनाशी सनातनदेवका सदा अपने करनेके अयोग्य, ऐश्वर्यशाली, निर्गुण, निराकार
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15698)
- **Original**: चारों मुखोंद्वारा स्तवन करते रहते हैं; परंतु और भक्तानुग्रहमूर्ति हैं; उन परमात्माकों पति
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15699)
- **Original**: बेदोंद्वारा अनिर्ववनीय, कालके काल तथा अन्तकके बनानेके लिये लक्ष्मी और सरस्वतीके अतिरिक्त
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15700)
- **Original**: अन्तक उन भगवान्‌कों सिद्ध नहीं कर पाते। दूसरी कौन स्त्री समर्थ हो सकती है ? वैकुण्ठशायी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15701)
- **Original**: वृन्दे! जो अपनी कलासे रुद्ररूप धारण चतुर्भुज भगवान्‌की ये ही दो भार्याएँ हैं। गोलोकमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15702)
- **Original**: करके जगत्‌का संहार करते हैं, पाँचों मुखोंसे भी जो द्विभुज, वंशी बजानेवाले, किशोर गोप-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15703)
- **Original**: उनकी स्तुति करते हैं, जिनसे बढ़कर भगवान्‌को वेषधारी, परिपूर्णतम श्रीकृष्ण हैं; उनकी पत्नी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15704)
- **Original**: दूसरा कोई प्रिय नहीं है; उनके द्वार जब भगवान्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15705)
- **Original**: न्‍] श्रीकृष्णजन्मखण्ड ] 685 ऋऋऋऋऋऊऋऋऋऋ%$%कऋ%ऊऋऊऋऋ%ऋऋ%ऋछऊऋऋकऋऊकऋऊ$%ऋऋ%#%ऊऋ$%ऋ%ऋऊऋऊऋऊऋऊऋ%ऋकऋकऋऋऊऋछऋऊऋऊऋऋऋऋऋकऊऋऋ%ऊऋऋऋऋऋऋऋ%ऋछऊऋऋकऊऋऋ%%%$5%$$भफ$ साध्य नहीं होते, तब दूसरेकी कया बात है?
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15706)
- **Original**: परे हैं, अपना पति बनाना चाहती हो, परंतु वे यून्दे! जो सर्वशक्तिस्वरूपा, दुर्गतिनाशिनी, परमन्रह्म-
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15707)
- **Original**: गोलोकमें केवल राधिकाद्वारा साध्य हैं; दूसरा स्वरूपिणी, ईश्वरी, मूलप्रकृति, नारायणी, विष्णुमाया,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15708)
- **Original**: कोई कभी भी उन्हें सिद्ध नहीं कर सकता। इतना वैष्णी और सनातनी हैं, जिनकी मायासे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15709)
- **Original**: कहकर छद्यावेषधारी धर्मने उसकी परीक्षाके लिये भ्रमणशील जगत्‌ सदा चक्कर काटता रहता है,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15710)
- **Original**: प्रचुर भोगसुखका प्रलोभन दिया और अपनेको ये दुर्गा भी जिन देवकी भक्तिपूर्वक रात-दिन
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15711)
- **Original**: ही पतिरूपमें स्वीकार करनेका अनुरोध किया। स्तुति करती रहती हैं। गजानन गणेश और छ:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15712)
- **Original**: फिर धर्म उसकी ओर बढ़े। ब्रजेश ! उनका विचार मुखबाले स्वामीकार्तिक भी भक्तिसहित यथाशक्ति
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15713)
- **Original**: केबल उसके सतीत्वको जानना था। उनकी यह जिनका स्तवन करते हैं। जिनकी सर्वप्रथम पूजा
- **Translation**: 

---


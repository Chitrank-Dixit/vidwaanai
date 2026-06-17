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

### Verse 1 (Vishnu Puran 0.281)
- **Original**: 57 बलणता सुष्टिकेनेत चाण्रेण तथा सरित । क्रीडतो खलभद्रस्य हरेहास्पं तिलोक्यताम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.282)
- **Original**: 58 सख्य: पश्यत चाणूरं नियुद्धार्थमयं हरि: । समुपैत्ति न सन्त्यत्र कि बृद्धा पुक्तकारिण:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.283)
- **Original**: 59 क् यौजनोन्मुखीभूतसुकुमारतनुहरि: । क्र क्‍ज्र॒कठिनाभोगशरीरोउयं॑ महासुर:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.284)
- **Original**: 60 इमो. सुललितैरहैयतेंते. नवयोवनो । द्ैतेयमल्लाओआरणूरप्रमुखास्त्वतिदारणा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.285)
- **Original**: 61 नियुद्धप्राश्रिकानां तु महानेष व्यतिक्रम: । यदह्ालबलिनोर्युद्धं मध्यस्थैस्समुपेक्ष्यते
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.286)
- **Original**: 62 औपराजर उदाय इत्थे पुरस्ील्लेकस्य वदतश्चालयन्भुवम्‌ । ववबल्ग बद्धकक्ष्योउन्तर्जनस्य भगवान्हरि:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.287)
- **Original**: 63 खलभद्रो5पि चास्फोल्ा बतल्ग ललित तथा । पदे पदे तथा भूमिर्यन्न शीर्णा तदद्धुतम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.288)
- **Original**: 64 नियुद्धकुशलो दैत्यो बलभद्रेण मुष्टिकः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.289)
- **Original**: 65 सन्निपातावधूतैस्तु चाणूरेण सम॑ हरिः। अ्रक्षेपणर्मष्टिभिश्न कीलबज्जनिपातनै:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.290)
- **Original**: 66 अ्रीविष्णुपुराण [ अ0 20 कारण वसुदेवजी भी मानो आयी हुई जराकों छोड़कर फिरसे नत्रयूबक-से हो गये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.291)
- **Original**: राजाके अन्तःपुस्की स्लियाँ तथा नगर निवासिनी महिछलाएँ, भी उन्हें एकटक देखते-देखते उपराम न हुईं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.292)
- **Original**: [वे परस्पर कहने लूगीं---] “अरी सख्तियों ! अरुणनयनसे युक्त श्रीकृष्णचन्द्रका अति सुन्दर मुख तो देखो, जो कुबलयापौडके साथ युद्ध करनेके परिश्रमसे स्वेद ब्िन्दरपर्ण होकर हिस-कण-सिश्चित हारत्कालीन प्रफुल्ल कमछको लज्जित कर रहा है। अरी ! इसका दर्शन करके अपने नेत्रोंका होना सफल कर लो''
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.293)
- **Original**: [एक ख््री बोली -- ] “हे भाभिनि ! इस बालकका यह लक्ष्मी आदिका आश्रयभूत श्रीवत्साकयुक्त वक्षःस्थऊक तथा झब्रुऑंको पराजित करनेवाल्जी इसकी दोनों भुजाएँ तो देखो !'
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.294)
- **Original**: [दूसरी>--] 'अरी ! क्या तुम नील्प्म्थर धारण किये इन दुग्ध, चन्द्र अथवा कमलनालके समान सुभ्रवर्ण बत्य्देवजीक्ों आते हुए नहीं देखती हो ?'”
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.295)
- **Original**: [तीसरी0--- ] ' अरी सस्लियो ! [ अखाड़ेमें] चकर देकर घूमनेवाले चाणूर और मुष्टिकके साथ क्रीडा करते हुए बलभद्र तथा कृष्णका हँसना देख स्तर ।''
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.296)
- **Original**: चौथी*--] हाय ! सस्क्ियो ! देखों तो चाणूरसे लड़तेके लिये ये हरि आगे बढ़ रहे हैं; क्या इन्हें छुड़ानेवाले कोई भी बड़े-यूढ़े यहाँ लहीं हैं?”
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.297)
- **Original**: “कहाँ तो यौखनमें प्रवेश करनेवाले सुकुमार-दारीर इयाम और कहाँ वजग़के समान कठोर दशारीस्वात्र यह महान्‌ असुर !
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.298)
- **Original**: ये दोनों नवयुयक तो बड़े ही सुकुमार दरीरवाले [ किंतु इनके प्रतिपक्षी ] ये चाणूर आदि दैत्य मलल अत्यन्त दारुण हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.299)
- **Original**: मल्लयुद्धके परी क्षकगर्णोंका यह बहुत बड़ा अन्याय है जो ये मध्यस्थ होकर भी इन बालक और बलबान्‌ मल्ल्मेंके युद्धकी उपेक्षा कर रहे हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.300)
- **Original**: भ्रीपराशरजी बोले--नगरकी स्तियोंके इस प्रकार बार्तालाप करते समय भगवान्‌ कृष्णचन्द्र अपनी कमर कसकर उन समस्त दर्सककि बीचमें पृथिवीको कम्पायमान करते हुए रह्न्धूमिपें कूद पड़े
- **Translation**: 

---


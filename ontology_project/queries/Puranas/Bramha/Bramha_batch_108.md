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

### Verse 1 (Bramha 0.2141)
- **Original**: मरणे यानि दुःखानि यममार्गे यमालये। मया तान्यनुभूतानि नरके यातनास्तथा
- **Translation**: 

---

### Verse 2 (Bramha 0.2142)
- **Original**: कृमिकौटदुमाणां च हस्त्यश्रमृगपक्षिणाम्‌ । महिषोष्टगर्णां चैव तथान्येषां बनौकसाम्‌
- **Translation**: 

---

### Verse 3 (Bramha 0.2143)
- **Original**: द्विजातीयां च॒ सर्वेषां शुद्राणां चैव योनिषु । धनिनां क्षत्रियाणां च दरिद्राणां तपस्थिनाम्‌
- **Translation**: 

---

### Verse 4 (Bramha 0.2144)
- **Original**: नृषाणां नृषभृत्यानां तथान्येषां चर देहिनाम्‌। गृहेषु तेषामुत्पन्नों देव चाहं पुनः पुनः
- **Translation**: 

---

### Verse 5 (Bramha 0.2145)
- **Original**: गतो5स्मि दासतां नाथ भृत्यातां बहुशो नृणाम्‌ । दरिद्रत्व॑ चेश्वरत्व॑ स्वामित्व॑ च तथा गतः
- **Translation**: 

---

### Verse 6 (Bramha 0.2146)
- **Original**: 23-38)
- **Translation**: 

---

### Verse 7 (Bramha 0.2147)
- **Original**: * राजा इन्दझुप्तके द्वारा भगवान्‌ श्रीविष्णुकी स्तुति * 905 कौन आपकी पूजा न करेगा। भगवन्‌! ब्रह्मा
- **Translation**: 

---

### Verse 8 (Bramha 0.2148)
- **Original**: स्तुति करनेपर भगवान्‌ गरुड़ध्वजने प्रसन्‍न होकर आदि देवता भी आपको स्तुति करनेमें समर्थ
- **Translation**: 

---

### Verse 9 (Bramha 0.2149)
- **Original**: उनका सब मनोरथ पूर्ण किया। जो मनुष्य नहीं हैं, फिर मानव-बुद्धि लेकर मैं आपकी
- **Translation**: 

---

### Verse 10 (Bramha 0.2150)
- **Original**: भगवान्‌ जगन्नाथका पूजन करके प्रतिदिन इस स्तुति कैसे कर सकता हूँ। क्योंकि आप
- **Translation**: 

---

### Verse 11 (Bramha 0.2151)
- **Original**: स्तोत्रसे उनका स्तवन करता है, बह बुद्धिमान्‌ प्रकृतिसे परे परमेश्वर हैं। प्रभो! मैंने अज्ञानके
- **Translation**: 

---

### Verse 12 (Bramha 0.2152)
- **Original**: निश्चय ही मोक्ष प्राप्त कर लेता है। जो विद्वान्‌ भावसे आपकी स्तुति की है। यदि आपको
- **Translation**: 

---

### Verse 13 (Bramha 0.2153)
- **Original**: पुरुष तीनों संध्याओंके समय पतित्र हो इस श्रेष्ठ मुझपर दया हो तो मेरे इस अपराधको क्षमा
- **Translation**: 

---

### Verse 14 (Bramha 0.2154)
- **Original**: स्तोत्रका जप करता है, वह धर्म, अर्थ, काम और करें । हरे! साधु पुरुष अपराधीपर भी क्षमाभाव
- **Translation**: 

---

### Verse 15 (Bramha 0.2155)
- **Original**: मोक्ष पाता है। जो एकाग्रचित्त हो इसका पाठ या ही रखते हैं, अतः देवेधर! आप भक्तस्नेहके
- **Translation**: 

---

### Verse 16 (Bramha 0.2156)
- **Original**: श्रवण करता अथवा दूसरोंको सुनाता है, वह वशीभूत होकर मुझपर प्रसन्न होइये। देव! मैंने
- **Translation**: 

---

### Verse 17 (Bramha 0.2157)
- **Original**: पापरहित हो भगवान्‌ विष्णुके सनातन धाममें भक्तिभावित चित्तसे आपकी जो स्तुति की है,
- **Translation**: 

---

### Verse 18 (Bramha 0.2158)
- **Original**: जाता है। यह स्तोत्र परम प्रशंसनीय, पापोंको दूर वह साज्जोपाज़ सफल हो। वासुदेव! आपको ! करनेबाला, भोग एबं मोक्ष देनेवाला, कल्याणमय, नमस्कार है।* गोपनीय, अत्यन्त दुर्लभ तथा पवित्र है। इसे जिस ब्रह्माजी कहते हैं--राजा इन्द्रद्ुस्अके इस प्रकार
- **Translation**: 

---

### Verse 19 (Bramha 0.2159)
- **Original**: किसी मनुष्यको नहीं देना चाहिये। नास्तिक, * हतो मया हताश्चान्ये घ्रातितों ग्रातितास्तथा
- **Translation**: 

---

### Verse 20 (Bramha 0.2160)
- **Original**: दत्त ममान्यैरन्येभ्यो मया दत्तमनेकश:
- **Translation**: 

---


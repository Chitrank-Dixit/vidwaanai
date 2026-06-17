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

### Verse 1 (Vishnu Puran 0.7041)
- **Original**: राजा निभिके शापसे वसिष्ठजीका लिफ्षदेह मित्रावरुणके चीर्यमें प्रविष्ट हुआ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7042)
- **Original**: और उर्वशीके देखनेसे उसका वीर्य स्खलित होनेपर उसीसे उन्होंने दूसरा देह धारण किया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7043)
- **Original**: निमिका शरीर भो आति मनोहर गन्ध और तैल आदिसे सुरक्षित रहनेके कारण गला-सड़ा नहीं, बल्कि तत्काल मरे हुए देहके समान ही रहा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7044)
- **Original**: यज्ञ समाप्त होनेपर जब देलगण अपना भाग ग्रहण करनेके ह्ियि आये तो उससे ऋत्विग्गण बोले कि--- “गजमानको वर दीजिये”
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7045)
- **Original**: देवताओंद्वारा प्रेरणा किये जानेपर राजा निमिने उनसे कहा--
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7046)
- **Original**: “भगवन्‌ ! आपलोग सम्पूर्ण संसार-दुःखको दूर करनेवाले हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7047)
- **Original**: मेंरे विचारमें शरीर और आत्माके वियोग होनेमें जैसा दुःख होता है लैसा और कोई दुःख्व नहीं है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7048)
- **Original**: इसलिये मैं अब फिर शरीर गहण करना नहीं चाहता, समस्त स्त्रेगोंके नेत्रोंमें हो वास करना चाहता हूँ ।"
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7049)
- **Original**: आ*7 ] चतुर्थ अंक 7 भूतानां नेत्रेश्र॒बतारित:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7050)
- **Original**: ततो भूतान्यु- न्मेषनिमेषं चक्कु:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7051)
- **Original**: अपुत्नस्थ चर भूभुजः द्ारीरमराजकभीरवो मुनयो5रण्या ममन्धुः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7052)
- **Original**: तत्र च कुमारो जज्ञे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7053)
- **Original**: जननाज्जनकसंज्ञां चाबाप
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7054)
- **Original**: अभूष्विदेहोउस्प पितेति बैदेह:, मधनान्मिथिरिति
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7055)
- **Original**: तस्थोदावसु: पुन्नोौ5भवत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7056)
- **Original**: उदावसोर्नन्दिवर्द्नस्ततस्पुकेतु:.. तस्माद्देबरात- स्ततश्च॒ बृहदुक्थः: तस्य च महावीर्यस्तस्थापि सुधृति:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7057)
- **Original**: ततश्च धृष्टकेतुरजायत
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7058)
- **Original**: थृष्टकेतोहर्यश्वस्तस्य च मनुर्मनो: प्रतिकः, तस्मात्कृतरथस्तस्थ देवमीढ:, तस्य चर विबुधो विबुधस्य महाधृतिस्ततश्च कृतरातः, ततो महारोमा तस्य सुवर्णरोमा तत्पुत्रो हस्वरोमा हस्वरोम्णस्सीर- ध्वजो5भवत्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7059)
- **Original**: तस्य पुत्रार्थ यजनभुवं कृषत: सीरे सीता दुहिता समुत्पन्ना
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7060)
- **Original**: सीरथ्वजस्य ॒प्राता साद्भाश्याधिपति: कुश- ध्वजनामासीत्‌
- **Translation**: 

---


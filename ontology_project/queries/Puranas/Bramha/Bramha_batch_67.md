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

### Verse 1 (Bramha 0.1321)
- **Original**: . ब्रह्माजी कहते हैं--इस प्रकार बहुत दिनॉतक देखा, दैत्यों और दानबोंने मेरे पुत्रोंकों अपने
- **Translation**: 

---

### Verse 2 (Bramha 0.1322)
- **Original**: आराधना करनेपर भगवान्‌ सूर्यने दक्षकन्या अदितिको स्थानसे हटा दिया और सारी त्रिलोकी नष्टप्राय
- **Translation**: 

---

### Verse 3 (Bramha 0.1323)
- **Original**: अपने तेजोमय स्वरूपका प्रत्यक्ष दर्शन कराया। कर दी। तब उन्होंने भगवान्‌ सूर्यफी आराधनाके
- **Translation**: 

---

### Verse 4 (Bramha 0.1324)
- **Original**: अदिति बोलीं--जगत्‌्के आदि कारण भगवान्‌ लिये महान्‌ प्रयत्न किया। वे नियमित आहार
- **Translation**: 

---

### Verse 5 (Bramha 0.1325)
- **Original**: सूर्य! आप मुझपर प्रसन्न हों। गोपते! मैं आपको * नमस्तुभ्यं परं॑ सूक्ष्म सुपुण्य॑ बिश्नरतेडतुलम्‌ । धाम धामवठामीशं धामाधारं च शाश्रतम्‌
- **Translation**: 

---

### Verse 6 (Bramha 0.1326)
- **Original**: जगतामुपकाराय त्वामहू॑ स्तौमि_ गोपते। आददानस्थ यद्गूप॑ तीब्र॑ तस्मे नमास्यहम्‌
- **Translation**: 

---

### Verse 7 (Bramha 0.1327)
- **Original**: ग्रहौतुमष्टमासेत.. कालेनाप्युमय॑ रसम्‌
- **Translation**: 

---

### Verse 8 (Bramha 0.1328)
- **Original**: बिभ्रतस्तव यद्वूपमतितीब्रं नतास्मि सतत
- **Translation**: 

---

### Verse 9 (Bramha 0.1329)
- **Original**: समेतमग्रिसोमाभ्यां. नमस्तस्थ गुणात्मने। यद्टूपयृग्यजु:साप्रामैक्येन तपते त़ब
- **Translation**: 

---

### Verse 10 (Bramha 0.1330)
- **Original**: विश्रमेतत्त्रयोसंज्ञं नमस्तस्मै विभावसो
- **Translation**: 

---

### Verse 11 (Bramha 0.1331)
- **Original**: यत्ु॒ तस्मात्पर॑ रूपमोमित्युक्त्वाभिसंहितम्‌
- **Translation**: 

---

### Verse 12 (Bramha 0.1332)
- **Original**: अस्थूर्ल स्थूलपमलं नमस्तस्मैसनातन
- **Translation**: 

---

### Verse 13 (Bramha 0.1333)
- **Original**: (32। 12-16)
- **Translation**: 

---

### Verse 14 (Bramha 0.1334)
- **Original**: 66 * संक्षिप्त ब्रह्मपुराण * भलीभाँति देख नहीं पाती। दिवाकर! आप ऐसी
- **Translation**: 

---

### Verse 15 (Bramha 0.1335)
- **Original**: सिद्ध हो जानेके कारण तपस्थासे निवृत्त हो कृपा करें, जिससे मुझे आपके रूपका भलीभौँति
- **Translation**: 

---

### Verse 16 (Bramha 0.1336)
- **Original**: गयीं। तत्पश्चात्‌ वर्षके अन्तमें देवमाता अदितिकी दर्शन हो सके। भक्तोंपर दया करनेवाले प्रभो! मेरे
- **Translation**: 

---

### Verse 17 (Bramha 0.1337)
- **Original**: इच्छा पूर्ण करनेके लिये भगवान्‌ सविताने पुत्र आपके भक्त हैं। आप उनपर कृपा करें।
- **Translation**: 

---

### Verse 18 (Bramha 0.1338)
- **Original**: उनके गर्भमें निवास किया। उस समय देवी तब भगवान्‌ भास्करने अपने सामने पड़ी हुई
- **Translation**: 

---

### Verse 19 (Bramha 0.1339)
- **Original**: अदिति यह सोचकर कि मैं पविश्नतापूर्वक हो देवीको स्पष्ट दर्शन देकर कहा--'देवि! आपकी
- **Translation**: 

---

### Verse 20 (Bramha 0.1340)
- **Original**: इस दिव्य गर्भकों धारण करूँगी, एकाग्रचित्त जो इच्छा हो, उसके अनुसार मुझसे कोई एक वर
- **Translation**: 

---


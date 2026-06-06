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

### Verse 1 (Vaivtpuran 543.15894)
- **Original**: है तथा महासागरमें नावके डूब जानेपर एवं शस्त्रकों लेकर और विष्णु तथा महेश्वरी दुर्गाका
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15895)
- **Original**: दावाप्निके बीच घिर जानेपर भी उस मनुष्यकी ध्यान करके शीघ्र ही त्रिपुरपर प्रहार किया। मृत्यु नहीं होती। वैश्येन्द्र ! इस स्तोत्रके प्रभावसे उसकी चोट खाकर वह दैत्य भूतलपर गिर पड़ा।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15896)
- **Original**: मनुष्य डाकुओं, शत्रुओं तथा हिंसक जन्तुओंसे उस समय देवताओंने शंकरका स्तवन किया और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15897)
- **Original**: घिर जानेपर भी कल्याणका भागी होता है। तात ! उनपर पुष्पोंकोी वर्षा कौ। दुर्गने उन्हें त्रिशुल, [यदि गोलोककी प्राप्तिके लिये आप नित्य इस विष्णुने पिनाक और ब्रह्माने शुभाशीर्वाद दिया।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15898)
- **Original**: स्तोत्रका पाठ करेंगे तो यहाँ ही आपको उन मुनिगण हर्षमग्र हो गये। सभी देवता हर्षविभोर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15899)
- **Original**: पार्वतीके साक्षात्‌ दर्शन होंगे। स्त्रीकूप चातिपुरुष॑ देवि त्व॑ च नपुंसकम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15900)
- **Original**: वृक्षाणां वृक्षरूपा त्व॑ सृष्टा चाकूररूपिणी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15901)
- **Original**: वहाँ च दाहिकाशक्तिजले शैत्यस्वरूपिणी । सूर्य तेज:स्वरूपा च प्रभारूपा च संततम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15902)
- **Original**: गन्धरूपा च भूमौ च आकाशे शब्दरूपिणी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15903)
- **Original**: शोभास्वरूपा चन्द्रे च पद्मसंधे च निश्चितम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15904)
- **Original**: सृष्टी सृष्टिस्वरूपा च॑ पालने परिपालिका
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15905)
- **Original**: महामारी च संहारे जले च जलरूपिणी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15906)
- **Original**: क्षुत्व॑ दया त्वं निद्रा त्वं तृष्णा त्वं बुद्धिरूपिणी । तुष्टिस्त्वं चापि पुष्टिस्त्वं श्रद्धा त्वं च क्षमा स्वयम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15907)
- **Original**: सान्तिस्त्व॑ च स्वयं भ्रान्ति; कान्तिस्त्य॑ कीर्तिरव च । लज्जा त्व॑च तथा माया भुक्तिमुक्तिस्वरूपिणी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15908)
- **Original**: सर्वशक्तिस्वरूपा ्त्बं सर्वसम्पत्पदायिनी । वेदेइनिर्वचनीया त्व॑ं त्वां न जानाति कश्चना
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15909)
- **Original**: सहस्रवकत्रस्त्वां स्तोतुं न च शक्त: सुरेश्वरि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15910)
- **Original**: वेदा न शक्ता; को विद्वानू न च शक्ता सरस्वतो
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15911)
- **Original**: स्वयं विधाता शछों न न च विष्णु: सनातन:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15912)
- **Original**: कि. स्तौमि पश्चवक्त्रेण रणत्रस्तो महेश्वारि
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15913)
- **Original**: कृपा कुरु महामाये मम शक्रुक्षय॑ कुरु । इत्युक्वा च सकरुणं रथस्थे पतिते रणे
- **Translation**: 

---


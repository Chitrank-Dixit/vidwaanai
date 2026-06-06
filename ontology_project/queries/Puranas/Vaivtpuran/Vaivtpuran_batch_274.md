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

### Verse 1 (Vaivtpuran 13.11622)
- **Original**: अत्यन्त सूक्ष्म-स्वरूपधारी होनेके कारण आप आया। उनके नेत्रॉमें भक्तिके आँसू भर आये और
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11623)
- **Original**: योगियोंके भी ध्यानमें नहीं आते हैं; ब्रह्मा, विष्णु उन्होंने सनातन पूर्णब्रह्मस्वरूप अपने उस पुत्रका और महेश भी आपकी वन्दना करते हैं; आप स्तवन किया। नित्य-स्वरूप परमात्माकों नमस्कार है। आप चार ननन्‍्द बोले--जो ब्राह्मणोंक हितकारी, गौओं
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11624)
- **Original**: युगोंमें चार वर्णोका आश्रय लेते हैं; इसलिये युग- तथा ब्राह्मणोंके हितैषी तथा समस्त संसारका भला
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11625)
- **Original**: क्रमसे शुक्ल, रक्त, पीत और श्याम नामक गुणसे * अक्षर परम॑ ब्रह्म ज्योतीरूप॑ सनातनम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11626)
- **Original**: गुणातीत॑ निराकार॑ स्वेच्छामयमनन्तकम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11627)
- **Original**: भक्तध्यानाय.. सेवाये तातारूपधरं॑ वरम्‌ । शुक्लरक्तपीतश्याम॑ युगानुक्रमणेन च
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11628)
- **Original**: शुक्लतेज:स्वरूप॑ च सत्ये सत्यस्वरूपिणम्‌ । त्रेतायां कुड्डुमाकार॑ ज्वलन्त॑.ब्रह्मतेजसा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11629)
- **Original**: ड्वापों पीतवर्ण च शोभित॑ पीतवाससा । कृष्णवर्ण॑ कलौ कृष्ण परिपूर्णत्म॑ प्रभुम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11630)
- **Original**: नवधाराधरोत्कृष्टश्यामसुन्दरविग्रहम्‌ । नन्दैकनन्दन॑ बन्दे. यशोदानन्दनं॑ प्रभुम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11631)
- **Original**: गोपिकाचेतनहरं राधाप्राणाधिकं परम्‌ । विनोदमुरलीशब्द॑ कुर्वन्त॑ कौतुके+न च
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11632)
- **Original**: रूपेणाप्रतिमेनैव रत्रभूषणभूषितम्‌ । कन्दर्पकोटिसौन्दर्य. बिध्रन्त॑ शान्तमीश्चरम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11633)
- **Original**: क्रीडन्त राधया साध॑ वृन्दारण्ये च॑ कुत्रचित्‌ । कुत्रचित्निर्जने5रण्ये राधावक्ष:स्थलस्थितम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11634)
- **Original**: जलक्रीडां. प्रकुर्व-तं॑ राधया सह ॒ कुत्रचित्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11635)
- **Original**: राधिकाकबरीभारं कुर्वन्त॑ कुत्रचिद॒ यने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11636)
- **Original**: कुत्रचिद्राधिकापादे दत्तवन्‍्तमलक्तकम्‌ । राधाचर्वितताम्बूल॑ गृहन्तं कुत्रचिन्मुदा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11637)
- **Original**: पश्यन्त॑ कुत्नचिद्राधां. पश्यन्ती. वक्रच॒क्षुपा । दतवन्तं च राधायै कृत्वा मालां च कुत्रचित्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11638)
- **Original**: कुत्रचिद्राधधा सा्ध॑ गच्छन्त॑ गरासमण्डलम्‌ । राधादत्तां गले मालां धृतवन्त॑च कुत्रचित्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11639)
- **Original**: साथ॑ गोपालिकाभिश्व॒ विहरन्त॑ च कुत्रचित्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11640)
- **Original**: राधां गृहीत्वा गच्छन्तं विहाय तां च कुत्रचित्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11641)
- **Original**: विप्रपत्रीदत्तमन्त॑ भुक्तवत्त॑ च कुत्रचित्‌ । भुक्तवन्त॑ तालफल बालक: सह कुत्रचित्‌
- **Translation**: 

---


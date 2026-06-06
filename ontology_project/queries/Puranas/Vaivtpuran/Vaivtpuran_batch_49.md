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

### Verse 1 (Vaivtpuran 4.9027)
- **Original**: श्वेत चँबर, दर्पण तथा बहुमूल्य रत्रोंके सारतत्त्वसे चन्द्रमाओंकी प्रभाकों छीने लेते थे। पारिजातके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.9028)
- **Original**: बने हुए कलश उस चतुःशालाको विभूषित कर पुष्पोंकी मालाओंसे उनके सुरम्य केशपाश आवेष्टित
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.9029)
- **Original**: रहे थे। रेशमी सूतमें गुँथे हुए चन्दन-पल्लबोंकी थे। वे भाँति-भाँतिके सुन्दर आभूषणोंसे विभूषित
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.9030)
- **Original**: बन्दनवारसे विभूषित मणिमय स्तम्भ-समूह उसके थीं। पके ब्रिम्यफलके समान उनके लाल-लाल
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.9031)
- **Original**: प्राज़्णको रमणीय बना रहे थे। चन्दन, अगुरु, ओठ थे। मुखारविन्दोंपर मन्‍्द मुस्कानकी छटा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.9032)
- **Original**: कस्तूरी तथा कुंकुमके द्रबका वहाँ छिड़काव हुआ छा रही थी। पके अनारके दानोंकी भाँति
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.9033)
- **Original**: था। श्वेत धान्य, श्वेत पुष्प, मूँगा, फल, अक्षत, दन्तपंक्तियाँ उनकी शोभा बढ़ा रही थीं। मनोहर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.9034)
- **Original**: दूर्वादल और लाजा आदिके निर्मज्छन (निछावर)- चम्पाके समान गौरवर्णवाली उन गोपकिशोरियोंके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.9035)
- **Original**: से उसकी अपूर्व शोभा हो रही थी। फल, रत्न, कटिभाग अत्यन्त कृश थे। उनकी नासिकाओंमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.9036)
- **Original**: रत्रकलश, सिन्दूर, कुंकुम और पारिजातकी गजमुक्ताकी बुलाकें शोभा दे रही थीं। वे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.9037)
- **Original**: मालाओंसे उसको सजाया गया था। फूलोंकी नासिकाएँ पक्षिराज गरुड़की सुन्दर चोंचको शोभा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.9038)
- **Original**: सुगन्‍्धसे सुवासित वायु उस स्थानको सब ओरसे धारण करती थीं। उनका चित्त नित्य मुकुन्दके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.9039)
- **Original**: सौरभयुक्त बना रही थी। जो सर्वथा अनिर्वचनीय, चरणारबिन्दोंमें लगा था। ट्वारपर खड़े हुए
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.9040)
- **Original**: अनिरूपित और ब्रह्माण्डमात्रमें दुर्लभ द्रव्य एवं निमेषरहित देवताओंने उन सबको देखा। वह द्वार
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.9041)
- **Original**: वस्तुएँ थीं, उन्हींसे उस भव्य भवनको विभूषित श्रेष्ठ मणिरत्ञोंकी वेदिकाओंसे सुशोभित था।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.9042)
- **Original**: किया गया था। वहाँ अत्यन्त सुन्दर रज्रमयी शब्या इन्द्रनीलमणिके बहुत-से खम्भे उसकी शोभा बढ़ा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.9043)
- **Original**: बिछी थी, जिसपर महीन एवं कोमल वस्त्रोंका रहे थे। उनके बीच-बीचमें सिन्दूरी रंगकी लाल
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.9044)
- **Original**: बिछावन था। नारद! करोड़ों रत्रमय कलश तथा मणियाँ जड़ी थीं। उस द्वारकों पारिजात-पुष्पोंकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.9045)
- **Original**: रत्ननिर्मित पात्र वहाँ सजाकर रखे गये थे, जो मालाओंसे सजाया गया था। उन्हें छूकर बहनेवाली
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.9046)
- **Original**: बहुमूल्य होनेके साथ ही बहुत सुन्दर थे। उनसे वायु वहाँ सर्वत्र सुगन्‍्ध फैला रही थी। राधिकाके
- **Translation**: 

---


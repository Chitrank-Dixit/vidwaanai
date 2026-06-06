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

### Verse 1 (Vaivtpuran 22.6999)
- **Original**: जाऊँगी। जो सत्यहीन, धरोहर हड़प लेनेवाला, होते हैं। जो सबके कारण, ऐश्वर्यशाली, सर्वेश्वर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 22.7000)
- **Original**: झूठी गवाही देनेवाला, विश्वासघाती और कृतप्न और सनातन हैं, वे भगवान्‌ नारायण भी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 22.7001)
- **Original**: है, उसके गृह मैं नहीं जाऊँगी। जो चिन्ताग्रस्त, ब्रह्मशापसे भय मानते हैं। भयभीत, शत्रुके चंगुलमें फँसा हुआ, महान्‌ पापी, ब्रह्म! इसी बीच अड्विरा, प्रचेता, क्रतु,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 22.7002)
- **Original**: कर्जदार और अत्यन्त कृपण है--ऐसे पापियोंके भूगु, पुलह, पुलस्त्य, मरीचि, अत्रि, सनक,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 22.7003)
- **Original**: घर मैं नहीं जाऊँगी। जो दीक्षाहीन, शोकार्त, सनन्‍्दन, तीसरे सनातन, साक्षात्‌ नारायणस्वरूप
- **Translation**: 

---

### Verse 6 (Vaivtpuran 22.7004)
- **Original**: मन्दबुद्धि और सदा स्त्रीके वशमें रहनेवाला है भगवान्‌ सनत्कुमार, कपिल, आसुरि, बोढु,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 22.7005)
- **Original**: तथा जो कुलटा स्त्रीका पति अथवा पुत्र है, उसके पक्शिख, दुर्वासा, कश्यप, अगस्त्य, गौतम,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 22.7006)
- **Original**: घर मैं कभी नहीं जाकँगी। जो दुष्ट वचन कण्व, और्व, कात्यायन, कणाद, पाणिनि, मार्कण्डेय, बोलनेवाला और झगड़ालू है, जिसके घरमें लोमश और स्वयं भगवान्‌ वसिष्ठ-ये सभी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 22.7007)
- **Original**: निरन्तर कलह होता रहता है तथा जिसके घरमें ब्राह्मण हर्षपूर्ण-चित्तते वहाँ आये। वे सभी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 22.7008)
- **Original**: स्त्रीका स्वामित्व है-ऐसे लोगोंके घर .मैं नहीं ब्रह्मतेजसे प्रज्वलित हो रहे थे और उनके मुखोंपर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 22.7009)
- **Original**: जाऊँगी। जहाँ श्रीहरिकी पूजा और उनके गुणोंका
- **Translation**: 

---

### Verse 12 (Vaivtpuran 22.7010)
- **Original**: 340 + संक्षिप्त ख्क्तवैवर्तपुराण * 5555$555$5 55 555 55 55% 5 5 5 5 # 55 5 5 5 5 5 5 55 5 $ 5 5 455 $ 5 क 5 5 ऋ 5 5 5 5 $ 5 55 5 55 55555 8 5 £ कीर्तन नहीं होता तथा उनकी प्रशंसामें उत्सुकता
- **Translation**: 

---

### Verse 13 (Vaivtpuran 22.7011)
- **Original**: मैं नहीं जाऊँगी। जो अपने द्वारा अथवा पराये नहीं है, उसके घर मैं नहीं जाऊँगी। जो कन्या,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 22.7012)
- **Original**: द्वारा दी हुई ब्राह्मणकी और देवताकी वृत्तिका अन्न और वेदको बेचनेवाला, मनुष्यघाती और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 22.7013)
- **Original**: अपहरण करता है, वह ज्ञानशील ही क्‍यों न हिंसक है, उसका घर नरककुण्डके समान है;
- **Translation**: 

---

### Verse 16 (Vaivtpuran 22.7014)
- **Original**: हो, उसके घर मैं नहीं जाऊँगी। जो मूर्ख कर्म अतः: मैं उसके घर नहीं जाऊँगी। जो कृपणतावश
- **Translation**: 

---

### Verse 17 (Vaivtpuran 22.7015)
- **Original**: करके दक्षिणा नहीं देता, वह शठ पापी और माता, पिता, भार्या, गुरुपन्नी, गुरु, पुत्र, अनाथ
- **Translation**: 

---

### Verse 18 (Vaivtpuran 22.7016)
- **Original**: पुण्यहीन है; उसके घर मैं नहीं जाऊँगी। जो बहिन और आश्रयहीन बान्धवोंका पालन-पोषण
- **Translation**: 

---

### Verse 19 (Vaivtpuran 22.7017)
- **Original**: मन्त्रविद्या (झाड़-फूँक)-से जीविका चलानेवाला, नहीं करता; सदा धन-संग्रहमें ही लगा रहता
- **Translation**: 

---

### Verse 20 (Vaivtpuran 22.7018)
- **Original**: ग्रामयाजी (पुरोहित), वैद्य, रसोइया और देवल है; उसके नरक-कुण्ड-सदृश घरमें मैं नहीं
- **Translation**: 

---


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

### Verse 1 (Vaivtpuran 543.13534)
- **Original**: लोकमें यह व्यवहार है कि सब लोग सबको फैल रही थी। सतीके उस प्राणहीन शरीरको
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13535)
- **Original**: परस्पर समझाते-बुझाते हैं। शम्भो! महेश्वर! देखकर भगवान्‌ शिव विरहकी आगसे जलने [दुर्दिनमें दुःख, शोक और भयकी प्राप्ति होती है। लगे। बे मूर्तिमान्‌ तत्त्वमाशि होनेपर भी सतीके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13536)
- **Original**: जब दुर्दिन बीत जाता और सुदिन आ जाता है, वियोगमें कभी मूर्च्छि, कभी चेतन होते हुए
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13537)
- **Original**: तब उनकी प्राप्ति कैसे हो सकती है ? उस समय भाँति-भाँतिसे विलाप करने लगे। तदनन्तर उनके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13538)
- **Original**: तो हर्ष और ऐश्वर्यविषयक दर्पकी ही निरन्तर स्वर्णप्रतिम मृत देहकों वक्षपर धारण करके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13539)
- **Original**: वृद्धि होती है; परंतु विद्वान्‌ पुरुष इन सबको सप्तद्वीप, लोकालोक पर्वत तथा सप्तसिन्धुमें भ्रमण
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13540)
- **Original**: स्वप्रकी भाँति मिथ्या समझते हैं। महादेव! तुम करते हुए भारतमें शतश्रृज्ज-गिरिके पास जम्बूद्ीपमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13541)
- **Original**: ज्ञानकी उत्पत्तिके कारण तथा सनातन हो। ज्ञान निर्जन प्रदेशस्थ अक्षयवटके नीचे नदीतीरपर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13542)
- **Original**: प्राप्त करो--अपने स्वरूपका स्मरण करो। तुम्हारा पहुँचे। वहाँसे महायोगी शंकर विरहाकुलचित्त
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13543)
- **Original**: कल्याण हो, तुम सचेत होओ--होशमें आओ। होकर पूरे एक वर्षतक पृथ्वीपर परिभ्रमण करते
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13544)
- **Original**: निश्चय हो तुम्हें सतीकी प्राप्ति होगी। जैसे रहे। सती देवीके उस मृत देहके अद्भग-प्रत्यड्र
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13545)
- **Original**: शीतलता जलको, दाहिका शक्ति अग्निको, तेज जिस-जिस स्थानपर गिरे, वे स्थान कामनाप्रद
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13546)
- **Original**: सूर्यको तथा गन्ध पृथ्वोकों कभी नहीं छोड़ती सिद्धपीठ हो गये। तदनन्तर शंकरने सतीके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13547)
- **Original**: है; उसी तरह सती तुम्हें छोड़कर अलग नहीं अवशिष्ट अड्लोंका संस्कार किया। अस्थियोंकी (रह सकती है। माला गूँधकर उसे अपना कण्ठभूषण बना लिया सनातन ज्ञानानन्दस्वरूप ज्ञाननिधे शंकर! मैं और प्रतिदिन सतीका शरीर-भस्म अपने शरीरपर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13548)
- **Original**: जो कहता हूँ, उसे सुनो। तुम परात्पर परमेश्वर लगाने लगे। इसके बाद बे निश्वेष्ट-से होकर एक
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13549)
- **Original**: हो, परंतु शोकबश अपने-आपको भूल गये हो। बटमूलमें पड़ गये। तब लक्ष्मीपूजित भगवान्‌ प्रत्येक जगतूमें तथा जन्म-जन्ममें सुदिन और नारायण अपने पार्षदों, देवताओं और ऋषि-
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13550)
- **Original**: दुर्दिनका चक्र निरन्तर चला करता है। वे सुदिन मुनियोंके साथ वहाँ पधारकर श्रीशंकरको गोदमें और दुर्दिन ही समस्त प्राकृत प्राणियोंके लिये लेकर उन्हें समझाने लगे। सुख-दुःखकी प्राप्तिक मुख्य कारण होते हैं। श्रीभगवानने कहा--स्वात्माराम शिव! मेरी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13551)
- **Original**: सुखसे हर्ष, दर्प, शौर्य, प्रमाद, राग, ऐश्वर्यकी बात सुनो और उसपर ध्यान दो। वह हितकारक,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13552)
- **Original**: अभिलाषा और विद्वेष निरन्तर प्रकट होते रहते [63 ] सं0 ब्रा0 लै0 पुराण 20
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13553)
- **Original**: 588 * संक्षिप्त ग्रह्मवैवर्तपुराण * हैं। दुःख, शोक और उद्धेगसे सदा भयकी प्राप्ति
- **Translation**: 

---


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

### Verse 1 (Vaivtpuran 543.17354)
- **Original**: वक्ष:स्थलपर कस्तूरी-कुंकुमयुक्त चन्दनका अनुलेप रत्नमाला पहनायी। सती पद्मावतीने पद्माद्वारा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17355)
- **Original**: किया, उनकौ शिखामें चम्पाका सुन्दर पुष्प कमल-पुष्पोंसे समर्चित चरणकमलमें जल, दूब,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17356)
- **Original**: लगाया, हाथमें सहस्नदलयुक्त क्रीड़ा-कमल दिया पुष्प और चन्दनयुक्त अर्घ्य प्रदान किया। मालतीने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17357)
- **Original**: और उनके हाथसे मुरली छीनकर उसमें रत्लदर्पण श्रीहरिकी चूड़ाको मालतीकौ मालासे सुशोभित
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17358)
- **Original**: पकड़ा दिया तथा उनके आगे पारिजातका खिला किया। सती पार्वतीने चम्पाके पुष्पका पुटक
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17359)
- **Original**: हुआ रुचिर पुष्प रख दिया। तत्पश्चात्‌ जो समर्पित किया। पारिजाताने हर्षमग्र हो श्रीहरिको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17360)
- **Original**: शान्तमूर्ति, कमनीय और नायिकाके मनकों हर पारिजात-पुष्प, कपूरयुक्त ताम्बूल और सुवासित
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17361)
- **Original**: लेनेवाले हैं तथा मन्द-मन्द मुस्करा रहे थे; शोतल जल निबेदित किया। कदम्बमालाने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17362)
- **Original**: उन प्रियतम श्रीकृष्णसे राधा एकान्तमें मुस्कराती कदम्ब-पुष्पोंकी शुभ माला, प्रफुछ्लित क्रीड़ा-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17363)
- **Original**: हुई मधुर वचन बोलीं। कमल और अमूल्य रत्लदर्पण समर्पित किया। श्रीराधिकाने कहा--नाथ! जो स्वयं सुकोमला कमलाने पूर्वकालमें वरुणद्वारा दिये
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17364)
- **Original**: मड्अलोंका भण्डार, सम्पूर्ण मड्रलोंका कारण, हुए दोनों सुन्दर वस्त्रोंकों श्रीहरिके हाथमें हो
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17365)
- **Original**: मड्रलरूप तथा मड़लोंका प्रदाता है, उसके रख दिया। सुन्दरी वधूने साक्षात्‌ श्रीहरिकों
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17366)
- **Original**: विषयमें कुशल-मड्गलका प्रश्न करना तो निष्फल गोरोचनकी-सी आभावाले एवं मधुर मधुसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17367)
- **Original**: ही है; तथापि इस समय कुशल पूछना परिपूर्ण मधुपात्र दिया। सुधामुखीने भक्तिपूर्वक
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17368)
- **Original**: समयानुसार उचित है; क्योंकि लौकिक व्यवहार अमृतसे लबालब भरा हुआ अमृतपात्र प्रदान
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17369)
- **Original**: वेदोंसे भी बली माना जाता है। इसलिये किया। किसी दूसरी गोपीने प्रफुल्लित मालती-
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17370)
- **Original**: रुक्मिणीकान्त ! सत्यभामाके प्राणपति! इस समय
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17371)
- **Original**: 768 रत] संक्षिप्त ब्रह्मवैवर्तपुराण ] &4&###88 ## #8# 6 86 # 8 # 468 6 & 4 ; 4 44 5 44 # # 5 $ $ 4 4 #% $ $ 4 4 4 4 5 4 4 4 % 4 5 4 % % 4 % 8 5 # क 5 5 4 5 % 5 5 4 % 4 $ 45 कुशल तो है न? तद्मन्तर श्रीराधाने भगवान्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17372)
- **Original**: मैं ही सदा द्वारकामें रुक्मिणीका स्वामी होता श्रीकृष्णससे उनके स्वरूप तथा अवतार-लीलाके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17373)
- **Original**: हूँ, क्षीरसागरमें शयन करनेवाला मैं ही सम्बन्धमें प्रश्न किया। सत्यभामाके शुभ भवनमें वास करता हूँ तथा तब श्रीकृष्ण बोले--राधे! जिसे सुनकर
- **Translation**: 

---


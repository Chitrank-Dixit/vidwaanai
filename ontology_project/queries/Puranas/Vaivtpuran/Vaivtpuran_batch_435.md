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

### Verse 1 (Vaivtpuran 23.1662)
- **Original**: नैवेद्यमात्रका भक्षण करता है, उसे अन्न खानेका ग्रहण करता है। ब्रह्मन्‌! जिनकी जैसी इच्छा होती
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1663)
- **Original**: पाप नहीं लगता। वह उपवासका पूरा फल प्राप्त है, वे उसीके अनुसार आहार करते हैं; क्योंकि
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1664)
- **Original**: कर लेता है।* रुचियोंका स्वरूप भिन्न-भिन्न प्रकारका होता है। नारद! गृहस्थ, शैव, शाक्त, विशेषत: वैष्णव गृहस्थ ब्राह्मणोंके लिये हविष्यात्र-भओोजन सदा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1665)
- **Original**: यति तथा ब्रह्मचारियोंके लिये यह बात बतायी उत्तम माना गया है। भगवान्‌ नारायणका उच्छिष्ट
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1666)
- **Original**: गयी है। जो बैष्णब पुरुष नित्य भगवान्‌ प्रसाद ही उनके लिये अभीष्ट भोजन है। जो
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1667)
- **Original**: श्रीकृष्णके नैवेद्य (प्रसाद)-का भोजन करता है, भगवानको निवेदित नहीं हुआ है, वह अभक्षणीय
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1668)
- **Original**: बह जीबन्मुक्त हो प्रतिदिन सौ उपबास-ब्रतोंका है। जो भगवान्‌ विष्णुको अर्पित नहीं किया
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1669)
- **Original**: फल पाता है। सम्पूर्ण देवता और तीर्थ उसके गया, बह अन्न बिष्ठा और जल मूत्रके समान
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1670)
- **Original**: अज्ञोंका स्पर्श चाहते हैं। उसके साथ वार्तालाप है। एकादशीके दिन सब प्रकारका अन्न-जल
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1671)
- **Original**: तथा उसका दर्शन समस्त पापोंका नाश करनेवाला मल-मूत्रके तुल्य कहा गया है। जो ब्राह्मण
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1672)
- **Original**: है। यतियों, विधवाओं और ब्रह्मचारियोंके लिये एकादशीके दिन स्वेच्छासे अन्न खाता है, वह
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1673)
- **Original**: ताम्बूल-भक्षण निषिद्ध है। * उपवासासमर्थश्व 'फलपूलजलं पिबेत्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1674)
- **Original**: नष्ट शरीरे स॒ भवेदन्यथा चात्मघातक:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1675)
- **Original**: सकृद्‌ भुंक्े हृविष्यात्र॑ किष्णो्नवेद्याव च । न भवेत्‌ प्रत्यवायों स चोपवासफलं लभेतू
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1676)
- **Original**: 4%######## 85 66 ## 5 4 # नारद! समस्त ब्राह्मणोंके लिये जो अभक्ष्य
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1677)
- **Original**: खाया जाय तो उससे बुद्धिका नाश होता है। है, उसका वर्णन सुनो। ताँबेके पात्रमें दूध पीना, नवमीको लौको और दशमीकों कलम्बीका शाक जूठे बर्तन या अन्नमें घी लेकर खाना तथा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1678)
- **Original**: सर्वथा त्याज्य है। एकादशीकों शिम्बी (सेम), नमकके साथ दूध पीना तत्काल गोमांस-भक्षणके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1679)
- **Original**: द्वादशीकों पृतिका (पोई) और त्रयोदशीकों बैगन समान माना गया है। काँसके बर्तनमें रखा हुआ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1680)
- **Original**: खानेसे पुत्रका नाश होता है। मांस सबके लिये एवं जो द्विज उठकर बायें हाथसे जल पीता सदा वर्जित है। है, वह शराबी माना गया है और समस्त धर्मोसे पार्वणश्राद्ध और ब्रतके दिन प्रातःकालिक बहिष्कृत है। मुने! भगवान्‌ श्रीहरिको निवेदित
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1681)
- **Original**: स्नानके समय सरसोंका तेल और पकाया हुआ न किया गया अन्न, खानेसे बचा हुआ जूठा
- **Translation**: 

---


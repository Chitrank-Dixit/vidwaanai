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

### Verse 1 (Vaivtpuran 115.634)
- **Original**: हीन ब्राह्मण ब्राह्मणाभासमात्र है। वैष्णव पुरुष उनके नैबेद्यको मुखमें ग्रहण करता है, वह इस
- **Translation**: 

---

### Verse 2 (Vaivtpuran 115.635)
- **Original**: अपने कुलकी करोड़ों और नाना आदिकी सैकड़ों भूतलपर परम पवित्र एवं जीवन्मुक्त है। कुलीन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 115.636)
- **Original**: पीढ़ियोंक साथ भगवान्‌ विष्णुके धाममें जाता है। ट्विजोंका जो अन्न-जल भगवान्‌ बिष्णुको अर्पित
- **Translation**: 

---

### Verse 4 (Vaivtpuran 115.637)
- **Original**: बैष्णबजन सदा गोविन्दके चरणारविन्दोंका ध्यान नहीं किया गया, वह मल-मूत्रके समान है--ऐसा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 115.638)
- **Original**: करते हैं और भगवान्‌ गोविन्द सदा उन बैष्णबोंके ब्रह्माजीका कथन है। ब्रह्माजी तथा उनके पुत्र निकट रहकर उन्हींका ध्यान किया करते हैं। सनकादि--सभी बिष्णुपरायण हैं; फिर उन्हींके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 115.639)
- **Original**: भक्तोंकी रक्षाके लिये सुदर्शनचक्रकों नियुक्त करके कुलमें उत्पन्न हुआ ब्राह्मण श्रीहरिसे विमुख कैसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 115.640)
- **Original**: भी श्रीहरि निश्चिन्त नहीं होते हैं; इसलिये स्वयं भी हो सकता है? माता-पिता, नाना आदि अथवा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 115.641)
- **Original**: उनके पास मौजूद रहते हैं। (अध्याय 11) #अल्‍पज00 क्र की0520020000 ब्रह्माजीकी अपूज्यताका कारण, गन्धर्वराजकी तपस्यासे संतुष्ट हुए भ्रगवान्‌ शंकरका उन्हें अभीष्ट वर देना तथा नारदजीका उनके पुत्ररूपसे उत्पन्न हो उपबईण नामसे प्रसिद्ध होना तदनन्तर शौनकजीके पृछनेपर सौतिने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 115.642)
- **Original**: छोड़कर अन्य सभी ब्रह्मकुमार, जिनको संख्या कहा--ब्रह्मन्‌! हंस, यति, अरणि, वोढु, पम्नशिख,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 115.643)
- **Original**: बहुत अधिक थी, सदा सांसारिक कार्योमें संलग्न अपान्तरतमा तथा सनक आदि-इन सबको
- **Translation**: 

---

### Verse 11 (Vaivtpuran 115.644)
- **Original**: हो प्रजाकी सृष्टि करके गुरुजनों (पिता आदि)- *स किं गुरु स कि तात: स किं पुत्र: स कि सखा। स कि राजा स किं बन्धुर्न दह्याद्‌ यो हरी मतिम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 115.645)
- **Original**: अनैष्णयाद्‌ द्विजादू विप्र चण्डालो वैष्णवों नरः।सगण: श्रपयों मुक्तो ब्राह्मणो नरक॑ गब्रजेतू
- **Translation**: 

---

### Verse 13 (Vaivtpuran 115.646)
- **Original**: ( ब्रह्मखण्ड 115। 38-39) ै ध्यायन्ते वैष्णवा: शश्वत्‌ गोविन्दपदपड्धूजम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 115.647)
- **Original**: ध्यायते तांध् गोविन्द: शश्वत्‌ तेषां च संनिधौ
- **Translation**: 

---

### Verse 15 (Vaivtpuran 115.648)
- **Original**: (ब्रह्मखण्ड 61
- **Translation**: 

---

### Verse 16 (Vaivtpuran 115.649)
- **Original**: की आज्ञाका पालन करने लगे। स्वर्य प्रजापति
- **Translation**: 

---

### Verse 17 (Vaivtpuran 115.650)
- **Original**: रहा था। सर्वज्ञ शिव सबके संहारक हैं। वे ही ब्रह्मा अपने पुत्र नारदके शापसे अपृण्य हो गये।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 115.651)
- **Original**: काल और मृत्युञ्य हैं। बे परमेश्वर ग्रीष्म-ऋतुकी इसीलिये विद्वान्‌ पुरुष ब्रह्माजीके मन्त्रकी उपासना
- **Translation**: 

---

### Verse 19 (Vaivtpuran 115.652)
- **Original**: दोपहरीके करोड़ों सूर्योके समान तेजस्वी थे। नहीं करते। नारदजी अपने पिताके शापसे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 115.653)
- **Original**: शान्तस्वरूप शिव तत्त्वज्ञान, मोक्ष तथा हरिभक्ति उपबर्हण नामक गन्धर्व हो गये। उनके वृत्तान्तका
- **Translation**: 

---


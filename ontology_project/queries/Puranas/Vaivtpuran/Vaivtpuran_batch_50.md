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

### Verse 1 (Vaivtpuran 4.9047)
- **Original**: उस चतु:ःशालाकी बड़ी शोभा हो रही थी। नाना उस परम आश्चर्यमय अन्त:पुरके द्वारका अवलोकन
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.9048)
- **Original**: प्रकारके वाद्योंकी मधुर ध्वनि वहाँ गूँज रही थी। करके देवताओंके मनमें श्रीकृष्ण-चरणारविन्दोंक
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.9049)
- **Original**: वीणा आदिके स्वर-यन्त्रोंक साथ गोपियॉोंका दर्शनकी उत्कण्ठा जाग उठी। उन्होंने'- उन
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.9050)
- **Original**: सुमधुर गीत सुनायी पड़ता था। मृदंग तथा सखियोंसे पूछकर शीघ्र ही द्वारके भीतर प्रवेश
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.9051)
- **Original**: अन्यान्य बाद्योंकी ध्वनिसे वह स्थान बड़ा मोहक किया। उनके शरीरमें रोमाश्ष हो आया था।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.9052)
- **Original**: जान पड़ता था। श्रीकृष्ण-तुल्य रूप, रंग और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.9053)
- **Original**: + भ्रीकृष्णजन्मखण्ड * 413 #6#####% 48 ## ## # 8 # # 5 $ 5 % 4 #% #% ऋ& > डक 48 ऋ कक हअ क#ड अऊ 5 अर 555 4548 8998 8988 # 5 9 % कक कक ऋकऊ_ बेश-भूषावाले गोपसमूहोंसे घिरे हुए उस अन्तः:-
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.9054)
- **Original**: उन्होंने शिवकों दाहिने और धर्मकों बायें कर पुरको झुंड-की-झुंड गोपाड्नाएँ, जो श्रीराधाकी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.9055)
- **Original**: लिया तथा वे भक्तिके उद्रेकसे चित्तको ध्यानमग्र सखियाँ थीं, सुशोभित कर रही थीं। श्रीराधा और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.9056)
- **Original**: करके उन परात्पर, गुणातीत, परमात्मा जगदीश्वर श्रीकृष्णके गुणगानसम्बन्धी पदोंका संगीत वहाँ
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.9057)
- **Original**: श्रीकृष्णकी स्तुति करने लगे। सब ओर सुनायी पड़ता था। ऐसे अन्तःपुरकों।.. ब्रह्माजी बोले--जो वर, वरेण्य, बरद, देखकर वे देवता विस्मयसे विमुग्ध हो उठे।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.9058)
- **Original**: बरदायकॉंके कारण तथा सम्पूर्ण प्राणियोंकी उन्होंने वहाँ मधुर गीत सुना और उत्तम नृत्य
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.9059)
- **Original**: उत्पत्तिके हेतु हैं; उन तेज:स्वरूप परमात्माको देखा। वे सब देवता वहाँ स्थिरभावसे खड़े
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.9060)
- **Original**: मैं नमस्कार करता हूँ। जो मड्गलकारी, मज्जलके हो गये। उन सबका चित्त ध्यानमें एकतान हो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.9061)
- **Original**: योग्य, मड्भलरूप, मड्रलदायक तथा समस्त रहा था। उन देवेश्वरोंको वहाँ रमणीय रज्नसिंहासन
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.9062)
- **Original**: मड्गलोंके आधार हैं; उन तेजोमय परमात्माको दिखायी दिया, जो सौ धनुषके बराबर विस्तृत
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.9063)
- **Original**: मैं प्रणाम करता हूँ। जो सर्वत्र विद्यमान, निर्लिप्त, था। बह सब ओरसे मण्डलाकार दिखायी देता
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.9064)
- **Original**: आत्मस्वरूप, परात्पर, निरीह और अवितर्कर्य हैं; था। श्रेष्ठ रत्रोंके बने हुए छोटे-छोटे कलश-
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.9065)
- **Original**: उन तेजःस्वरूप परमेश्वरकों नमस्कार है। जो समूह उसमें जुड़े हुए थे। विचित्र पुतलियों,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.9066)
- **Original**: सगुण, निर्गुण, सनातन, ब्रह्म, ज्योतिःस्वरूप, फूलों तथा चित्रमय काननोंसे उसकी बड़ी
- **Translation**: 

---


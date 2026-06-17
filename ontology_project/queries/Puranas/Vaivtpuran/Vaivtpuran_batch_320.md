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

### Verse 1 (Vaivtpuran 15.6753)
- **Original**: विवाह तथा गणेशका विवाह--यह सारा वृत्तान्त चरणकमलोंकी सेवा करती रहती थीं। नारद!
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.6754)
- **Original**: तुमसे वर्णन कर दिया। अब तुम्हारे मनमें कौन- इस प्रकार मैंने देवताओंका समागम, पार्वतीको
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.6755)
- **Original**: सी अभिलाषा है? फिर और क्या सुनना चाहते पुत्र-प्राप्ति, कुमारका अभिषेक, उनका पूजन और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.6756)
- **Original**: हो? (अध्याय 17) #3+>0+>>#गय+45,.....0> गणेशके शिरश्छेदनके वर्णनके प्रसड्में शंकरद्वारा सूर्यका मारा जाना, कश्यपका शिवको शाप देना, सूर्यका जीवित होना और माली-सुमालीकी रोगनिवृत्ति नारदने पूछा--महाभाग नारायण! तो
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.6757)
- **Original**: हो गया। तब ब्रह्माके पौत्र तपस्वी कश्यपजी, वेदबेदाज्रोंके पारगामी विद्वान्‌ हैं। परमेश्वर! मैं
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.6758)
- **Original**: जो ब्रह्मतेजसे प्रज्वलित हो रहे थे, अपने पुत्रको आपसे एक बहुत बड़े संदेहका समाधान जानना
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.6759)
- **Original**: प्रभाहीन देखकर शिवको शाप देते हुए बोले- चाहता हूँ। प्रभो! जो देवेश्वर महात्मा शंकरके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.6760)
- **Original**: “जिस प्रकार आज तुम्हारे त्रिशूलसे मेरे पुत्रका पुत्र तथा विध्लोके विनाशक हैं, उन गणेश्वरके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.6761)
- **Original**: वक्ष:स्थल विदीर्ण हो गया है, उसी तरह तुम्हारे लिये जो विप्न घटित हुआ, उसका क्‍या कारण
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.6762)
- **Original**: पुत्रका मस्तक कट जायगा।' शिवजी आशुतोष है? जब परिपूर्णतम परात्पर परमात्मा तो हैं ही; अत: क्षणमात्रमें ही उनका क्रोध जाता गोलोकनाथ स्वयं ही अपने अंशसे पार्वतीके पुत्र
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.6763)
- **Original**: रहा। तब उन्होंने उसी क्षण ब्रह्मज्ञानद्वारा सूर्यको होकर उत्पन्न हुए थे, तब उन ग्रहाधिराज भगवान्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.6764)
- **Original**: जीवित कर दिया। तदनन्तर जो ब्रह्मा, विष्णु और श्रीकृष्णके मस्तकका ग्रहकी दृष्टिसे कट जाना
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.6765)
- **Original**: महेशके अंशसे उत्पन्न हैं, वे त्रिगुणात्मक बड़े आश्चर्यकी बात है। आप इस वृत्तान्तको मुझे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.6766)
- **Original**: भक्तवत्सल सूर्य चेतना प्राप्त करके पिताके समक्ष बतलानेकी कृपा करें। खड़े हुए। फिर भक्तिपूर्वक पिताकों तथा शंकरको श्रीनारायणने कहा--ब्रह्मन्‌! विप्लेश्वरका
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.6767)
- **Original**: नमस्कार किया। साथ ही (पिताद्वारा दिये गये) यह विप्न जिस कारणसे हुआ था, उस प्राचीन
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.6768)
- **Original**: शम्भुके शापकों जानकर वे कश्यपजीपर क्ुद्ध इतिहासको तुम सावधान होकर श्रवण करो।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.6769)
- **Original**: हो गये, जिससे उन्होंने अपने विषयको ग्रहण नारद! एक समयकी बात है। भक्तवत्सल शंकरने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.6770)
- **Original**: नहों किया और क्रोधावेशमें यों कहा--'ईश्वरके माली और सुमालीको मारनेवाले सूर्यपर बड़े
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.6771)
- **Original**: बिना यह सब कुछ तुच्छ, अनित्य और नश्वर क्रोधके साथ त्रिशूलसे प्रहार किया। वह शिवके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.6772)
- **Original**: है, अत: विद्वान्‌को चाहिये कि वह मड्गलकारक समान तेजस्वी त्रिशूल अमोघ था। अत: उसकी
- **Translation**: 

---


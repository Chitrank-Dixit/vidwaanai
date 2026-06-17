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

### Verse 1 (Vaivtpuran 543.16114)
- **Original**: श्वेत चँचर डुलाती रहती है और तुम्हारे गोकुलको लौटेंगे। उस समय श्रीकृष्ण आकर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16115)
- **Original**: चरणकमलॉकी सेवा करती है। प्रसन्नताके साथ पुनः माताकों प्रणाम करेंगे और मुने! इतना कहकर तथा ब्रह्मा आदि रातमें हर्षपूर्वक इस पुण्यमय वृन्दावनमें पधारेंगे।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16116)
- **Original**: देवताओंद्वारा बन्दित उनके चरणकमलोंकों प्रणाम सती राधिके ! तुम शीघ्र ही श्रीकृष्णके मुखकमलका
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16117)
- **Original**: करके उद्धव चुप हो गये। उद्धवके मधुर दर्शन करोगी। उस समय तुम्हारा सारा विरह-
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16118)
- **Original**: वचनोंकों सुनते ही सती राधिकाके मुखपर दुःख दूर हो जायगा। अतः मातः! तुम अपने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16119)
- **Original**: मुस्कराहट छा गयी और उन्होंने उद्धबको अमूल्य चित्तको स्थिर करों और इस अत्यन्त दारुण दिव्य बस्त्राभूषण, रत्न, हार, भोजन, जल, शोकको त्याग दो। पुनः प्रसन्नतापूर्वक अग्रिमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16120)
- **Original**: ताम्बूल आदि देकर आशीर्वाद दिया। फिर, तपाकर शुद्ध किये हुए रमणीय वस्त्र पहनकर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16121)
- **Original**: श्रीकृष्णवर्णित ज्ञाकका उपदेश किया तथा लक्ष्मी, अमूल्य रत्नोंके बने हुए आभूषणोंकों धारण कर [विद्या, कीर्ति, सिद्धिके साथ ही श्रीहरिके दास्य, लो। कस्तूरी और कुंकुमसे युक्त चिकने चन्दनको
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16122)
- **Original**: श्रीहरिकि चरणोंमें निश्चला भक्ति और श्रेष्ठतम शरीरपर लगा लो और मालतीकी मालाओंसे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16123)
- **Original**: पार्षद-पदकी प्राप्तिका वरदान दिया। इस प्रकार
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16124)
- **Original**: * श्रीकृष्णजन्मखण्ड * 7033 कक $ 5585 £ # # $ 4 % # # 4 85 # # 95 5 5 ## 4 % 4 # $ 5 # $ 8 55 # $ 5# / 4 6 //# 5 5 # 5 # % 8 55 5 5 5 5 8 5 # ऊ हक 5 इक # 5 उद्धवको वर-प्रसाद प्रदान करके राधिकाजीने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16125)
- **Original**: जाओ। बेटा! विरह-तापसे कातर हुईं मुझको तुम उठकर अग्नि-शुद्ध साड़ी और कड्जुकी धारण की
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16126)
- **Original**: भूल न जाना। तुम निश्चय ही मेरे प्रियतमको तथा अमूल्य रत्नोंके आभूषण, होीरोंके हार,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16127)
- **Original**: भेजोगे, इसीसे मैं तुमसे कुछ कह रही हूँ; अन्यथा मनोहर रत्नमाला, सिन्दूर, कज्जल, पुष्पमाला और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16128)
- **Original**: स्त्रियोंक मनकी बात भला, कौन विद्वान्‌ जानता सुह्निग्ध चन्दनसे शरीरका श्रृज्रार किया। उस
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16129)
- **Original**: है? विद्वान्‌ तो शास्त्रानुसार कुछ-कुछ ही निरूपण समय उनके शरीरका रंग तपाये हुए सुवर्णके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16130)
- **Original**: कर सकता है। जब बेद उसका बर्णन करनेमें समान चमकीला था और कान्ति सैकड़ों चन्द्रमाओंके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16131)
- **Original**: समर्थ नहीं हैं तब शास्त्र बेचारे क्या कह सकते सदृश उद्दीप्त थी। असंख्य गोपियाँ उन्हें घेरे हुए हैं? परंतु पुत्र! तुम जाकर श्रीकृष्णसे मेरी बात थीं। तत्पश्चात्‌ वे हर्षपूर्वक रत्लसिंहासनपर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16132)
- **Original**: कहोगे; मैं तुम्हें सब कुछ बतला रही हूँ। उद्धव! विराजमान हर्षमग्र उद्धवकी पूजा करके बोलीं। मुझे घर और वनमें कोई भेद नहीं प्रतीत होता। श्रीराधिकाने पूछा--उद्धव! कपटरहित हो
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16133)
- **Original**: मेरे लिये जैसे पशु आदि हैं, वैसे ही मनुष्य सच-सच बतलाओ, क्या सचमुच श्रीहरि आयेंगे ?
- **Translation**: 

---


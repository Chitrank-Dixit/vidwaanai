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

### Verse 1 (Vaivtpuran 21.3744)
- **Original**: चुका तथा समस्त यज्ञोंका फल पा गया। अखिल करनेवाला है। जिसमें दो चक्र हों, विशाल मुख
- **Translation**: 

---

### Verse 2 (Vaivtpuran 21.3745)
- **Original**: यज्ञों, तीर्थों, ब्रतों और तपस्याओंके फलका वह हो तथां जो वनमालाके चिहसे सम्पन्न हो, [अधिकारी समझा जाता है। साध्वि! चारों वेदोंके गृहस्थोंके लिये सदा सुखदायी हो, उस पाषाणको
- **Translation**: 

---

### Verse 3 (Vaivtpuran 21.3746)
- **Original**: पढ़ने तथा तपस्या करनेसे जो पुण्य होता है, वही भगवान्‌ 'लक्ष्मीनारायण' का विग्रह समझना चाहिये।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 21.3747)
- **Original**: पुण्य शालग्राम-शिलाकी उपासनासे प्राप्त हो जाता जो द्वार-देशमें दो चक्रोंसे युक्त हो तथा जिसपर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 21.3748)
- **Original**: है। जो निरन्तर शालग्राम-शिलाके जलसे अभिषेक श्रीका चिह्न स्पष्ट दिखायी पड़े, ऐसे पाषाणको
- **Translation**: 

---

### Verse 6 (Vaivtpuran 21.3749)
- **Original**: करता है, बह सम्पूर्ण दानके पुण्य तथा पृथ्वीकी भगवान्‌ 'वासुदेव' का विग्रह मानना चाहिये। इस
- **Translation**: 

---

### Verse 7 (Vaivtpuran 21.3750)
- **Original**: प्रदक्षिणके उत्तम फलका मानों अधिकारी हो विग्रहकी अर्चनासे सम्पूर्ण कामनाएँ सिद्ध हो
- **Translation**: 

---

### Verse 8 (Vaivtpuran 21.3751)
- **Original**: जाता है। शालग्राम-शिलाके जलका निरन्तर पान सकेंगी। सूक्ष्म चक्रके चिहसे युक्त, नवीन मेघके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 21.3752)
- **Original**: करनेवाला पुरुष देवाभिलषित प्रसाद पाता है; सपान श्याम तथा मुखपर बहुत-से छोटे-छोटे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 21.3753)
- **Original**: इसमें संशय नहीं। उसे जन्म, मृत्यु और जरासे छिद्रोंसे सुशोभित पाषाण 'प्रद्युश्न" का स्वरूप
- **Translation**: 

---

### Verse 11 (Vaivtpuran 21.3754)
- **Original**: छुटकारा मिल जाता है। सम्पूर्ण तीर्थ उस होगा। उसके प्रभावसे गृहस्थ सुखी हो जायेंगे।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 21.3755)
- **Original**: पुण्यात्मा पुरुषका स्पर्श करना चाहते हैं। जीवन्मुक्त जिसमें दो चक्र सटे हुए हों और जिसका पृष्ठभाग
- **Translation**: 

---

### Verse 13 (Vaivtpuran 21.3756)
- **Original**: एवं महान्‌ पवित्र वह व्यक्ति भगवान्‌ श्रीहरिके विशाल हो, गृहस्थोंको निरन्तर सुख प्रदान करनेवाले
- **Translation**: 

---

### Verse 14 (Vaivtpuran 21.3757)
- **Original**: पदका अधिकारी हो जाता है। भगवान्‌के धामर्म॑ उस पाषाणको भगवान्‌ “संकर्षण' की प्रतिमा समझनी चाहिये। जो अत्यन्त सुन्दर गोलाकार हो बह उनके साथ असंख्य प्राकृत प्रलयतक रहनेकी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 21.3758)
- **Original**: सुविधा प्रात करता है। बहाँ जाते ही भगवान्‌ उसे तथा पीले रंगसे सुशोभित हो, विद्वान्‌ पुरुष कहते
- **Translation**: 

---

### Verse 16 (Vaivtpuran 21.3759)
- **Original**: अपना दास बना लेते हैं। उस पुरुषको देखकर, हैं कि गृहाश्रमियोंकों सुख देनेवाला वह पाषाण भगवान्‌ 'अनिरुद्ध' का स्वरूप है। जहाँ शालग्रामकी शिला रहती है, वहाँ भगवान्‌ श्रीहरि विराजते हैं और वहां सम्पूर्ण तीर्थोंकों साथ लेकर भगवती लक्ष्मी भी निवास ब्रह्महत्याके समान जितने बड़े-बड़े पाप हैं, वे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 21.3760)
- **Original**: इस प्रकार भागने लगते हैं, जैसे गरुड़कों देखकर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 21.3761)
- **Original**: सर्प। उस पुरुषके चरणोंकी रजसे पृथ्वीदेवी तुरंत पवित्र हो जातो हैं। उसके जन्म लेते ही लाखों पितरोंका उद्धार हो जाता है।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 21.3762)
- **Original**: » प्रकृतिखण्ड « 167 6448 448 0644448262(:2450828240454828240//2822/44
- **Translation**: 

---

### Verse 20 (Vaivtpuran 21.3763)
- **Original**: /8 40 4 4 8 4
- **Translation**: 

---


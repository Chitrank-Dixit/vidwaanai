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

### Verse 1 (Bramha 0.421)
- **Original**: देवशत आदि कई पुत्र हुए, जो सम्पूर्ण विश्वमें हुए सत्यवतीके प्रति प्रसन्‍नता प्रकट कौ और
- **Translation**: 

---

### Verse 2 (Bramha 0.422)
- **Original**: बिख्यात थे। उनके नाम इस प्रकार बतलाये जाते कहा--' सुन्दरि! पुत्र अथवा पौजत्रमें मैं कोई अन्तर
- **Translation**: 

---

### Verse 3 (Bramha 0.423)
- **Original**: हैं। देवरात, कात्यायन गोत्रके प्रवर्तक कति, नहीं मानता। तुमने जो कहा है, जैसा ही होगा।'
- **Translation**: 

---

### Verse 4 (Bramha 0.424)
- **Original**: हिरण्याक्ष, रेणु, रेणुक, सांकृति, गालव, मुद्गडल, तत्पश्चात्‌ सत्यवतीने भृगुवंशी जमदग्रिकों जन्म
- **Translation**: 

---

### Verse 5 (Bramha 0.425)
- **Original**: मधुच्छन्द, जय, देवल, अष्टक, कच्छप और दिया, जो तपस्यापरायण, जितेन्द्रिय तथा सर्वत्र
- **Translation**: 

---

### Verse 6 (Bramha 0.426)
- **Original**: हारोत-ये सभी विश्वामित्रके पुत्र थे। इन समभाव रखनेबाले थे। सत्यवती भी सत्यधर्ममें
- **Translation**: 

---

### Verse 7 (Bramha 0.427)
- **Original**: कौशिकवंशी महात्माओंके प्रसिद्ध गोत्र इस तत्पर रहनेवाली पुण्यात्मा स्त्री थी। वही कौशिकी
- **Translation**: 

---

### Verse 8 (Bramha 0.428)
- **Original**: प्रकार हैं-पाणिनि, ब्ुु, ध्यानजप्य, पार्थिव, नामसे प्रसिद्ध महानदी हुई। इश्ष्वाकुवंशमें रेणु
- **Translation**: 

---

### Verse 9 (Bramha 0.429)
- **Original**: देवरात, शालड्भायन, बाष्कल, लोहितायन, हारीत नामके एक राजा थे। उनकी कन्याका नाम रेणुका
- **Translation**: 

---

### Verse 10 (Bramha 0.430)
- **Original**: और अष्टकाद्माजन। इस वंशमें ब्राह्मण और था। रेणुकाको कामली भी कहते हैं। तप और । क्षत्रियका सम्बन्ध विख्यात है। विश्वामित्रके विद्यासे सम्पन्न जमदग्रिने रेणुकाके गर्भसे अत्यन्त
- **Translation**: 

---

### Verse 11 (Bramha 0.431)
- **Original**: पुत्रोंमें शुनःशेप सबसे बड़ा माना गया है; यद्यपि भयद्भर परशुरामजोकों प्रकट किया, जो समस्त
- **Translation**: 

---

### Verse 12 (Bramha 0.432)
- **Original**: उसका जन्म भृगुकुलमें हुआ था, तथापि वह विद्याओंमें पारड्रत, भनुर्वेदमें प्रवीण, क्षत्रिय-
- **Translation**: 

---

### Verse 13 (Bramha 0.433)
- **Original**: कौशिक गोत्रवाला हो गया। हरिदश्वके यज्ञमें कुलका संहार करनेवाले तथा प्रज्वलित अग्निके
- **Translation**: 

---

### Verse 14 (Bramha 0.434)
- **Original**: वह पशु बनाकर लाया गया था, किन्तु देवताओं ने समान तेजस्वी थे। ऋचीकके सत्यवतीसे प्रथम तो
- **Translation**: 

---

### Verse 15 (Bramha 0.435)
- **Original**: उसे विश्वामित्रकों समर्पित कर दिया। देवताओं द्वारा ब्रह्मवेत्ताओंमें श्रेष्ठ जमदग्र हुए। मध्यम पुत्र
- **Translation**: 

---

### Verse 16 (Bramha 0.436)
- **Original**: प्रदत्त होनेके कारण वह देवरात नामसे बिख्यात शुनःशेप और कनिष्ठ पुत्र शुनःपुच्छ थे। कुशिकनन्दन
- **Translation**: 

---

### Verse 17 (Bramha 0.437)
- **Original**: हुआ। देवरात आदि विश्वामित्रके अनेक पुत्र थे। गाधिने विश्वामित्रको पुत्ररूपमें प्राप्त किया, विश्वामित्रकी पत्नी दृषद्वतीके गर्भसे अष्टकका तपस्वोी, विद्वान्‌ और शान्त थे। वे ब्रह्मर्षिको
- **Translation**: 

---

### Verse 18 (Bramha 0.438)
- **Original**: जन्म हुआ था। अष्टकका पुत्र लौहि बताया गया समानता पाकर वास्तवमें ब्रह्मर्षि हो गये। धर्मात्मा
- **Translation**: 

---

### Verse 19 (Bramha 0.439)
- **Original**: है। इस प्रकार मैंने जहकुलका वर्णन किया। इसके विश्वामित्रका दूसरा नाम विश्वरथ था। विश्वामित्रके
- **Translation**: 

---

### Verse 20 (Bramha 0.440)
- **Original**: बाद महात्मा आयुके बंशका वर्णन करूँगा। #>-ॉ्फअसच2 0000 आयु और नहुषके वंशका वर्णन, रजि एवं ययातिका चरित्र लोमहर्षणजी कहते हैं--आयुके उनकी पत्नी
- **Translation**: 

---


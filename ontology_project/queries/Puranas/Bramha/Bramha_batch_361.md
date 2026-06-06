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

### Verse 1 (Bramha 0.7201)
- **Original**: और पुत्रवधूके साथ समागम तथा स्त्री, बालक होते हैं। ब्राह्मणकी हत्या तथा पृथ्वीका अपहरण
- **Translation**: 

---

### Verse 2 (Bramha 0.7202)
- **Original**: और बूढोंकी हत्या करते हैं, उनकी भी यही दशा करनेवाले और धरोहरकों हड़प लेनेवाले पापी
- **Translation**: 

---

### Verse 3 (Bramha 0.7203)
- **Original**: होती है; वे चौदह इन्द्रोंकी आयुपर्यन्त नरक- उस नरकमें डालकर प्रलयकालतक जलाये जाते
- **Translation**: 

---

### Verse 4 (Bramha 0.7204)
- **Original**: यातनामें पड़े रहते हैं। महारौरव नामक नरक हैं। तदनन्तर रौरव नामक नरक है, जो प्रज्वलित , ज्वालाओंसे परिपूर्ण तथा अत्यन्त भयंकर है, वज़मय बाणोंसे व्याप्त रहता है। उसका विस्तार
- **Translation**: 

---

### Verse 5 (Bramha 0.7205)
- **Original**: उसका विस्तार चौदह हजार योजन है। जो मूढ़ साठ हजार योजनका है। उस नरकमें गिराये हुए
- **Translation**: 

---

### Verse 6 (Bramha 0.7206)
- **Original**: नगर, गाँव, घर अथवा खेतमें आग लगाते हैं, वे मनुष्य जलते हुए बाणोंसे बिंधकर यातना भोगते
- **Translation**: 

---

### Verse 7 (Bramha 0.7207)
- **Original**: एक कल्पतक उस नरकमें पकाये जाते हैं। हैं। झूठी गवाही देनेवाले मनुष्य उसमें ईंखकी
- **Translation**: 

---

### Verse 8 (Bramha 0.7208)
- **Original**: तामिस्न नरकका विस्तार एक लाख योजन है। भाँति पेरे जाते हैं। उसके बाद मज्जूप नामक नरक , वहाँ सदा खड्ग, पट्टिश और मुद्गरोंकी मार पड़ती है, जो लोहेसे बना हुआ है। वह सदा प्रज्वलित
- **Translation**: 

---

### Verse 9 (Bramha 0.7209)
- **Original**: रहती है। इससे वह बड़ा भयंकर जान पड़ता है। रहता है। उसमें वे हो डालकर जलाये जाते हैं,
- **Translation**: 

---

### Verse 10 (Bramha 0.7210)
- **Original**: यमराजके दूत चोरोंको उसीमें डालकर शूल, जो दूसरोंको निरपराध बंदी बनाते हैं। अप्रतिष्ठ
- **Translation**: 

---

### Verse 11 (Bramha 0.7211)
- **Original**: शक्ति, गदा और खड्गसे उन्हें तीन सौ कल्पोंतक नामक नरक पीब, मूत्र और विष्ठाका भंडार है।
- **Translation**: 

---

### Verse 12 (Bramha 0.7212)
- **Original**: पीटते रहते हैं। महातामिल्ल नापक नरक और भी उसमें ब्राह्मणको पीड़ा देनेवाला पापी नीचे मुँह
- **Translation**: 

---

### Verse 13 (Bramha 0.7213)
- **Original**: दुःखदायी है। उसका विस्तार तामिस्तकी अपेक्षा करके गिराया जाता है। विलेपक नामका घोर
- **Translation**: 

---

### Verse 14 (Bramha 0.7214)
- **Original**: दूना है। उसमें जोंकें भरी हुई हैं और निरन्तर नरक लाहकी आगसे जलता रहता है। उसमें
- **Translation**: 

---

### Verse 15 (Bramha 0.7215)
- **Original**: अन्धकार छाया रहता है। जो माता, पिता और मदिरा पीनेवाले द्विज डालकर जलाये जाते हैं।
- **Translation**: 

---

### Verse 16 (Bramha 0.7216)
- **Original**: मित्रकी हत्या करनेवाले तथा विश्वासघाती हैं, वे महाप्रभ नामसे विख्यात नरक बहुत ऊँचा है।
- **Translation**: 

---

### Verse 17 (Bramha 0.7217)
- **Original**: जबतक यह पृथ्वी रहती है, तबतक उससमें पड़े उसमें चमकता हुआ शूल गड़ा होता है। जो लोग रहते हैं और जोंकें निरन्तर उनका रक्त चूसती पति-पलोमें भेद डालते हैं, उन्हें वहीं शूलसे छेदा
- **Translation**: 

---

### Verse 18 (Bramha 0.7218)
- **Original**: रहती हैं। असिपत्रवन नामक नरक तो बहुत ही जाता है। उसके बाद जयन्ती नामक अत्यन्त घोर
- **Translation**: 

---

### Verse 19 (Bramha 0.7219)
- **Original**: कष्ट देनेवाला है। उसका बिस्तार दस हजार नरक है, जहाँ लोहेकी बहुत बड़ी चट्टान पड़ी
- **Translation**: 

---

### Verse 20 (Bramha 0.7220)
- **Original**: योजन है। उसमें अग्निके समान प्रज्वलित खड्ग रहती है। परायी स्थ्रियोंक साथ सम्भोग करनेवाले
- **Translation**: 

---


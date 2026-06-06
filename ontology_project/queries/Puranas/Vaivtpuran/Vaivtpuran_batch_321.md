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

### Verse 1 (Vaivtpuran 15.6773)
- **Original**: सत्यकों छोड़कर अमड्रलकी इच्छा न करे। चोटसे सूर्यकी चेतना नष्ट हो गयी और वे तुरंत
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.6774)
- **Original**: इसलिये अब मैं विषयका परित्याग करके ही रथसे नीचे गिर पड़े। जब कश्यपजीने देखा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.6775)
- **Original**: परमेश्वर श्रीकृष्फा भजन करूँगा।' यह सुनकर कि मेरे पुत्र॒की आँखें ऊपरको चढ़ गयी हैं और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.6776)
- **Original**: देवताओंने ब्रह्माको प्रेरित किया, तब उन प्रभुने वह चेतनाहीन हो गया है, तब वे उसे छातीसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.6777)
- **Original**: शीघ्रतापूर्वक वहाँ पधारकर सूर्यकों समझाया और लगाकर फूट-फूटकर बिलाप करने लगे। उस
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.6778)
- **Original**: उन्हें इनके कार्यपर नियुक्त किया। फिर ब्रह्मा, समय सारे देवताओंमें हाहांकार मच गया। वे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.6779)
- **Original**: शिव और कश्यप आनन्दपूर्वक सूर्यको आशीर्वाद सभी भयभीत होकर जोर-जोरसे रुदन करने
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.6780)
- **Original**: देकर अपने-अपने भवनको चले गये। इधर सूर्य लगे। अन्धकार छा जानेसे सारा जगत्‌ अंधीभूत।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.6781)
- **Original**: भी अपनी राशिपर आरूढ़ हुए। तत्पश्चात्‌ माली (637] सं0 ख्र0 बै0 पुराण
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.6782)
- **Original**: 332 + संक्षिप्त ख्रह्मवैचर्तपुराण * अ5अ&### #%48 85 4 4 # 4 54458 / डक क्र अ्ड पक ब्फअकरऋ कक पक कफ कक अर ऋप् क अप पर परम पर अ ड़ 28 धर 6 अर क # और सुमाली व्याधिग्रस्त हो गये। उनके शरीरमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.6783)
- **Original**: ब्रह्यलोकको चले गये। मुने! तदनन्तर बे दोनों सफेद कोढ़ हो गयी, जिससे सारा अज्ज गल
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.6784)
- **Original**: पुष्करमें जाकर सूर्यका भजन करने लगे। वहाँ गया, शक्ति जाती रही और प्रभा नष्ट हो गयी।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.6785)
- **Original**: वे तीनों काल स्नान करके भक्तिपूर्वक उत्तम सूर्य- तब स्वयं ब्रह्माने उन दोनोंसे कहा--सूर्यके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.6786)
- **Original**: मन्त्रके जपमें तल्लीन हो गये। फिर समयानुसार कोपसे ही तुम दोनों हतप्रभ हो गये हो और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.6787)
- **Original**: सूर्यसे वरदान पाकर वे पुनः अपने असली रूपमें तुम्हारा शरीर गल गया है, अतः तुमलोग सूर्यका
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.6788)
- **Original**: आ गये। इस प्रकार मैंने यह सारा वृत्तान्त वर्णन भजन करो।' फिर ब्रह्मा उन दोनॉंको सूर्यका कर दिया, अब और क्‍या सुनना चाहते हो? कवच, स्तोत्र और पूजाकी सारी विधि बतलाकर (अध्याय 18) #2+*++8--#य#थ9395-505+>ल ब्रह्माद्वारा माली-सुमालीको सूर्यके कवच और स्तोत्रकी प्राप्ति तथा सूर्यकी कृपासे उन दोनोंका नीरोग होना तदनन्तर नारदजीके पूछनेपर नारायण
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.6789)
- **Original**: ब्रह्मा उन दैत्योंके घर गये। तब दैत्योंने उन्हें बोले--नारद! मैं श्रीसूर्यके पूजनका क्रम तथा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.6790)
- **Original**: प्रणाम करके कुशल-समाचार पूछा और बैठनेके सम्पूर्ण पापों और व्याधियोंसे विमुक्त करनेवाले
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.6791)
- **Original**: लिये आसन दिया। उन दैत्योंका शरीर गल गया कवच और स्तोत्रका वर्णन करता हूँ, सुनो।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.6792)
- **Original**: था, उसमेंसे पीव और दुर्गन्ध निकल रही थी। जब माली और सुमाली-ये दोनों दैत्य
- **Translation**: 

---


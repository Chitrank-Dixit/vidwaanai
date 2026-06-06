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

### Verse 1 (Markende Puran 0.3081)
- **Original**: देवता अक्षभागका उपभोग छरें
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3082)
- **Original**: यदि खलके 1. पा--जानुप॑तर:
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3083)
- **Original**: 220 50225222 2474 #677 &566555:2772:2.227 भ्रपंडमें आकर तुम युद्धकी अभिलापा रमख्क्ते हो तो आओ। मेरी शिनाएँ (योगिनियाँ) तुम्हारे कच्चे मांससे तृप्त हों
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3084)
- **Original**: चूँकि उस देवीतें भगवान्‌ शिक्षकों दूतके कार्यमें नियुक्त क्रिया था, इसलिये वह 'शित्रदूती' के नामसे संस्नारमें विख्यात हुई
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3085)
- **Original**: थे महादैत्य भी भगवान्‌ शित्रके मुँहसे देबोके त्चन सुनकर क्रोधमें भर गये और जहाँ कात्यायदी विराजमान थीं, उस ओर बढ्ढे
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3086)
- **Original**: तदननार के दैत्य अमर्पमें भरकर पहले हो टेवीके कप बाण, शक्ति और ऋष्टि आदि अस्‍्त्रोंकी चृष्टि करने लगे
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3087)
- **Original**: तब देवीने भी ख्ेल-खेलमें हो धनुषको टंकार की और उससे छोड़े हुए बड़े- बड़े दाणोंद्रारा देत्योंके चलाये हुए बाण, घशूल, शक्ति और फरसेक्ये काट डाला
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3088)
- **Original**: फिर काली उसके आगे होकर शत्रुऑकों शूलके प्रहारसे बिंदीर्ण करने लगी और ख़ट्वाड्भसे उनका कचूमर बिचरने लगी
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3089)
- **Original**: 1, पा0-- न्यास्त0। 2. पा7>-तस्‍य। « संक्षिप्त मार्कण्डेयपुराण « 40#+444 4566 62 7:27:520.0 7777 +7 #++.&555:2 2:22. «7 744 #+*< 637: अह्माणों भी जिस जिस ओर दौड़ती, उसो-उसो ओर अपने कमण्डलुका जल छिड्ककर शत्तुओंके ओज और पराक्रमकों नष्ट कर देती थीं
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3090)
- **Original**: महेंश्वरोने तरिशुलसे तथा वैध्णबीने अक्रसे और अत्पन्त क्रोधमें भरी हुई कुमार कार्तिकेयकी शक्तिने शक्तिसे दैत्योंका संहार आरम्भ किवा
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3091)
- **Original**: इन्द्रशक्तिके चजप्रहारसे विदार्ण हो सैकड़ों देत्य- दानव रक्तकी धारा बहाते हुए पगृथ्वोपर सो गये
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3092)
- **Original**: च्रारशही शक्तिने कितयोंको अपनी भुथुनकी मारसे नष्ट किया, दाढ़ोंके अग्रभागसे कितनोंकी छाती क्लेद डाली तथा कितने ही दैत्य चक्रकी चोटसे विदीर्ण हो गये
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3093)
- **Original**: नारसिही भी दूसरे-दूसेरे महादैत्योंकों अपने नखोंसे दिदोर्ण करके खाती और सिंहनादसे दिशाओं एवं आकाशकों गुँजाती हुईं युद्ध-क्षेत्रमें किचरने लगी
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3094)
- **Original**: कितने ही असुर शिवदूतोंके प्रदण्ड अड्रह्माससे अत्यन्त भयभीत हो प्रृशत्रीपर गिर पड़े और गिरनेपर उन्हें शिबदूतीने उस समय अपना ग्रास्त बना लिया
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3095)
- **Original**: डति मातृगणं कुद्ध॑ मर्देयन्त महाखुतन्‌। दृष्ठाध्युपायैविविधैर्नेशुदेवारिसेनिका:
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3096)
- **Original**: पलायनपरान्‌ वृष्ठा देत्वान्‌ मातृगणार्दितान्‌। योद्धुपध्यायथी क़ुद्धो रक्तबोजों महासुर:
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3097)
- **Original**: रक्तबिन्युर्धदा भूमी पतत्वस्थ शरीरतः। समुत्यतति मेदिन्यां' तत्प्रमाणस्तदासुर:
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3098)
- **Original**: युयुथे स गदापाण्ििरिडिशक्तथा महासुरः। ज्ञतऔ दी स्ववज्रेण रक्तयीजमताडयत्‌
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3099)
- **Original**: कुलिशेनाहतस्याशु बहु" सुख्याव शोणितम्‌
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3100)
- **Original**: समुन्तस्थुस्ततों योधास्तद्रूपास्तत्पराक्रमा:
- **Translation**: 

---


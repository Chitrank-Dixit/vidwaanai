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

### Verse 1 (Markende Puran 0.3541)
- **Original**: जो मेरे इस चरित्रकां स्मरण करता है, बह मनुष्य संकटसे मुक्त हो जाता हैं। में! प्रभावसे सिंह आदि हिंसक जन्नु नष्ट हो जाते हैं तथा
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3542)
- **Original**: 238 > संक्षिप्त मार्कफ्डेयपुराण « 22 22593 50007 रूल7 ++#44 4 #448:666657::37227:/: 57777 744 44478 #& 8 3 828 22202: 002//54-4/4744 64854 लुटेरे और शत्रु भी मेरे चरित्रका स्मरण करनेत्राले
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3543)
- **Original**: देखते-देखते वहीं अन्तर्थाग हो ग्थी। फिर समस्त पुरुषमे दूर भागते हैं
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3544)
- **Original**: देवता भो शत्रुओंके मारे जानेसे निर्धय हो पहलेकी ऋपिरचासा
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3545)
- **Original**: ही भाँति यज्ञभागका ठपभोग करते हुए अपने अपने इत्युक्ला सा भगषती चणिड़का चण्डविक्रमा
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3546)
- **Original**: , अधिकास्का पालन करने लगे। संसाएका विश्यंस पश्यतामेव' देवानों ततैधान्तरधीयत। .
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3547)
- **Original**: करनेवाले महाभवड्डूर अतुछलपराक्रमी देवशत्रु शुम्भ तेशपे देवा निशतड्भपः स्वाधिकारान्‌ यथा पुण
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3548)
- **Original**: तथा पहाबली निशुम्भके युद्धमें देवीद्वारा मारे जानेपर यज्ञभागभूज: सर्वे अक्रुर्सितिहतारय:
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3549)
- **Original**: शेष दैत्व पाताललोकमें चले आये
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3550)
- **Original**: 32--35
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3551)
- **Original**: दैत्वाञ्न देव्या निहते शु््पे देवरिपौ युथि &34
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3552)
- **Original**: राजन! इस प्रकार भगवती अम्यिका देवी दित्य होती जगद्विष्वेसिनि तस्मिन्‌ महोग्रेउतुलविक्रमे। हुई भी पुनः- पुन: प्रकट होकर जगंतकी रक्षा करती निशुध्मे चर महावीयें श्ेघा: पातालमाययु:
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3553)
- **Original**: हैं 8 36
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3554)
- **Original**: वे हो इस विश्वको पोहिंत करतों. वे ही एवं भगयतो देवी सा तित्याधि पुन: पुनः । जगतूको जन्म देतों तथा त्रे हो प्रार्थन करनेपर सन्तुष्ट सम्भूय कुरुते भूष जगतः परिषालनम्‌
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3555)
- **Original**: हो विज्ञान एवं सर्प्ाद्धि प्रदान करतों हैं
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3556)
- **Original**: तयतन्मोहाते विश्व सेव विश्व प्रसूयते। राजन्‌! महाप्रलयके समय मंहामारीका स्वरूप धारण सा चांचिता जा विज्ञान तुष्टा ऋद्धि प्रदच्छति
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3557)
- **Original**: करनेवाली वें 'महाक्ाली ही इस समस्त ब्रह्माण्डमें व्याप्त॑ ततत्सकर्ल ग्रह्माण्ड मनुजेश्रर। व्यात्ते हैं
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3558)
- **Original**: थे हो समय-समथ्रपर महामारी मसहाक्राल्या महाकाले महामारीस्वरूपया
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3559)
- **Original**: होती और वे हो स्तर अजन्मा ज्ञोतों हुई भो सृष्टिके सैब ' काले महासारी सै सृष्टिभवत्यजा।
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3560)
- **Original**: रूममें प्रकट होती हैं। बे सनाहनी देखी ही समयानुसार स्थिति करोति भूतानां सैव काले सनातनी
- **Translation**: 

---


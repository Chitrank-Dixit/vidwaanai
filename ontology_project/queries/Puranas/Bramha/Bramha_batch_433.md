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

### Verse 1 (Bramha 0.8641)
- **Original**: (परम धाम)-को प्राप्त होता है। जिस प्रकार भयंकर पराक्रम दिखानेवाली मृत्युका भी जोर नहीं
- **Translation**: 

---

### Verse 2 (Bramha 0.8642)
- **Original**: सावधान सारथि अच्छे घोड़ोंको रथमें जोतकर चलता। वह योगबल पाकर अपने हजारों रूप बना
- **Translation**: 

---

### Verse 3 (Bramha 0.8643)
- **Original**: धनुर्धर श्रेष्ठ बोरको तुरंत अभीष्ट स्थानपर पहुँचा सकता और उन सबके द्वारा इस पृथ्वीपर विचर देता है, वैसे ही धारणाओमें चित्तकों एकाग्र सकता है। फिर तेजको समेट लेनेवाले सूर्यकी
- **Translation**: 

---

### Verse 4 (Bramha 0.8644)
- **Original**: करनेवाला योगी लक्ष्यकी ओर छूटे हुए बाणकी भ्रौति वह उन सभी रूपोंकों अपनेमें लोन करके
- **Translation**: 

---

### Verse 5 (Bramha 0.8645)
- **Original**: भाँति शीघ्र परम पदको प्राप्त कर लेता है। जो उग्र तपस्यामें प्रवृत्त हो जाता है। बलवान्‌ योगी
- **Translation**: 

---

### Verse 6 (Bramha 0.8646)
- **Original**: समाधिके द्वारा अपने आत्माको परमात्मामें लगाकर बन्धन तोड़नेमें समर्थ होता है। उसमें अपनेको
- **Translation**: 

---

### Verse 7 (Bramha 0.8647)
- **Original**: स्थिर भावसे बैठा रहता है, उसे अजर (बुद़ापेसे मुक्त करनेकी पूर्ण शक्ति होती है।
- **Translation**: 

---

### Verse 8 (Bramha 0.8648)
- **Original**: रहित) पदकी प्राप्ति होती है। योगके महान्‌ न्रतमें : द्विजबरो! ये मैंने योगकी स्थूल शक्तियाँ
- **Translation**: 

---

### Verse 9 (Bramha 0.8649)
- **Original**: एकाग्रचित्त रहनेवाला जो योगी नाभि, कण्ठ, भतायी हैं। अब दृष्टान्तके लिये योगसे प्राप्त
- **Translation**: 

---

### Verse 10 (Bramha 0.8650)
- **Original**: पाश्चभाग, हृदय, वक्ष:स्थल, नाक, कान, नेत्र और होनेवालो कुछ सूक्ष्म शक्तियोंका वर्णन करूँगा
- **Translation**: 

---

### Verse 11 (Bramha 0.8651)
- **Original**: मस्तक आदि स्थानोंमें धारणाके ड्वारा आत्माको तथा आत्म-समाधिके लिये जो चित्रकों धारणा
- **Translation**: 

---

### Verse 12 (Bramha 0.8652)
- **Original**: परमात्माके साथ युक्त करता है, बह पर्वतके की जातो है, उसके विषयमें भी कुछ सूक्ष्म
- **Translation**: 

---

### Verse 13 (Bramha 0.8653)
- **Original**: समान महान्‌ शुभाशुभ कर्मोंको भी शौष्र ही भस्म दृष्टान्न बतलाऊकँगा। जिस प्रकार सदा सावधान
- **Translation**: 

---

### Verse 14 (Bramha 0.8654)
- **Original**: कर डालता है और इच्छा करते ही उत्तम योगका
- **Translation**: 

---

### Verse 15 (Bramha 0.8655)
- **Original**: » योग और साख्यका संक्षिएर वर्णन * 415 पपय ले यक हो जाल है। ......
- **Translation**: 

---

### Verse 16 (Bramha 0.8656)
- **Original**: विलोन रहती हैं। उनकी सूक्ष्म गतिका आश्रय
- **Translation**: 

---

### Verse 17 (Bramha 0.8657)
- **Original**: उनकी गतिका आश्रय हम 2 30200
- **Translation**: 

---

### Verse 18 (Bramha 0.8658)
- **Original**: (03000 +3045 स्पयेकियंता है: शरद; निर्मल अन्त:करणवाले यति परमात्माको प्राप्त «335 व न पअप करे जनक करके तद्गरप हो जाते हैं। उन्हें अमृतत्व मिल जाता "4 4 5:44 न "0 पटक 00 +-+ कक
- **Translation**: 

---

### Verse 19 (Bramha 0.8659)
- **Original**: क्षेत्रज् आत्मा सम्पूर्ण क्षेत्रोंमे विचरण करता है। परम गति है। जो सब 4. 4 2 हुंधधी-नधतिआ पर हे भ् जी (2 इन्द्रियाँ हा 4-30 अनुसरण मसाले हे उप महान सी की है *2क-अ> मी है प्राप्त होती है। सांख्ययोगी प्रकृतिका हु: 4008 क+6804264 »4-20:«-4 /8/«--.-+ 408 %%00702:5 0 कक +« करते
- **Translation**: 

---

### Verse 20 (Bramha 0.8660)
- **Original**: परमात्मा श्रीनारायणको प्राप्त होते हैं। विप्रवरों! कान सफर पक मिला जी है? यहाँ
- **Translation**: 

---


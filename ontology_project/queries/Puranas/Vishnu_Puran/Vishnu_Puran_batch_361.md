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

### Verse 1 (Vishnu Puran 0.7201)
- **Original**: चतुर्थ अंझ 257 उसका उाह््द सुना
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7202)
- **Original**: तब यह बोली--- मुझ अनाथाके पुत्रको कौन लिये जाता है, अब मैं किसकी शरण जाऊँ 7”
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7203)
- **Original**: किन्तु यह सुनकर भी इस भयसे कि रानी मुझे नंगा देख लेगी, राजा नहीं उठा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7204)
- **Original**: तदनत्तर गन्धर्यधगण दूसरा भी मेष छेकर चल दिये।
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7205)
- **Original**: उसे ले जाते समय उसका इझाब्द सुनकर भी उर्वशी 'हाय ! मैं अनाथा और भर्तुहीना हुँ तथा एक कायरके अधीन हो गयी हूं।' इस प्रकार कहती हुई यह आर्तस्वस्से त्रित्मप करने छूगी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7206)
- **Original**: तब राजा यह सोचकर कि इस समय अन्धकार है (अतः रानी मुझे नग्न न देख सकेगी], क्रोधपूर्वक 'ओरे दुष्ट ! तू मारा गया' यह कहते हुए तलवार लेकर पीछे दौड़ा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7207)
- **Original**: इसी समय गज्धजेनि अति उज्ज्वर्त सिध्युत्‌ प्रकट कर दी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7208)
- **Original**: उसके प्रकाशमें राजाक्ये वस्नहीन देखकर प्रतिज्ञा टूट जानेसे उर्वज्ञो तुरत्त ही वहाँसे चल्मे गयी
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7209)
- **Original**: गन्षर्वगण भी उन मेषोंकों कहीं छोड़कर स्वर्गलोकमें चले गये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7210)
- **Original**: किन्तु जब राजा उन मेषोंको लिये हुए अति प्रसन्नचित्तसे अपने शायनागारमें आया तो वहां उसने उर्वशीको न देखा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7211)
- **Original**: उसे न देखनेसे वह उस वस्नहीन-अवस्थामें ही पागलके समाग घूमने लगा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7212)
- **Original**: घूमते-घृमघते उसने एक दिन कुरुक्षेत्रक कमल-सरोवरमें अन्य चार अप्सराओंके सहित उर्वशीको देखा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7213)
- **Original**: उसे देख्ककर बह उन्पक्तके समान 'हे जाये ! उहर, अरी हृदयकी निष्ठरे ! खड़ी हो जा, अरी कपट रखनेवालों ! वार्तात्ँ्रपके लिये तनिक ठहर जा --ऐसे अनेक वचन कहने लगा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7214)
- **Original**: उर्वशी बोली--''महाराज ! इन अआज्ञानियोंकी-सोी चेष्टाओंसे कोई स्थभ नहीं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7215)
- **Original**: इस समय में गर्भवती हूँ। एक वर्ष उपरान्त आप यहीं आ जायें, उस समय आपके एक पुत्र होगा और एक रात मैं भी आपके साथ रहूँगी।” उर्वज्ञीके ऐसा कहनेपर राजा पुरूरवा प्रसन्न-चित्तसे अपने नगरकों चला गया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7216)
- **Original**: तदनत्तर उर्वशीने अन्य अप्सराओसे कहा--
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7217)
- **Original**: “ये यही पुरुषश्रेष्न हैं जिनके साथ मैं इतने दिनॉतक प्रेमाकृष्ट-चित्तसे भूमण्डलमें रही थी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7218)
- **Original**: इसपर अन्य अप्सराओनि कहा--
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7219)
- **Original**: “वाह ! वाह ! सचमुच इनका रूप बड़ा ही मनोहर है, इनके साथ तो सर्यदा हमारा भी सहवास हो"
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7220)
- **Original**: वर्ष समाप्त होनेपर राजा पुरूरवा वहाँ आये
- **Translation**: 

---


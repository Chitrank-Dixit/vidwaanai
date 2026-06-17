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

### Verse 1 (Vaivtpuran 543.15594)
- **Original**: कालसूत्र नरकमें जाता है। वहाँ सौ वर्षोतक है, “उसे सात जन्मोंतक कौआ होना पड़ता है।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15595)
- **Original**: यातना भोगकर फिर हजार बर्षोकी आयुवाला लोहेकी चोरी करनेवाला संतानहीन, मषी चुरानेवाला
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15596)
- **Original**: प्रेत होता है। इसके बाद वह एक जन्मतक कोकिल, अम्जनका चोर शुक और मिठाई चुरानेवाला
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15597)
- **Original**: मक्खी, एक जन्ममें चींटी, एक जन्ममें भ्रमर, कीड़ा होता है। तात! ब्राह्मण और गुरुसे द्वेष एक जन्ममें मधुमक्खी, एक जन्ममें बरं, एक करनेवाला सिरका कोट--जूँ होता है। पुंश्वली
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15598)
- **Original**: जन्ममें डाँस, एक जन्ममें मच्छर, एक जनन्‍्ममें स्त्रीका भोग करके पुरुष रौरब नरकमें जाता है
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15599)
- **Original**: दुर्गन्धयुक्त कौट और एक जन्ममें खटमल होनेके और फिर सौ वर्षोतक निरर्थक कीट होता है
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15600)
- **Original**: बाद दुर्बुद्धि एवं रोगग्रस्त शुद्र होता है। फिर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15601)
- **Original**: + श्रीकृष्णजन्मखण्ड + 681 ऋ$$#%%%%$%$%ऊक$%$%$%ऋ$%ककककऊक कक %##/##%######%%#%%####%$%%$%#$##%%%ऋऋ$%%%$%%अ%$$% कक कक उससे मुक्त होकर ब्राह्मण हो जाता है। तेलकी ब्रजेश्व! जो मिट्टी, भस्म और गोबरके चोरी करनेवाला तेली तीन जन्मोंतक सिरका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15602)
- **Original**: पिण्डोंसे अथवा बालुकासे शिवलिक्ञका निर्माण कौट--जूँ होता है। जो दुष्ट क्षेत्रकी सीमा--मेड़को
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15603)
- **Original**: करके एक बार भी उसका पूजन करता है, वह नष्ट करनेवाला, भूमिचोर, हिंसक तथा दान की
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15604)
- **Original**: कल्पपर्यन्त स्वर्गमें निवास करता है। तत्पश्चात्‌ हुई भूमिको बापस ले लेनेवाला है, वह अवश्यमेव
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15605)
- **Original**: वह भूमिका स्वामी एवं महादिद्वान्‌ ब्राह्मण होता कालसूत्र नरकमें जाता है। वहाँ भूख-प्याससे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15606)
- **Original**: है। सौ लिड्रोंका पूजन करनेसे मनुष्य भारतवर्षमें पीड़ित होकर साठ हजार बर्षोतक कष्ट भोगता राजा होता है। एक हजार लिड्भपूजनसे उसे है। तत्पश्चात्‌ विष्ठाका कीड़ा होकर उत्पन्न होता
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15607)
- **Original**: निश्चित फलकी प्राप्ति होती है। बह चिरकालतक है। इसके बाद एक जन्ममें असत्‌ शुद्र होता
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15608)
- **Original**: स्वर्गमें निवास करके अन्तमें भारतभूमिपर राजेन्द्र है और उसके बाद शुद्ध हो जाता है। इसलिये
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15609)
- **Original**: होता है। दस हजार लिड्ड-पूजनसे राजाधिराज विद्वान्‌को चाहिये कि वह यह सब जानकर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15610)
- **Original**: और एक लाख लिड्र-पूजनसे चक्रवर्ती सम्राट यत्रपूर्वक इनसे सावधान रहे। लाल वस्त्रको
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15611)
- **Original**: हो जाता है। अत्यन्त भक्तिपूर्वक पूजन करनेसे चुरानेवाला एक जन्ममें लाल रंगका कीड़ा होता
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15612)
- **Original**: उसका अतिरिक्त फल मिलता है। तीर्थल्लान, दान, है। फिर एक जन्ममें शूद्र होता है; इसके बाद
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15613)
- **Original**: ब्रह्मभोज, नारायणार्चन आदि कर्मसे वह ब्राह्मणर्वृशमें शुद्ध होकर ब्राह्मण हो जाता है। जो ब्राह्मण तीनों
- **Translation**: 

---


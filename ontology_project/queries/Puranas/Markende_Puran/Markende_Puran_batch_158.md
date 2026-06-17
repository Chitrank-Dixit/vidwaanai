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

### Verse 1 (Markende Puran 0.3141)
- **Original**: रक्त गिया
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3142)
- **Original**: किंतु ज्यों हो वह गिर त्यों ही महादैत्योंको हुम अपने इस उतावले मुखसे खा
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3143)
- **Original**: चामुण्डाने उसे अपने मुखर ले लिया। रक्त जाओ
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3144)
- **Original**: इस प्रकार रक्तसे उत्पन्न होनेवाले
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3145)
- **Original**: गिलेसे कालीके मुखमें जो महादैत्य उत्पन्न महादैत्वोॉका भक्षण करती हुई तुम रणमें विचरती
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3146)
- **Original**: हुए, उन्हें भी बह चट कर गयी और उसने रहों
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3147)
- **Original**: ऐसा करनेसे उस दैत्यका सारा रक्त क्षीण हो रक्तबीऊका रक्त भी पी लिया
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3148)
- **Original**: तदनन्तर जानेपर बह स्वयं भो नश्ट हो जायगा
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3149)
- **Original**: उन देवबीने रक्तबरीजकों, जिसका रक्त चामुण्डाने पी पयड्डर देत्थोंकी जन तुम खा जाओगी तो दूसरे लिया था, बज, छाण, खड़्ग तथा ऋष्टि आदिसे नये द्वैत्व उत्पन्न नहीं हो म़केंगे।' कालीसे यों मार डाला
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3150)
- **Original**: ग़ज़न्‌
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3151)
- **Original**: इस प्रकार शस्त्रोंके कहकर चण्डिका देवोने शूलसे रक्तत्रीजको मार
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3152)
- **Original**: समुदावसे आहत एज रक्तहीन हुआ महादैत्य और कालोने अपने मुझमें उसका रक्त ले लिया। रक्तबीज पृथ्वीपर गिर पड़ा। नरेधर
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3153)
- **Original**: इससे देवताओंको तब उसने वहाँ चण्डिकापर गदासे प्रहार किया
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3154)
- **Original**: अनुपम हर्षकी प्राप्ति हुई
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3155)
- **Original**: और मातृगण किंतु उस गदापातने देवीको तर्क धो चेदना नहों
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3156)
- **Original**: उन असुरोंके रक्रपानके मदसे उद्धत-सा होकर गहुँचायी। रक्तबोजके घायल शरीरसे बहुत-सा
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3157)
- **Original**: नृत्य करने लगा
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3158)
- **Original**: झति #रीसार्कण्डेबपुराणे झाकार्णिके गन्तन्कों दैवोँगाहात्ये रक्तत्ीजतशों ऊमाए्यो5ख्याव:
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3159)
- **Original**: बबल्मच ह, अर्था्लोकः 9. शलोकाः 619, एक 693, एकग्रादित:
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3160)
- **Original**: इस प्रकार श्रीयार्कण्डेब्रपुराणपें स्ावर्णिक्र मन्वन्तरकमी कथाके अन्तर्गत देवीमाहात्प्यमें 'रक्तजीज-सेअ' नामक आठवाँ अध्याय पूरा हुआं
- **Translation**: 

---


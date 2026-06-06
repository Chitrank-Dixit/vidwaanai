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

### Verse 1 (Vishnu Puran 0.1721)
- **Original**: 38 । भ्रान्तिरहितमनिद्रमजरामरम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1722)
- **Original**: 49 अरजो5शब्दममृतमप्रुतं यदसंवृत्तम्‌ । पूर्वापरे न वे वस्मिस्तद्विष्णो: परम पदम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1723)
- **Original**: 42 परमेशत्वगुणवत्सर्वभूतमसंश्रवम्‌ । नता: स्म तत्पदं विष्णोजिह्वादृग्गोचरं न यत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1724)
- **Original**: 43 प्रथम अंच् 33 [ नारायण ] को नमस्कार है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1725)
- **Original**: जो कठिनतायुक्त होकर इस सा्पूर्ण संसारक्रो धारण करते हैं और शब्द आदि पाँचों विषयोकि आधार तथा व्यापक हैं, उन भूमिरूप भगवानूकों नमस्कार है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1726)
- **Original**: जो संसारका योनिरूप है और समस्त देहधारियॉंका बीज है, भगतान्‌ हरिके उस जलस्वरूपको हम नमस्कार करते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1727)
- **Original**: जो समस्त देलताओंका हव्यभुक्‌ू और पितृगणका कव्यभुक मुख है, उस अग्रिस्वरूप विष्णुभगवानकों नमस्कार है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1728)
- **Original**: जो प्राण, अपान आदि पाँच प्रकारसे देहमें स्थित होकर दिन-रात चेष्टा करता रहता है तथा जिसकी योनि आकाश है, उस वायुरूप भगवानकों नमस्कार है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1729)
- **Original**: जो समस्त भूतोंको अलकाश देता है उस अनन्तमूर्ति और परम झुद्ध आक्ादास्वरूप प्रभुको नमस्कार है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1730)
- **Original**: समस्त इन्द्रिय-सृष्टिके जो उत्तम स्थान हैं तन दाब्द-स्पर्शादिरूप बिधाता श्रीकृष्णचन्द्रको नमस्कार है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1731)
- **Original**: जो क्षर और सअश्ठर इन्द्रियरूपसे नित्य विषयोको ग्रहण करते हैं उन ज्ञानमूल्ठ हरिको नमस्कार है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1732)
- **Original**: इन्द्रियोंके द्राश ग्रहण किये विषयोंको जो आत्माके सम्मुख उपस्थित करता है उस अन्त:करण- रूप विश्वात्माकों नमस्कार है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1733)
- **Original**: जिस अनन्तमें सकल चिश्व स्थित है, जिससे तह उत्पन्न हुआ है और जो उसके लयका भी स्थान है उस प्रकृतिस्वरूप परमात्माकों नमस्कार है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1734)
- **Original**: जो शुद्ध और निर्युण होकर भो भ्रमषष्गा गुणयुक्त-से दिखायी देते हैं उन आत्मस्वरूप पुरुषोत्तरदेवकों हम नमस्कार करते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1735)
- **Original**: जो अविकारी, अजन्मा, शुद्ध, निर्णुण, निर्मल और श्रीविष्णुका परमपद है उस ब्रह्मस्वरूपको हम नमस्कार करते हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1736)
- **Original**: जो न लम्बा है, न पतल्म है, न मोटा है, न छोटा है और न काला है, न लाल है; जो स्तरेह (द्रव), कान्ति तथा शरोरसे रहित एवं अनासक्त और अशरीरी (जीवसे भिन्न) है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1737)
- **Original**: जो अवकाह्ञ स्पर्दा, गन्‍ध और रससे रहित तथा आँख-कान-यिहोन, अचल एवं जिड़ा, हाथ और मनसे रहित है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1738)
- **Original**: जो नाम, गोत्र, सुख और ततेजसे शून्य तथा कारणहीन है; जिसमें भय, भ्रान्ति, निद्रा, जप और मरण--इन (अवस्थाओं) का अभाव है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1739)
- **Original**: जो अरज (रजोगुणरहित), अशन्द, अमृत, अप्लुत (गतिशुन्य) और असंवृत (अनाच्छादित) है एवं जिसमें पूर्वापर व्यवहारकी गति नहीं है कही भगवान्‌ किष्णुका परमपद है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1740)
- **Original**: जिसका ईशान (हासन) ही
- **Translation**: 

---


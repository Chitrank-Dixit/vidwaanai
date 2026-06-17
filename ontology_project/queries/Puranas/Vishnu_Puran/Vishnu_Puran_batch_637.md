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

### Verse 1 (Vishnu Puran 0.12721)
- **Original**: 37 एसे यमास्सनियमाः पश्च पश्ञ च कोर्तिता: । विशिष्टफलदा: काम्या निष्कामाणां विमुक्तिदा:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12722)
- **Original**: 38 एकं भद्रासनादीनां समास्थाय गुणैर्युतः । यमाख्यैर्नियमास्थैश्न युज्नीत नियतो यतिः:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12723)
- **Original**: 39 प्राणाख्यमनिलं वश्यमश्यासात्कुरुते तु यत्‌ । प्राणायामस्स विज्ञेयस्सबीजो5बीज एवं च
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12724)
- **Original**: 40 परस्परेणाधिभवं प्राणापानां यथानिलो। कुस्तस्सद्विधानेन. तृतीयस्संयमात्तयो:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12725)
- **Original**: 49 तस्य चालम्बनवतः स्थूलरूप द्विजोत्तम । आलम्बनघनत्तस्य योगिनो 5भ्यसत: स्मृतम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12726)
- **Original**: 42 अब्दादिषृनुरक्तानि निगृह्याक्षाणि योगवित्‌। कुर्याचछित्तानुकारीणि प्रत्याहारपरायण:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12727)
- **Original**: 43 वह्यता परमा तेन जायतेउतिचलात्मनाम्‌ । इन्द्रियाणामवश्यैस्तैन योगी योगसाधकः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12728)
- **Original**: 44 प्राणायामेन पथने प्रत्याहारेण चेन्द्रिये। वशीकृते ततः कुर्यात्सथित चेतइशुभाश्रये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12729)
- **Original**: 45 वह्ठ अंडा हड9 है।
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12730)
- **Original**: जिसका योग इस प्रकारके चिशिष्ट घर्मसे युक्त होता है वह मुमुक्षु योगी कहा जाता है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12731)
- **Original**: जब मुपुक्षु पहले-पहले योगाभ्यास॒ आरम्भ करता है तो उसे 'योगयुक्त योगो' कहते हैं और जब उसे परमह्मको प्राप्ति हो जाती है तो वह विनिष्पन्नसमाधि' कहलाता है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12732)
- **Original**: यदि किसी विप्रवश् उस योगयुक्त योगीका चित द्रधित हो जाता है तो जन्पान्तरमें भी उसी अध्यासको करते रहनेसे वह सुक्त हो जाता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12733)
- **Original**: विनिष्पत्रसमाधि योगी तो योगाग्रिसे कर्मसमूहके भस्म हो जानेके कारण उसो जन्ममें घोड़े ही समयपें मोक्ष प्राप्त कर लेता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12734)
- **Original**: योगीकों चाहिये कि अपने चित्तको क्रह्मचित्तनके योग्य बनाता हुआ बह्मचर्य, अहिसा, सत्य, अस्तेय और अपरिगहका निष्वग्रमभावसे सेवन करें
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12735)
- **Original**: तथा संयत चित्तसे स्वाध्याय, शौच, सत्तोष और तपक्रा आचरण करे तथा सनको निरत्तर परब्रह्ममें छूगाता रहे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12736)
- **Original**: ये पाँच-पाँच यम और नियम बतलाये गये हैं। इनका सक्म आचरण करनेसे पृथकु-पृथक्‌ फल मिलते हैं और निष्कामभाठसे सेवन करनेसे मोक्ष प्राप्त होता है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12737)
- **Original**: यतिको चाहिये कि भद्भासनादि आसनोंमेंसे किसी एकका अजललृम्बन कर यप-नियमादि गुणोंसे युक्त हो योगाध्यास करो
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12738)
- **Original**: अध्यासके द्वारा जो प्राणवायुको वहामें किया जाता है उसे 'प्राणायाम' समझता चाहिये । वह सबीज (ध्यान तथा मन्ल़पाठ आदि आलम्बनयुक्त) और निर्बॉज (निरालम्ब) भेदसे दो प्रकारका है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12739)
- **Original**: सदुरुके उपदेशसे जब योगी प्राण और अपानबायुद्रारा एक-दूसरेका निरोध करता है तो [ क्रम: रेचक और पूरक नामक ] दो प्राणायाम होते है और इन दोनोंका एक ही
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12740)
- **Original**: समय संयम करनेसे [ क़ुम्मक नामक ) तीसरा अ्राणायाम होता है
- **Translation**: 

---


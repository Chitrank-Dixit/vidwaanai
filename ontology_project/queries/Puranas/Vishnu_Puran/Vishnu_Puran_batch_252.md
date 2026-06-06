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

### Verse 1 (Vishnu Puran 0.5021)
- **Original**: 91 सप्त द्वीपानिं पाताछविधयश्ष पमहापुने । सप्तल्लोकाश्व येउन्तःस्था ब्रह्माण्डस्यास्य सर्वत:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5022)
- **Original**: 2 स्थूलात्थूलतरैशैव सर्व॑ प्राणिभिरावृतम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5023)
- **Original**: 3 अद्'ुलस्पाष्टरभागो5पि न सोउस्ति मुनिसत्तम । न सन्ति प्राणिनो यत्र कर्मबन्धनिवन्धना:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5024)
- **Original**: 4 सर्वे चैते वश यान्ति यमस्य भगवन्‌ किल । आयुषो5न्ते तथा यान्ति यातनास्तत्मचोदिता:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5025)
- **Original**: 5 यातनाभ्य: परिभ्रष्टा देवाद्यास्वथ योनिषु । जन्तव: परिवर्तन्ते झास्त्राणामेष निर्णय:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5026)
- **Original**: 6 सोहमिच्छामि तच्छूतुं यमस्य वशवर्त्तिन: । ने भव्रन्ति नरा येन तत्कर्म कथयस्व मे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5027)
- **Original**: 7 श्रीपयशर उवाच अयमेब मुने प्रश्नों नकुलेन महात्मना। पृष्ठ: पितामह: प्राह भीष्मों यत्तच्छूणुष्च मे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5028)
- **Original**: 8 भौष्प उनाच पुरा ममागतो बत्स सखा कालिडको द्विज: । स मामुबाच्र पूछो वै मया जातिस्मरों मुनि:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5029)
- **Original**: 9 तेनाख्यातमिदं सर्वमित्थे चैतद्भधविष्यति । तथा च तदभूदृत्स यथोक्ते तेन धीमता
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5030)
- **Original**: 10 स पृष्ठश्न मया भूयः श्रदधानेन वे ट्विज: । यहादाह न तददृष्टमन्‍्यथा हि मया क्रचित्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5031)
- **Original**: 11 एकदा तु मया पृष्टमेतछमद्भकतोदितिम्‌। प्राह कालिड्ल्‍डको विप्रस्स्मृत्वा तस्य मुनेर्बच:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5032)
- **Original**: 12 जातिस्मरेण कथितो रहस्य: परमो मम । यमकिड्भरयोयो5पभूत्संवादस्त॑ ब्रवीमि ते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5033)
- **Original**: 13 और सुनना चाहता हूँ, कह आप मुझसे कहिये
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5034)
- **Original**: हे महामुने ! सातों ड्रीप, सातों पाताल और सातों लोक--ये सभी स्थान जो इस ब्रह्माण्डके अत्तर्गत हैं, स्थूल, सूक्ष्म, सूक्ष्मतर, सृक्ष्मातिसूक्ष्म तथा स्थूल और स्थूकूतर जीबोंसे भरे हुए हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5035)
- **Original**: हे मुनिसत्तम ! एक अक्ललऊका आठवाँ भाग भी कोई ऐसा स्थान नहीं है जहाँ कर्म वन्‍धनसे बैंघे हुए जीव न रहते हों
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5036)
- **Original**: कितु है भगवन्‌ ! आयुके समाप्त होनेपर ये सभी यमराजके वशीभूत हो जाते हैं और उन्हींके आदेशानुसार नरक आदि नाना प्रकारकी यातनाएँ भोगते हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5037)
- **Original**: तदनन्तर पाप-भोगफे समाप्त होनेपर ले देवादि योनियोंसें घृमते रहते हैं--सकल शास्त्रोंका ऐसा ही मत है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5038)
- **Original**: अतः आप मुझे वह कर्म बताइये जिसे करनेसे मनुष्य यमराजके बशीभूत नहीं होता; मैं आपसे यही सुनना चाहता हूँ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5039)
- **Original**: श्रीपराशरजी ओल्के--हे मुने ! यही प्रश्न महात्मा नकुल्ने पितामह भीष्पसे पूछ था। उसके उत्तरमें उन्होंने जो कुछ कहा था यह सुनो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5040)
- **Original**: भीष्पजीने कहा--हे वत्स ! पूर्वकारूमें मेरे पास एक कलिज़देशीय ब्राह्मण-मित्र आया और मुझसे ओल्ज--*मेरे फूझनेपर एक जातिस्मर मुनिने जतत्त्या था कि ये सब बातें अमुक अमुक प्रकार ही होंगी ।' हे वत्स ! उस बुद्धिमानने जो-जो बातें जिस-जिस प्रकार होनेको कही थीं वे सब ज्यो-की-त्यों हुई
- **Translation**: 

---


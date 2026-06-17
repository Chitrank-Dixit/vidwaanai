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

### Verse 1 (Vishnu Puran 0.7701)
- **Original**: मनुससार
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7702)
- **Original**: ददर्श चाश्वसमवेतं प्रसेन॑ सिंहेन विनिहतम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7703)
- **Original**: अखिलूजनमध्ये सिंहपददर्शनकृतपरिशुद्धि:.. सिंहपदमनुससार
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7704)
- **Original**: ऋक्षपतिनिहर्त क्र सिंहमप्यल्पे भूमिभागे दृष्ठा ततश्र तद्ब्गौरवादृक्षस्यापि पदान्यनुययौं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7705)
- **Original**: गिरितटे क्ष सकलमेब तद्यदुसैन्यमवस्थाप्यतत्पदानुसारी ऋक्षबिले प्रविवेश
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7706)
- **Original**: अन्तःप्रविष्टआ धात्राः सुकुमारक- मुल्लालयन्त्या वाणी शुआरव ।। 41
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7707)
- **Original**: श्रीविष्णुपुराण [ अ* 13 वह मणि घतिदिन आठ भार सोना देती थी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7708)
- **Original**: उसके प्रभावसे सम्पूर्ण ग्रष्टमें रोग, अनावृष्टि तथा सर्प, अप्रि, चोर या दुर्भिक्ष आदिक्ा भय नहीं रहता था
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7709)
- **Original**: भगवान्‌ अच्युतको भी ऐसी इच्छा हुई कि यह दिव्य रत्न तो राजा उम्रसेनके योग्य है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7710)
- **Original**: किंतु जातीय विद्रोहके भयसे समर्थ होते हुए भी उन्होंने उसे छीना नहीं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7711)
- **Original**: सबाजितकों जब यह मालूम हुआ कि भगवान्‌ मुझसे यह रल माँगनेवाले हैं तो उसने लोभवश उसे अपने भाई प्रसेनको दे दिया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7712)
- **Original**: किंत्‌ इस बातकों न जानते हुए कि पत्ित्रतापूर्वक धारण करनेसे तो यह मणि सुनर्ण-दान आदि अनेक गुण प्रकट करती है और अशुद्धायस्थामें धारण करनेसे घातक हो जाती ऐ, भरोन उसे अपने गलेगें बाँधे हुए घोड़ेपर चढ़कर मृगयाक्रे लिये बनक्नों चला गया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7713)
- **Original**: वहाँ उसे एक सिंहने मार डाला
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7714)
- **Original**: जब वह सिंह घोड़ेके सहित उसे मारकर हस निर्मत्त मणिक्रो अपने गुँहों झेकर चलनेको तैयार हुआ तो उसी समय ऋक्षराज जाम्बवानने उसे देखकर मार डाला
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7715)
- **Original**: तदनन्तर उस निर्मक मणिरत्रकों लेकर जाम्बवान्‌ू अपनो गुफामें आया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7716)
- **Original**: और उसे सुकुमार नामक अपने यालकके लिये खिलौना बना लिया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7717)
- **Original**: प्रसेनके न ल्ैटनेपर सब यादबोंगें आपसमें यह कानाफुँसी होने लगी कि “कृष्ण इस मणिरत्रकों लेना चाहते थे, अवश्य हो इन्हींने उसे ले लिया है--निश्चय यह इन्हींका काम है''
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7718)
- **Original**: इस ल्त्रेकप्रपवादक्या पता लगनेपर सम्पूर्ण यादवसेनाके सहित भगवानने प्रसेके घोड़ेके चरण चिह्रोंक्ा अनुसरण किया और आगे जाकर देखा कि प्रसेनकों घोड़ेसहित सिंहने मार डात्मा है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7719)
- **Original**: फिर सब ल्लोगोंके बीच सिंहके चरण-चिह्न देख लिये जानेसे अपनी सफाई हो जानेपर भी भगवानने ठन चिह्लॉका अनुसरण किया और थोड़ी ही दुरीपर ऋ्क्षराजद्वारा मारे हुए सिंहको देखा; किन्तु उस रलके महत्त्वके कारण उन्होंने जाम्बबानंके पद-चिह्लॉंका भी अनुसरण किया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7720)
- **Original**: और सम्पूर्ण यादल-सेनाको पर्वतके तटपर छोड़कर ऋक्षराजके चरणॉंका अनुसरण करते हुए स्वयं उनकी गुफामें खुस गये
- **Translation**: 

---


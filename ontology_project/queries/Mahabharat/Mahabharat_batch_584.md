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

### Verse 1 (Mahabharat 0.5831)
- **Original**: सोमदत्त, सैकड़ों सृक्षयवीर, राजा क्षेमभन्वा, विराट, दुपद, विधिवत्‌ दाह करा दोगे ? इनमें अनेकों ऐसे होंगे जो न तो
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5831)
- **Original**: सोमदत्त, सैकड़ों सृक्षयवीर, राजा क्षेमभन्वा, विराट, दुपद, विधिवत्‌ दाह करा दोगे ? इनमें अनेकों ऐसे होंगे जो न तो
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5832)
- **Original**: शिखण्डी, धृष्टशुप्र, युधामनन्‍्यु, उत्तरौजा, कोसलराज, अभिकोत्री रहे होंगे और न उनका संस्कार करनेवाला ही कोई
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5832)
- **Original**: शिखण्डी, धृष्टशुप्र, युधामनन्‍्यु, उत्तरौजा, कोसलराज, अभिकोत्री रहे होंगे और न उनका संस्कार करनेवाला ही कोई
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5833)
- **Original**: ब्रैपदीके पुत्र, झकुनि, अचल, वृषक, भगदत्त, कर्ण, कर्णके होगा। भैया ! यहाँ तो बहुतोंके अन्वेष्टिकर्म करने हैं, हम
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5833)
- **Original**: ब्रैपदीके पुत्र, झकुनि, अचल, वृषक, भगदत्त, कर्ण, कर्णके होगा। भैया ! यहाँ तो बहुतोंके अन्वेष्टिकर्म करने हैं, हम
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5834)
- **Original**: पुत्र, केकयराज, त्रिगर्तराज, घटोत्कथ, अल्म्युथ और किस-किसका को ? जलसख--इन सबका तथा और भी हजारों राजाओंका राजा धृतराष्ट्रके ऐसा कहनेपर कुन्तीनन्दन युथ्िष्ठिरने
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5834)
- **Original**: पुत्र, केकयराज, त्रिगर्तराज, घटोत्कथ, अल्म्युथ और किस-किसका को ? जलसख--इन सबका तथा और भी हजारों राजाओंका राजा धृतराष्ट्रके ऐसा कहनेपर कुन्तीनन्दन युथ्िष्ठिरने
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5835)
- **Original**: उन्होंने घ्तकी धाराओंसे प्रज्वल्ति हुई अभिमें दाह कराया। क्रैरवोंके पुरोहित सुधर्मा और अपने पुरोहित धौम्यको तथा
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5835)
- **Original**: उन्होंने घ्तकी धाराओंसे प्रज्वल्ति हुई अभिमें दाह कराया। क्रैरवोंके पुरोहित सुधर्मा और अपने पुरोहित धौम्यको तथा
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5836)
- **Original**: किन्हीं-किन्हींके लिये श्राद्धकर्म भी कराये गये, किन्हींके सक्षय, बिदुर, युयुत्सु, इद्रसेन आदि सेवक और सब
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5836)
- **Original**: किन्हीं-किन्हींके लिये श्राद्धकर्म भी कराये गये, किन्हींके सक्षय, बिदुर, युयुत्सु, इद्रसेन आदि सेवक और सब
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5837)
- **Original**: लिये सामगान कराया गया और किन्हींके लिये उनके सारथियोंको आज्ञा दी कि 'आपत्मेग विधिपूर्वक इन सभीके
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5837)
- **Original**: लिये सामगान कराया गया और किन्हींके लिये उनके सारथियोंको आज्ञा दी कि 'आपत्मेग विधिपूर्वक इन सभीके
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5838)
- **Original**: सम्बन्धियोंको बहुत झोक भी हुआ । उस रात्रिमें सामगानकी ज्तकर्म कराइये, जिससे कोई भी झारीर अनाथकी तरह नह
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5838)
- **Original**: सम्बन्धियोंको बहुत झोक भी हुआ । उस रात्रिमें सामगानकी ज्तकर्म कराइये, जिससे कोई भी झारीर अनाथकी तरह नह
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5839)
- **Original**: ध्यनि और खियोंके रूदनसे सभी जीवोंकों बड़ा कष्ट हुआ। न हो।' धर्मराजकी आज्ञा पाते ही ये सब स्मेग चन्दन, अगर,
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5839)
- **Original**: ध्यनि और खियोंके रूदनसे सभी जीवोंकों बड़ा कष्ट हुआ। न हो।' धर्मराजकी आज्ञा पाते ही ये सब स्मेग चन्दन, अगर,
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5840)
- **Original**: इसके बाद बहाँ अनेकों देझोंसे आये हुए जो अनाथ लोग मारे काझ्ठ, घी, तेल, सुगन्धित द्रव्य और रेशमी बस्तर आदि सब
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5840)
- **Original**: इसके बाद बहाँ अनेकों देझोंसे आये हुए जो अनाथ लोग मारे काझ्ठ, घी, तेल, सुगन्धित द्रव्य और रेशमी बस्तर आदि सब
- **Translation**: 

---


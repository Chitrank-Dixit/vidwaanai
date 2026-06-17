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

### Verse 1 (Vishnu Puran 0.8661)
- **Original**: इसके पीछे तेरह इनके बवेशके और तीन ब्राक्कक राजा होंगे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8662)
- **Original**: उनके बाद तेरह पुष्पमिन्न और पठुमित्र आदि तथा सात आज भाण्डलिक भूपत्तिगण होंगे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8663)
- **Original**: तथा नौ राजा क्रमशः कोसलदेइामें राज्य वरेंगे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8664)
- **Original**: निषश्रदेशके स्वामी भी ये ही होंगे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8665)
- **Original**: मगधदेशामें विश्वस्फटिक नामक राजा अन्य वर्णोकरो प्रवृत्त करेगा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8666)
- **Original**: यह कैमर्त्त, बढ़, पुलिन्द और ब्राह्मणोंको राज्यगें नियुक्त करेगा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8667)
- **Original**: सम्पूण क्षत्रिय-जातिको उनच्छिन्न कर पद्मावतीपुरीमें ठागगण तथा गंगाके निकटबर्ती प्रयाग और गयामें मागध और गुप्त राजालोग राज्य भोग करेंगे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8668)
- **Original**: कोसल, आन्म, पुण्डू, ताग्रलिप्त और समुद्रतटवर्तिनी पुरीकी देवरद्षित नामक एक राजा रक्षा कोगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8669)
- **Original**: कलिज्ज, माहिष, महेखद और भौसम आदि देशॉको गुह नरेश भोगेंगे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8670)
- **Original**: नैषध, नेमिषक और कालको शक आदि जनपदोंको मणि- धान्यक-वंशीय राजा भोगेंगे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8671)
- **Original**: त्रैराज्य और मुषिक देशॉपर क्नक नामक राजाका राज्य होगा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8672)
- **Original**: सौराष्ट्र, अबन्ति, शूद्र, आभीर तथा नर्मदा-तटबर्ती मरुभूमिपर ब्रात्य द्विज, आभीर और झुद्र आदिका आधिपत्य होगा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8673)
- **Original**: समुद्रतट, दालिकोर्तो, चन्द्रभागा और जाध्मीर आदि देशॉका व्रात्य, म्लेच्छ और शूद्र आदि राजागण भोग करेंगे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8674)
- **Original**: थे सम्पूर्ण राजालोग पृथियोमें एक ही सपयमें होंगे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8675)
- **Original**: ये थोड़ी पसन्नतावाले, अत्यन्त क्रोधो, सर्वदा अधर्म और मिथ्या भाषणमें रुचि रखनेताक्े, स्ती-बालक और गौओऑँंको हत्या करनेवाले, पर-धन-हरणमें रुंच रखनेबालछे, अल्पशक्ति तमःप्रधान उत्थानके साथ ही पतनश्ञीक, अल्पायु, महती कामनाबाले, अल्पपुण्य और अत्यत्त व्तेभी होंगे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8676)
- **Original**: ये सम्पूर्ण देशॉको परस्पर मिला देंगे तथा उन राजाओंके आश्रयसे ही खलखान्‌ और उन्हींकि स्वभावका अनुकरण करनेवाले म्लेच्छ तथा आर्यविपरीत आचरण करते हुए सारी प्रजाकों नष्ट प्रष्ट कर देंगे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8677)
- **Original**: अ0 24 )] ततश्चानुदिनमल्पाल्पह्वासव्यकच्छेदाद्धर्मार्थयो - ज॑गतस्सड्डयो. भविष्यति
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8678)
- **Original**: ततश्नार्थ एवाभिजनहेतु:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8679)
- **Original**: बलमेवाहोषधर्महितु
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8680)
- **Original**: अभिरुच्तिरिव दाम्पत्यसम्बन्धहेतु
- **Translation**: 

---


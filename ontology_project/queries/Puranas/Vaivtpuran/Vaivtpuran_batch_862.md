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

### Verse 1 (Vaivtpuran 543.15554)
- **Original**: महापापी कहलाते हैं। इन्हें हजारों वर्षोतक है तथा सोना दान करनेसे शुद्ध हो जाता है।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15555)
- **Original**: कुम्भीपाकमें रहना पड़ता है। वहाँ वे रात-दिन भ्रूणहत्या करनेवाला महापापी शुनीमुख नामक
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15556)
- **Original**: खौलते हुए तेलसे संतप्त किये जाते हैं, उन्हें नरकमें जाता है। बहाँ वह सौ बर्षोतक सूक्ष्म
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15557)
- **Original**: व्याधियाँ घेरे रहती हैं और सर्पाकार जन्तु काटता शस्त्रद्वारा पीड़ित किया जाता है। फिर उसे निश्चय
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15558)
- **Original**: रहता है। तदनन्तर वह पापी हजार करोड़ ही सौ वर्षोतक घोड़ेकी योनिमें जन्म लेना पड़ता
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15559)
- **Original**: जन्मोंतक गोध, सौ जन्मोंतक सूअर और सौ है। इसके बाद वह पापी अपने कर्मके फलस्वरूप । जन्मोंतक हिंसक पशु होनेके बाद रोगग्रस्त शूद्र दादके रोगसे युक्त वैश्य होता है और पचास होता है। उस जन्ममें बह मन्दाग्नि तथा ज्वरसे वर्षोंतक वह कष्ट भोगकर पुन: स्वर्णदानसे शुद्ध
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15560)
- **Original**: पीड़ित रहता है तथा सौ पल सोना दान करके होता है। इसके बाद अपने कुलमें उत्पन्न होनेपर । अवश्य ही शुद्ध हो जाता है। चारों वर्णोमें जो भी वह नीरोग होता है और फिर पवित्र ब्राह्मण मनुष्य वस्त्र चुरानेवाला, गव्य (दूध-दही-घी)- होकर जन्म लेता है। युद्धके बिना क्षत्रियको
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15561)
- **Original**: की चोरी करनेवाला, चाँदी और मुक्ताका अपहरण मारनेवाला ब्राह्मण अथवा क्षत्रिय तप्तशूल नरकमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15562)
- **Original**: करनेवाला तथा शूद्रके धनको लूट लेनेबवाला होता जाता है। वहाँ उसे एक हजार वर्षतक तपाये
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15563)
- **Original**: है; वह सौ वर्षोतक मृत्रकुण्डका भोग करके पुनः हुए लोहेसे काढेको भाँति पकाया जाता है और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15564)
- **Original**: हजार वर्षोतक बगुलेकी योनिमें उत्पन्न होता वह आर्तनाद करता है। तदनन्तर वह सौ वर्षोंतक
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15565)
- **Original**: है--वह ध्रुव है। व्रजराज! तदनन्तर वह सौ मदमत्त गजराज होता है। इसके बाद सौ वर्षोंतक
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15566)
- **Original**: वर्षोतक शुद्रजातिमें जन्म लेता है। वहाँ वह पापी रक्तदोषयुक्त शूद्र होता है। वहाँ वह हाथी दान
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15567)
- **Original**: कुष्टरोगसे युक्त होता है और उसके घावसे मवाद करनेसे रोगमुक्त होकर फिर ब्राह्मणके घरमें जन्म
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15568)
- **Original**: निकलती रहती है। तत्पश्चात्‌ थोड़ा-बहुत कोढ़से लेता है। वैश्य और शूद्रकी हत्या करनेवाला वैश्य
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15569)
- **Original**: युक्त होकर ब्राह्मण होता है और छ: पल सोना तथा वैश्यकी हिंसा करनेवाला शुद्र-ये निश्चय
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15570)
- **Original**: दान करनेसे पवित्र होकर रोगमुक्त हो जाता है। ही समान पापके भागी होते हैं। इन्हें सौ वर्षोतक
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15571)
- **Original**: जो खजाना लूटनेवाला, फल चुरानेवाला तथा कृमिकुण्ड नामक नरकमें वास करना पड़ता है।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15572)
- **Original**: खेल-ही-खेलमें धनका अपहरण करनेवाला है, वहाँ कीड़ोंके काटनेसे वह महान्‌ दुःखी होता वह भूतलपर यक्ष होता है। फिर सौ वर्षोतक है। इसके बाद वह कृमिरोगसे युक्त होकर सौ
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15573)
- **Original**: नीलकण्ठ पक्षी होता है। तत्पश्चात्‌ भारतभूमिपर वर्षोंतक किरात होता है। ब्रजेश्वर! तदनन्तर वह
- **Translation**: 

---


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

### Verse 1 (Mahabharat 0.2831)
- **Original**: और कवच नष्ट हो गये हों--ऐसे निहत्थोंका वध न किया सावधान करके प्रहार किया जाय। जो प्रहार न होनेका
- **Translation**: 

---

### Verse 2 (Mahabharat 0.2831)
- **Original**: और कवच नष्ट हो गये हों--ऐसे निहत्थोंका वध न किया सावधान करके प्रहार किया जाय। जो प्रहार न होनेका
- **Translation**: 

---

### Verse 3 (Mahabharat 0.2832)
- **Original**: जाय। सूत, भार ढोनेवाले, झख्र पहुँचानेवाले तथा धेरी और विश्वास करके बेखबर हो अथवा भयभीत हो, उसपर आघात
- **Translation**: 

---

### Verse 4 (Mahabharat 0.2832)
- **Original**: जाय। सूत, भार ढोनेवाले, झख्र पहुँचानेवाले तथा धेरी और विश्वास करके बेखबर हो अथवा भयभीत हो, उसपर आघात
- **Translation**: 

---

### Verse 5 (Mahabharat 0.2833)
- **Original**: झद्भू बजानेवाल्मेंपर भी किसी तरह प्रहार न किया जाय ।' न किया जाय। जो किसी एकके साथ युद्ध कर रहा हो,
- **Translation**: 

---

### Verse 6 (Mahabharat 0.2833)
- **Original**: झद्भू बजानेवाल्मेंपर भी किसी तरह प्रहार न किया जाय ।' न किया जाय। जो किसी एकके साथ युद्ध कर रहा हो,
- **Translation**: 

---

### Verse 7 (Mahabharat 0.2834)
- **Original**: इस प्रकास्के नियम बनाकर जे सभी राजालोग अपने उसपर दूसरा कोई शस्त्र न छोड़े। जो झरणमें आया हो
- **Translation**: 

---

### Verse 8 (Mahabharat 0.2834)
- **Original**: इस प्रकास्के नियम बनाकर जे सभी राजालोग अपने उसपर दूसरा कोई शस्त्र न छोड़े। जो झरणमें आया हो
- **Translation**: 

---

### Verse 9 (Mahabharat 0.2835)
- **Original**: सैनिकॉंके साथ बहुत प्रसन्न हुए। कफज्ओ व्यासजीद्वारा सज्ञयकी नियुक्ति तथा अनिष्टसूचक उत्पातोंका वर्णन वैज्मम्पायलजीने कह्ा--राजन्‌ ! तदन्तर पूर्व और पश्चिम
- **Translation**: 

---

### Verse 10 (Mahabharat 0.2835)
- **Original**: सैनिकॉंके साथ बहुत प्रसन्न हुए। कफज्ओ व्यासजीद्वारा सज्ञयकी नियुक्ति तथा अनिष्टसूचक उत्पातोंका वर्णन वैज्मम्पायलजीने कह्ा--राजन्‌ ! तदन्तर पूर्व और पश्चिम
- **Translation**: 

---

### Verse 11 (Mahabharat 0.2836)
- **Original**: हो या परोक्षमें; दिनमें हो या रातमें, अथवा मनमें सोची हुई दिज्ञामें आमने-सामने खड़ी हुई दोनों ओरकी सेनाओंको
- **Translation**: 

---

### Verse 12 (Mahabharat 0.2836)
- **Original**: हो या परोक्षमें; दिनमें हो या रातमें, अथवा मनमें सोची हुई दिज्ञामें आमने-सामने खड़ी हुई दोनों ओरकी सेनाओंको
- **Translation**: 

---

### Verse 13 (Mahabharat 0.2837)
- **Original**: ही क्‍यों न हो, वह बात भी सक्षयको मालूम हो जायगी। इसे देखकर भूत, भविष्य और वर्तमात--तीनों काल्मेंका ज्ञान
- **Translation**: 

---

### Verse 14 (Mahabharat 0.2837)
- **Original**: ही क्‍यों न हो, वह बात भी सक्षयको मालूम हो जायगी। इसे देखकर भूत, भविष्य और वर्तमात--तीनों काल्मेंका ज्ञान
- **Translation**: 

---

### Verse 15 (Mahabharat 0.2838)
- **Original**: झख््र नहीं काट सकेंगे, परिश्रम कष्ट नहीं पहुँचा सकेगा तथा रखनेवाले भगवान्‌ व्यासने एकान्तमें बैठे हुए राजा धृतराष्ट्रके
- **Translation**: 

---

### Verse 16 (Mahabharat 0.2838)
- **Original**: झख््र नहीं काट सकेंगे, परिश्रम कष्ट नहीं पहुँचा सकेगा तथा रखनेवाले भगवान्‌ व्यासने एकान्तमें बैठे हुए राजा धृतराष्ट्रके
- **Translation**: 

---

### Verse 17 (Mahabharat 0.2839)
- **Original**: यह इस युद्धसे जीता-जागता निकल आयेगा । मैं इन कौरवों पास आकर कहा, “राजन! तुम्हारे पुत्रों तथा अन्य
- **Translation**: 

---

### Verse 18 (Mahabharat 0.2839)
- **Original**: यह इस युद्धसे जीता-जागता निकल आयेगा । मैं इन कौरवों पास आकर कहा, “राजन! तुम्हारे पुत्रों तथा अन्य
- **Translation**: 

---

### Verse 19 (Mahabharat 0.2840)
- **Original**: और पाण्डवोंकी कीर्तिका जिस्तार करूँगा, तुप इनके लिये की 8 ग्र्ह्च्् 9
- **Translation**: 

---

### Verse 20 (Mahabharat 0.2840)
- **Original**: और पाण्डवोंकी कीर्तिका जिस्तार करूँगा, तुप इनके लिये की 8 ग्र्ह्च्् 9
- **Translation**: 

---


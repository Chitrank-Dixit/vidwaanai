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

### Verse 1 (Bramha 0.3001)
- **Original**: फलका भागी होता है। गड्जा देवी सर्वत्र हैं, सर्वभूतस्वरूपा हैं, सब
- **Translation**: 

---

### Verse 2 (Bramha 0.3002)
- **Original**: गौतम! गोदावरी नदीमें दो-दो हाथ भूमिपर पापॉंका नाश करनेबाली तथा सम्पूर्ण अभीष्ट
- **Translation**: 

---

### Verse 3 (Bramha 0.3003)
- **Original**: तीर्थ होंगे। उनमें मैं स्वयं सर्वत्र रहकर सबकी वस्तुओंको देनेवाली हैं। वेदमें सदा उन्होंके ' समस्त कामनाओंको पूर्ण करता रहूँगा। सरिताओंमें यशका गान किया जाता है। जिनकी बुद्धि
- **Translation**: 

---

### Verse 4 (Bramha 0.3004)
- **Original**: श्रेष्ठ नर्मदा अमरकण्टकपर्व॑तपर अधिक उत्तम अज्ञानसे मोहित है, बे मर्त्यलोकके निवासी मानो गयी हैं। यमुनाका विशेष महत्त्व उस समझते हैं कि गड्भा केवल मर्त्यलोकमें हो हैं,
- **Translation**: 

---

### Verse 5 (Bramha 0.3005)
- **Original**: स्थानपर है, जहाँ वे गज्जासे मिली हैं। सरस्वती पाताल अथवा स्वर्गमें नहीं हैं। भगवती गड्जा . नदी प्रभासतीर्थमें श्रेष्ठ बतायी गयी हैं। तृष्णा,
- **Translation**: 

---

### Verse 6 (Bramha 0.3006)
- **Original**: 146 * संक्षिम ब्रह्मपुराण « भीमरथी और तुद्नभद्रा-इन तीन नदियोंका जहाँ
- **Translation**: 

---

### Verse 7 (Bramha 0.3007)
- **Original**: मुझे सदा ही प्रिय हैं। वे स्मरणमात्रसे पाप- समागम हुआ है, वह तीर्थ मनुष्योंको मुक्ति
- **Translation**: 

---

### Verse 8 (Bramha 0.3008)
- **Original**: राशिका बिनाश करनेवाली हैं। पाँचों भूतोंमें जल देनेवाला है। इसी प्रकार पयोणष्णी नदी भी जहाँ
- **Translation**: 

---

### Verse 9 (Bramha 0.3009)
- **Original**: श्रेष्ठ है! जलमें भी जो तीर्थका जल है, बह तपती (ताप्ती) में मिली हैं, बह तीर्थ मोक्षदायक
- **Translation**: 

---

### Verse 10 (Bramha 0.3010)
- **Original**: सर्वश्रेष्ठ माना गया है। तीर्थ-जलमें भी भागीरथी है; परंतु ये गौतमी गड्जा मेरी आज्ञासे सर्वत्र सर्वदा
- **Translation**: 

---

### Verse 11 (Bramha 0.3011)
- **Original**: गड्जा श्रेष्ठ हैँ और उनसे भी गौतमी गद्जा उत्कृष्ट और सब मभनुष्योंको स्नान करनेपर मोक्ष प्रदान
- **Translation**: 

---

### Verse 12 (Bramha 0.3012)
- **Original**: मानी गयी हैं; क्योंकि वे भगवान्‌ शंकरकी करेंगी। कोई-कोई तोर्थ किसी विशेष समयमें
- **Translation**: 

---

### Verse 13 (Bramha 0.3013)
- **Original**: जटाके साथ लायी गयी थीं। अत: इनसे बढ़कर देवताका शुभागमन होनेपर अधिक पुण्यमय माना
- **Translation**: 

---

### Verse 14 (Bramha 0.3014)
- **Original**: कल्याणकारी तीर्थ दूसरा कोई नहीं है। मुने! जाता है, किंतु गोदावरी नदी सदा ही सबके लिये
- **Translation**: 

---

### Verse 15 (Bramha 0.3015)
- **Original**: स्वर्ग, पृथ्वी और पातालमें भी गज्ला सब मनोरथोंको तीर्थ है। मुनिश्रेष्ठ
- **Translation**: 

---

### Verse 16 (Bramha 0.3016)
- **Original**: दो सौ योजनके भीतर गोदाबरी
- **Translation**: 

---

### Verse 17 (Bramha 0.3017)
- **Original**: पूर्ण करनेबाली हैं। नदीमें साढ़े तीन करोड़ तीर्थ होंगे। ये गड्डा,. ब्रह्माजी कहते हैं--नारद! इस प्रकार साक्षात्‌ निम्नाक्वित नामोंसे प्रसिद्ध होंगी-माहेश्वरी, गड्ना,
- **Translation**: 

---

### Verse 18 (Bramha 0.3018)
- **Original**: भगवान्‌ शंकरने संतुष्ट होकर महात्मा गौतमको गौतमी, बैष्णवी, गोदावे, नन्‍्दा, सुनन्दा, कामदायिनी,
- **Translation**: 

---

### Verse 19 (Bramha 0.3019)
- **Original**: गोदाबरीका जो माहात्म्य बतलाया था। वहीं मैंने ब्रह्मतेज :समानीता तथा सर्वपापप्रणाशिनी
- **Translation**: 

---

### Verse 20 (Bramha 0.3020)
- **Original**: गोदावरी
- **Translation**: 

---


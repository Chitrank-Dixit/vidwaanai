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

### Verse 1 (Vaivtpuran 3.225)
- **Original**: आभरणोंसे विभूषित थीं। निद्रा, तृष्णा, श्षुथा, भगवान्‌कों प्रणाम किया और सफलमनोरथ हो
- **Translation**: 

---

### Verse 2 (Vaivtpuran 3.226)
- **Original**: पिपासा, दया, श्रद्धा और क्षमा आदि जो देवियाँ उनकी आज्ञासे वे श्रेष्ठ रत्रमय सिंहासनपर बैठों।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 3.227)
- **Original**: हैं, उन सबकी तथा समस्त शक्तियोंकी वे ईश्वरी जो प्रातःकाल उठकर वाणीद्वारा किये गये इस
- **Translation**: 

---

### Verse 4 (Vaivtpuran 3.228)
- **Original**: और अधिष्ठात्री देवी हैं। उनके सौ भुजाएँ हैं। स्तोत्रका पाठ करता है, वह सदा बुद्धिमान,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 3.229)
- **Original**: वे दर्शनमात्रसे भय उत्पन्न करती हैं। उन्हींको धनवान, विद्वान्‌ और पुत्रवान्‌ होता है। दुर्गतिनाशिनी दुर्गा कहा गया है। वे परमात्मा सौति कहते हैं--तत्पश्चात्‌ परमात्मा श्रीकृष्णके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 3.230)
- **Original**: श्रीकृष्णकी शक्तिरूपा तथा तीनों लोकोंकी परा मनसे एक गौरवर्णा देवी प्रकट हुईं, जो रत्नमय
- **Translation**: 

---

### Verse 7 (Vaivtpuran 3.231)
- **Original**: जननी हैं। त्रिशूल, शक्ति, शार्ड्र धनुष, खड्‌्ग, बाण, अलंकारोंसे अलंकृत थीं। उनके श्रीअज्ञोंपर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 3.232)
- **Original**: शद्गु, चक्र, गदा, पद्म, अक्षमाला, कमण्डलु, बज्र, पीताध्बरकी साड़ी शोभा पा रही थी। मुखपर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 3.233)
- **Original**: अड्जुश, पाश, भुशुण्डि, दण्ड, तोमर, नारायणास्त्र, मन्द हास्यकी छटा छा रही थी। वे नवयौवना
- **Translation**: 

---

### Verse 10 (Vaivtpuran 3.234)
- **Original**: त्रह्मास्त्र, रौद्रास्त्र, पाशुपतास्त्र, पार्जन्यास्त्र, वारुणास्त्र, देवी सम्पूर्ण ऐश्वर्योंकी अधिष्ठात्री थीं। वे ही
- **Translation**: 

---

### Verse 11 (Vaivtpuran 3.235)
- **Original**: आप्रेयास्त्र तथा गान्धर्वास्त्र--इन सबको हाथोंमें फलरूपसे सम्पूर्ण सम्पत्तियाँ प्रदान करती हैं।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 3.236)
- **Original**: धारण किये श्रीकृष्णके सामने खड़ी हो, प्रकृति स्वर्गलोकमें उन्होंको स्वर्गलक्ष्मी कहते हैं तथा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 3.237)
- **Original**: देबीने प्रसन्नतापूर्वक्क उनका स्तवन किया। राजाओंके यहाँ वे ही राजलक्ष्मी कहलाती हैं।। प्रकृति बोलीं--प्रभो! मैं प्रकृति, ईश्वरी, श्रीहरिके सामने खड़ी होकर उन साध्वी लक्ष्मीने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 3.238)
- **Original**: सर्वेश्वरी, सर्वस्पपिणी और सर्वशक्तिस्वरूपा कहलाती उन्हें हाथ जोड़कर प्रणाम किया। उनकी ग्रीवा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 3.239)
- **Original**: हूँ। मेरी शक्तिसे हो यह जगत्‌ शक्तिमान्‌ है तथापि भक्तिभावसे झुक गयी और उन्होंने उन परमात्मा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 3.240)
- **Original**: मैं स्वतन्त्र नहीं हूँ; क्योंकि आपने मेरी सृष्टि भगवान्‌ श्रीकृष्फा स्तवत किया। की है, अत: आप ही तीनों लोकोंके पति, गति, महालक्ष्मी बोलीं--'जो सत्यस्वरूप, सत्यके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 3.241)
- **Original**: पालक, स्रष्टा, संहारक तथा पुनः सृष्टि करनेवाले स्वामी और सत्यके बीज हैं, सत्यके आधार,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 3.242)
- **Original**: हैं। परमानन्द ही आपका स्वरूप है। मैं सानन्द सत्यके ज्ञाता तथा सत्यके मूल हैं, उन सनातन
- **Translation**: 

---

### Verse 19 (Vaivtpuran 3.243)
- **Original**: आपकी बन्दना करती हूँ। प्रभो! आप चाहें तो देव श्रीकृष्णको मैं प्रणाम करती हूँ।' पलक मारते-मारते ब्रह्माका भी पतन हो सकता यों कह श्रीहरिको मस्तक नवाकर तपाये
- **Translation**: 

---

### Verse 20 (Vaivtpuran 3.244)
- **Original**: है। जो भ्रूभड़की लीलामात्रसे करोड़ों विष्णुओंकी हुए सुवर्णकी-सी कान्तिवाली लक्ष्मीदेवी दसों
- **Translation**: 

---


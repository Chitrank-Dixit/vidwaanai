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

### Verse 1 (Nard Puran 0.741)
- **Original**: हैं--इन तीनों प्रश्नोंक विषयमें मेरा मत सुनो। ऋभु बोले--ब्रह्मनू! इन सबमें मेरी रुचि
- **Translation**: 

---

### Verse 2 (Nard Puran 0.742)
- **Original**: आत्मा सबमें व्याप्त है। यह आकाशको भाँति नहीं है। मुझे तो मीठा अन्न दो। हलुआ, खीर और
- **Translation**: 

---

### Verse 3 (Nard Puran 0.743)
- **Original**: सर्वव्यापक है, अत: इसके विषयमें कहाँसे आये, खाँडके बने हुए पदार्थ भोजन कराओ। कहाँ रहते हैं और कहाँ जायँंगे-यह प्रश्न कैसे निदाघने अपनी स्त्रीसे कहा--शोभने ! हमारे
- **Translation**: 

---

### Verse 4 (Nard Puran 0.744)
- **Original**: सार्थक हों सकता है ? इसलिये मैं न जानेबाला हूँ घस्में जो अच्छी-से-अच्छी भोजन-सामग्री उपलब्ध
- **Translation**: 

---

### Verse 5 (Nard Puran 0.745)
- **Original**: और न आनेवाला। (तू, मैं और अन्यका भेद भी हो, उसके द्वारा इन अतिथि-देवताके लिये मिष्टान्च
- **Translation**: 

---

### Verse 6 (Nard Puran 0.746)
- **Original**: शरीरकों लेकर हो है) वास्तवमें न तू तू है, न बनाओ। अन्य अन्य है और न मैं मैं हूँ (केवल विशुद्ध पतिके ऐसा कहनेपर ब्राह्मणपत्लीने स्वामीकी
- **Translation**: 

---

### Verse 7 (Nard Puran 0.747)
- **Original**: आत्मा ही सर्वत्र विराजमान है)। इसी प्रकार आज्ञाका आदर करते हुए ब्राह्मण देवताके लिये
- **Translation**: 

---

### Verse 8 (Nard Puran 0.748)
- **Original**: मीठा भी मीठा नहीं है। मैंने जो तुमसे मिष्टान्नके मोठा भोजन तैयार किया। राजन्‌ ! महामुनि ऋभुके
- **Translation**: 

---

### Verse 9 (Nard Puran 0.749)
- **Original**: लिये पूछा था उसमें भी मेरा यहो भाव था कि इच्छानुसार मिष्टान्न भोजन कर लेनेपर निदाघने
- **Translation**: 

---

### Verse 10 (Nard Puran 0.750)
- **Original**: देखूँ, ये क्‍या कहते हैं। द्विजश्रेष्ठ ! इस विषयमें मेरा विनोतभावसे खड़े होकर पूछा। विचार सुनो। मीठा अन्न भी तृप्त हो जानेके बाद निदाघ बोले--ब्रह्मन ! कहिये, भोजनसे आपको
- **Translation**: 

---

### Verse 11 (Nard Puran 0.751)
- **Original**: मीठा नहीं लगता तो बही उद्वेगजनक हो जाता है। भलीभाँति तृप्ति हुई ? आप संतुष्ट हो गये न? अब
- **Translation**: 

---

### Verse 12 (Nard Puran 0.752)
- **Original**: कभी-कभी जो मीठा नहीं है, वह भी मीठा आपका चित्त पूर्णतः स्वस्थ है न? विप्रवर! आप
- **Translation**: 

---

### Verse 13 (Nard Puran 0.753)
- **Original**: लगता है अर्थात्‌ अधिक भूख होनेपर फीका अन्न कहाँके रहनेवाले हैं, कहाँ जानेको उद्यत हैं और
- **Translation**: 

---

### Verse 14 (Nard Puran 0.754)
- **Original**: भी मीठा (अमृतके समान) लगता है। ऐसा कहाँसे आपका आगमन हुआ है ? यह सब बताइये।
- **Translation**: 

---

### Verse 15 (Nard Puran 0.755)
- **Original**: कौन-सा अन्न है, जो आदि, मध्य और अन्त-तीनों ऋभुने कहा--ब्रह्मन्‌! जिसे भूख लगती है,
- **Translation**: 

---

### Verse 16 (Nard Puran 0.756)
- **Original**: कालमें रुचिकर ही हो। जैसे मिट्टीका घर उसीको अन्न भोजन करनेपर तृप्ति भी होती है।
- **Translation**: 

---

### Verse 17 (Nard Puran 0.757)
- **Original**: मिट्टीसे लिपनेपर स्थिर होता है, उसी प्रकार यह मुझे तो न कभी भूख लगी और न तृप्ति हुईं। फिर
- **Translation**: 

---

### Verse 18 (Nard Puran 0.758)
- **Original**: पार्थिव शरीर पार्थिव परमाणुओंसे पुष्ट होता है। मुझसे क्‍यों पूछते हो? जठराग्रिसे पार्थिव धातु
- **Translation**: 

---

### Verse 19 (Nard Puran 0.759)
- **Original**: जौ, गेहूँ, मूँग, घी, तेल, दूध, दही, गुड़ और (पहलेके खाये हुए पदार्थ)-के पच्र जानेपर
- **Translation**: 

---

### Verse 20 (Nard Puran 0.760)
- **Original**: फल आदि सभी भोज्य-पदार्थ पार्थिव परमाणु ही क्षुधाकी प्रतीति होती है। इसी प्रकार पिये हुए
- **Translation**: 

---


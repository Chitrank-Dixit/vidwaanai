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

### Verse 1 (Vaivtpuran 22.6919)
- **Original**: करोगे और आगे कहे जानेवाले स्तोत्रसे उनकी श्रीहरिने प्रसन्न हो इन्द्रको यह कबच देनेके पश्चात्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 22.6920)
- **Original**: स्तुति करके सिर झुकाओगे, तब उनसे वरदान पुनः जगत्‌की हित-कामनासे कृषापूर्वक उन्हें [पाकर तुम दुःखसे मुक्त हो जाओगे। देवराज! 30 हीं श्रीं क्लीं नमो महालक्ष्म्यै हरिप्रियायै
- **Translation**: 

---

### Verse 3 (Vaivtpuran 22.6921)
- **Original**: महालक्ष्मीका वह सुखप्रद स्तोत्र, जो परम गोपनीय स्वाहा' यह घोडशाक्षर-मन्त्र भी प्रदान किया।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 22.6922)
- **Original**: तथा त्रिलोकीमें दुर्लभ है, बतलाता हूँ। सुनो। फिर जो गोपनीय, परम दुर्लभ, सिद्धों और
- **Translation**: 

---

### Verse 5 (Vaivtpuran 22.6923)
- **Original**: नारायण कहते हैं--देवि! जिनका स्तवन मुनिबरोंद्वारा दुष्प्रप्प और निश्चितरूपसे सिद्धिप्रद
- **Translation**: 

---

### Verse 6 (Vaivtpuran 22.6924)
- **Original**: करनेमें बड़े-बड़े देवेश्वर समर्थ नहीं हैं, उन्हीं है, वह सामवेदोक्त शुभ ध्यान भी बतलाया। (बह
- **Translation**: 

---

### Verse 7 (Vaivtpuran 22.6925)
- **Original**: आपकी मैं स्तुति करना चाहता हूँ। आप बुद्धिके ध्यान इस प्रकार है--) जिनके शरीरकी आभा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 22.6926)
- **Original**: परे, सूक्ष्म, तेजोरूपा, सनातनी और अत्यन्त श्वेत चम्पाके पुष्पके सदृश तथा कान्ति सैकड़ों
- **Translation**: 

---

### Verse 9 (Vaivtpuran 22.6927)
- **Original**: अनिर्वचनीया हैं। फिर आपका वर्णन कौन कर चन्द्रमाओंके समान है, जो अग्निमें तपाकर शुद्ध
- **Translation**: 

---

### Verse 10 (Vaivtpuran 22.6928)
- **Original**: सकता है? जगदम्बिके! आप स्वेच्छामयी, की हुई साड़ीको धारण किये हुए तथा रत्ननिर्मित
- **Translation**: 

---

### Verse 11 (Vaivtpuran 22.6929)
- **Original**: निराकार, भक्तोंके लिये मूर्तिमान्‌ अनुग्रहस्वरूप आभूषणोंसे विभूषित हैं, जिनके प्रसन्न मुखपर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 22.6930)
- **Original**: और मन-वाणीसे परे हैं; तब मैं आपकी क्‍या मन्द मुस्कानकी छटा छायी हुई है, जो भक्तोंपर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 22.6931)
- **Original**: स्तुति करूँ। आप चारों वेदोंसे परे, भवसागरकों अनुग्रह करनेवाली, स्वस्थ और अत्यन्त मनोहर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 22.6932)
- **Original**: पार करनेके लिये उपायस्वरूप, सम्पूर्ण अन्नों तथा हैं, सहस्नदल-कमल जिनका आसन है, जो परम
- **Translation**: 

---

### Verse 15 (Vaivtpuran 22.6933)
- **Original**: सारी सम्पदाओंकी अधिदेवी हैं और योगियों- शान्त तथा श्रीहरिकी प्रियतमा पत्नी हैं, उन
- **Translation**: 

---

### Verse 16 (Vaivtpuran 22.6934)
- **Original**: योगों, ज्ञानियों-ज्ञानों, वेदों-वेदबेत्ताऑंकी जननी जगज्जननीका भजन करना चाहिये। देवेन्द्र! इस
- **Translation**: 

---

### Verse 17 (Vaivtpuran 22.6935)
- **Original**: हैं; फिर मैं आपका क्‍या वर्णन कर सकता हूँ! प्रकारके ध्यानसे जब तुम मनोहारिणी लक्ष्मीका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 22.6936)
- **Original**: जिनके बिना सारा जगत्‌ निश्चय ही उसी प्रकार न नतततकततीसस-33+3>->->-----------373333-333--+000000....... *श्रीमधुसूदन उवाच-- गृहाण कवच॑ शक्र सर्वदुःखबिनाशनम्‌ । परमैश्वर्यजनकं. सर्वशन्रुविमर्दनम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 22.6937)
- **Original**: ब्रह्मणे च पुरा दत्त संसरे च जलप्लुते
- **Translation**: 

---

### Verse 20 (Vaivtpuran 22.6938)
- **Original**: यद्‌ धृत्वा जगतां श्रेष्ठ: सर्वश्चर्ययुतों विधि:
- **Translation**: 

---


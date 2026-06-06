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

### Verse 1 (Vaivtpuran 28.7298)
- **Original**: भक्तगण जिन्हें स्वप्रमें भी नहीं देख पाते, उन्हींको तत्पश्चात्‌ शिवजीके वामभागमें कार्तिकेय, दाहिनी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 28.7299)
- **Original**: इस समय मैँ प्रत्यक्ष देख रहा हूँ। जिनकी कलासे ओर गणेश्वर, सामने नन्दीश्वर, महाकाल और [इन्द्र आदि देवगण तथा जिनके कलांशसे चराचर वीरभद्र तथा उनकी गोदमें उनकी प्रियतमा पत्नी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 28.7300)
- **Original**: प्राणी उत्पन्न हुए हैं, उन महेश्वरकों मैं नमस्कार गिरिराजनन्दिनी गौरीको देखा। उन सबको भी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 28.7301)
- **Original**: करता हूँ। जो सूर्य, चन्द्रमा, अग्नि, जल और परशुरामने बड़े हर्षके साथ भक्तिपूर्वक सिर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 28.7302)
- **Original**: बायुके रूपमें विराजमान हैं, उन महेश्वरको मैं झुकाकर नमस्कार किया। उस समय शिवजीका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 28.7303)
- **Original**: अभिवादन करता हूँ। जो स्त्रीरूप, नपुंसकरूप दर्शन करके परशुराम परम संतुष्ट हुए। शोकसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 28.7304)
- **Original**: और पुरुषरूप धारण करके जगत्‌का विस्तार करते पीड़ित तो वे थे ही; अतः आँखोंमें आँसू भरकर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 28.7305)
- **Original**: हैं, जो सबके आधार और सर्वरूप हैं, उन अत्यन्त कातर हो हाथ जोड़कर शान्तभावसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 28.7306)
- **Original**: महेश्वरको मैं नमस्कार करता हूँ। हिमालयकन्या दीन एवं गद़दवाणीके द्वारा शिवजीकी स्तुति
- **Translation**: 

---

### Verse 10 (Vaivtpuran 28.7307)
- **Original**: देवी पार्वतीने कठोर तपस्या करके जिनको प्राप्त करने लगे। किया है। दीर्घ तपस्याके द्वारा भी जिनका प्राप्त परशुराम बोले--ईश! मैं आपकी स्तुति
- **Translation**: 

---

### Verse 11 (Vaivtpuran 28.7308)
- **Original**: होना दुर्लभ है; उन महे श्वरको मैं नमस्कार करता करना चाहता हूँ, परंतु स्तबन करनेमें सर्वथा हूँ। जो सबके लिये कल्पवृक्षरूप हैं और असमर्थ हूँ। आप अक्षर और अक्षरके कारण
- **Translation**: 

---

### Verse 12 (Vaivtpuran 28.7309)
- **Original**: अभिलाषासे भी अधिक फल प्रदान करते हैं, तथा इच्छारहित हैं, तब मैं आपकी क्‍या स्तुति
- **Translation**: 

---

### Verse 13 (Vaivtpuran 28.7310)
- **Original**: जो बहुत शीघ्र प्रसन्न हो जाते हैं और जो भक्तोंके करूँ? मैं मन्दबुद्धि हूँ; मुझमें शब्दोंकी योजना
- **Translation**: 

---

### Verse 14 (Vaivtpuran 28.7311)
- **Original**: बन्धु हैं; उन महेश्वरकों मैं नमस्कार करता हूँ। करनेका ज्ञान तो है नहीं और चला हूँ देवेश्वरकी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 28.7312)
- **Original**: जो लीलापूर्वक क्षणभरमें अनन्त विश्व-सृष्टियोंका स्तुति करने। भला, जिनका स्तवन करनेकी शक्ति
- **Translation**: 

---

### Verse 16 (Vaivtpuran 28.7313)
- **Original**: संहार करनेवाले हैं; उन भयंकर रूपधारी वेदोंमें नहीं है, उन आपकी स्तुति करके कौन
- **Translation**: 

---

### Verse 17 (Vaivtpuran 28.7314)
- **Original**: महेश्वरकों मेरा प्रणाम है। जो कालरूप, कालके पार पा सकता है? आप मन, बुद्धि और वाणीके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 28.7315)
- **Original**: काल, कालके कारण और कालसे उत्पन्न अगोचर, सारसे भी साररूप, परात्पर, ज्ञान और
- **Translation**: 

---

### Verse 19 (Vaivtpuran 28.7316)
- **Original**: होनेवाले हैं तथा जो अजन्मा एवं बारंबार जन्म बुद्धिसे असाध्य, सिद्ध, सिद्धोंद्यात सेवित, आकाशकी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 28.7317)
- **Original**: धारण करनेवाले आदि सब कुछ हैं; उन तरह आदि, मध्य और अन्तसे हीन तथा
- **Translation**: 

---


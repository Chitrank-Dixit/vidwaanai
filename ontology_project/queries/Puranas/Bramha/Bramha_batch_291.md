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

### Verse 1 (Bramha 0.5801)
- **Original**: पुत्र कंसको अर्पित कर दिया। सुना गया है प्रथम उतरवानेके लिये आपकी ही सेवामें उपस्थित हुईं
- **Translation**: 

---

### Verse 2 (Bramha 0.5802)
- **Original**: उत्पन्न हुए छ: गर्भ हिरण्यकशिपुके पुत्र थे, जिन्हें है। हमलोग भी यहाँ उपस्थित हुए हैं। ये इन्द्र,
- **Translation**: 

---

### Verse 3 (Bramha 0.5803)
- **Original**: भगवान्‌ विष्णुकी प्रेरणासे योगनिद्राने क्रमश: दोनों अश्विनीकुमार, वरुण, रुद्र, बसु, आदित्य,
- **Translation**: 

---

### Verse 4 (Bramha 0.5804)
- **Original**: देवकीके उदरमें स्थापित कर दिया था। योगनिद्रा बायु, अग्नि तथा अन्य सम्पूर्ण देवता यहाँ खड़े है।
- **Translation**: 

---

### Verse 5 (Bramha 0.5805)
- **Original**: भगवान्‌ विष्णुको महामाया है, जिसने अविद्यारूपसे देवेश्वर! मुझे तथा इन देवताओंको जो कुछ करना
- **Translation**: 

---

### Verse 6 (Bramha 0.5806)
- **Original**: सम्पूर्ण जगत्‌को मोहित कर रखा है। उससे हो, उसके लिये आज्ञा दीजिये। आपके ही ! श्रीहरिने कहा--“निद्रे! तू मेरी आज्ञासे जा और आदेशका पालन करते हुए हमलोग सदा सम्पूर्ण
- **Translation**: 

---

### Verse 7 (Bramha 0.5807)
- **Original**: पातालवासी छ: गर्भांको एक-एक करके देवकीके दोषोंसे मुक्त रहेंगे। गर्भमें पहुँचा दे। ये सब कंसके हाथसे मारे ब्रह्माजोके इस प्रकार स्तुति करनेपर परमेश्वर
- **Translation**: 

---

### Verse 8 (Bramha 0.5808)
- **Original**: जायँगे। तत्पश्चात्‌ मेरा शेष नामक अंश अपने भगवान्‌ श्रोविष्णुने अपने श्वेत और कृष्ण-दो
- **Translation**: 

---

### Verse 9 (Bramha 0.5809)
- **Original**: अंशांशसे देवकीके उदरमें सातवें गर्भके रूपमें केश उखाड़े और देवताओंसे कहा--'मेरे ये दोनों
- **Translation**: 

---

### Verse 10 (Bramha 0.5810)
- **Original**: प्रकट होगा। बसुदेवजीकी दूसरी भार्या रोहिणी क्रैश ही भूतलपर अबतार ले पृथ्वीके भार और
- **Translation**: 

---

### Verse 11 (Bramha 0.5811)
- **Original**: आजकल गोकुलमें रहती हैं। तू प्रसबकालमें बह कलेशका नाश करेंगे। सम्पूर्ण देवता भी अपने-
- **Translation**: 

---

### Verse 12 (Bramha 0.5812)
- **Original**: गर्भ रोहिणीके ही उदरमें डाल देना। उसके अपने अंशसे पृथ्वीपर अवठीर्ण हो पहलेसे उत्पन्न
- **Translation**: 

---

### Verse 13 (Bramha 0.5813)
- **Original**: बिषयमें लोग यही कहेंगे कि 'देवकीौका सातवाँ हुए. उन्मत्त दैत्योंके साथ युद्ध करें। इसमें संदेह
- **Translation**: 

---

### Verse 14 (Bramha 0.5814)
- **Original**: गर्भ भोजराज कंसके डरसे गिर गया।' गर्भका नहीं कि नाना प्रकारके अस्त्र-शस्त्रोंसे चूर्ण होकर
- **Translation**: 

---

### Verse 15 (Bramha 0.5815)
- **Original**: संकर्षण होनेसे रोहिणीका वह वीर पुत्र लोकमें सम्पूर्ण दैत्य नष्ट हो जायँगे। बसुदेवकी पत्नी जो
- **Translation**: 

---

### Verse 16 (Bramha 0.5816)
- **Original**: 'संकर्षण' नामसे विख्यात होगा। उसके शरीरका
- **Translation**: 

---

### Verse 17 (Bramha 0.5817)
- **Original**: 278 » संक्षिप्त भ्रह्मपुराण « वर्ण श्वेतगिरिके शिखरकी भाँति गौर होगा। तदनन्तर
- **Translation**: 

---

### Verse 18 (Bramha 0.5818)
- **Original**: अनेक स्थान बनाकर सारी पृथ्वीकी शोभा बढ़ायेगी। पैं देवकीके उदरमें प्रवेश करूँगा। उस समय तुझे
- **Translation**: 

---

### Verse 19 (Bramha 0.5819)
- **Original**: भूति, संनति, कीर्ति, कान्ति, पृथ्वी, धृति, लज्जा, भी यशोदाके गर्भमें अविलम्ब प्रवेश करना होगा।
- **Translation**: 

---

### Verse 20 (Bramha 0.5820)
- **Original**: पुष्टि, उषा तथा अन्य जो भी स्त्री-नामधारी वस्तु वर्षा-ऋतुमें क्रवणमासके* कृष्णपक्षकी अष्टमी तिधिको
- **Translation**: 

---


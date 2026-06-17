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

### Verse 1 (Vaivtpuran 28.4326)
- **Original**: हैं, उन शुद्धसत्त्वस्वरूपा देवी षष्ठीको बार-बार आचमनीय, गन्ध, धूप, दीप, विविध प्रकारके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 28.4327)
- **Original**: नमस्कार है। हिंसा और क्रोधसे रहेत भगवती नैवेद्य तथा सुन्दर फलद्वारा भगवतीकी पूजा करनी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 28.4328)
- **Original**: षष्ठीको बार-बार नमस्कार है। सुरेश्वरि ! तुम मुझे चाहिये। उपचार अर्पण करनेके पूर्व '$& हीं
- **Translation**: 

---

### Verse 4 (Vaivtpuran 28.4329)
- **Original**: धन दो, प्रिय पत्नी दो और पुत्र देनेकी कृपा यष्टीदेव्ये स्वाहा' इस मन्त्रका उच्चारण करना
- **Translation**: 

---

### Verse 5 (Vaivtpuran 28.4330)
- **Original**: करो। महेश्वरि! तुम मुझे सम्मान दो, विजय विहित है। पूजक पुरुषकों चाहिये कि यथाशक्ति
- **Translation**: 

---

### Verse 6 (Vaivtpuran 28.4331)
- **Original**: दो और मेरे शत्रुओंका संहार कर डालो। धन इस अटष्टाक्षर महामन्त्रका जप भी करे। और यश प्रदान करनेवाली भगवती पषष्टीकों बार- तदनन्तर मनको शान्त करके भक्तिपूर्वक
- **Translation**: 

---

### Verse 7 (Vaivtpuran 28.4332)
- **Original**: बार नमस्कार है। सुपूजिते! तुम भूमि दो, प्रजा स्तुति करनेके पश्चात्‌ देवीको प्रणाम करे। फल
- **Translation**: 

---

### Verse 8 (Vaivtpuran 28.4333)
- **Original**: दो, विद्या दो तथा कल्याण एवं जय प्रदान करो। प्रदान करनेवाला यह उत्तम स्तोत्र सामवेदमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 28.4334)
- **Original**: तुम षष्ठीदेबीको बार-बार नमस्कार है।' वर्णित है। जो पुरुष देवीके उपर्युक्त अष्टाक्ष
- **Translation**: 

---

### Verse 10 (Vaivtpuran 28.4335)
- **Original**: इस प्रकार स्तुति करनेके पश्चात्‌ महाराज महामन्त्रका एक लाख जप करता है, उसे अवश्य
- **Translation**: 

---

### Verse 11 (Vaivtpuran 28.4336)
- **Original**: प्रियत्रतने षष्ठीदेवीके प्रभावसे यशस्य्री पुत्र प्रात कर ही उत्तम पुत्रकी प्राप्ति होती है, ऐसा ब्रह्माजीने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 28.4337)
- **Original**: लिया। ब्रह्मन! जो पुरुष भगवती षष्ठीके इस कहा है। मुनिवर! अब सम्पूर्ण शुभ कामनाओंको
- **Translation**: 

---

### Verse 13 (Vaivtpuran 28.4338)
- **Original**: स्तोत्रको एक वर्षतक श्रवण करता है, वह यदि प्रदान करनेवाला स्तोत्र सुनो। नारद! सबका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 28.4339)
- **Original**: अपुत्री हो तो दीर्घजीवी सुन्दर पुत्र प्राप्त कर लेता मनोरथ पूर्ण करनेवाला यह स्तोत्र बेदोंमें गोप्य है। है। जो एक वर्षतक भक्तिपूर्वक देवीकी पूजा *देवीको नमस्कार है। महादेवीको नमस्कार
- **Translation**: 

---

### Verse 15 (Vaivtpuran 28.4340)
- **Original**: करके इनका यह स्तोत्र सुनता है, उसके सम्पूर्ण है। भगवती सिद्धि एवं शान्तिको नमस्कार है।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 28.4341)
- **Original**: पाप विलीन हो जाते हैं। महान्‌ वन्ध्या भी इसके शुभा, देवसेना एवं भगवती षष्ठीको बार-बार
- **Translation**: 

---

### Verse 17 (Vaivtpuran 28.4342)
- **Original**: प्रसादसे संतान प्रसव करनेकी योग्यता प्राप्त कर नमस्कार है। बरदा, पुत्रदा, धनदा, सुखदा एवं
- **Translation**: 

---

### Verse 18 (Vaivtpuran 28.4343)
- **Original**: लेती है। वह भगवती देबसेनाकी कृपासे गुणी, मोक्षदा भगवती षष्ठीको बार-बार नमस्कार है।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 28.4344)
- **Original**: विद्वान, यशस्वी, दीर्घायु एवं श्रेष्ठ पुत्रकी जननी मूलप्रकृतिके छठे अंशसे प्रकट होनेवाली भगवती
- **Translation**: 

---

### Verse 20 (Vaivtpuran 28.4345)
- **Original**: होती है। काकवन्ध्या अथवा मृतवत्सा नारी एक सिद्धाकों नमस्कार है। माया, सिद्धयोगिनी, सारा,
- **Translation**: 

---


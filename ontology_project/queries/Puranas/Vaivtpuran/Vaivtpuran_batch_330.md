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

### Verse 1 (Vaivtpuran 15.8730)
- **Original**: हो आता था। इसी समय ब्रह्माजी पृथ्वी तथा जलानेवाले तथा ब्राह्मण होकर शुद्रान्न भोजन
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.8731)
- **Original**: नतमस्तक देवसमूहोंके साथ महादेवजीके सामने करनेवाले हैं; उनके भारसे मुझे बड़ा कष्ट जा खड़े हुए। जगदगुरुको आया देख भगवान्‌ है। जो मूढ़ पूजा, यज्ञ, उपवास-व्रत और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.8732)
- **Original**: शंकर शीघ्र हो भक्तिभावसे उठकर खड़े हो गये। नियमको तोड़नेवाले हैं; उनके भारसे भी मुझे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.8733)
- **Original**: उन्होंने प्रेमपूर्वक मस्तक झुकाकर उन्हें प्रणाम बड़ी पीड़ा होती है। जो पापी सदा गौ, ब्राह्मण, [किया और उनका आशीर्वाद प्राप्त किया। देवता, वैष्णव, श्रीहरि, हरिकथा और हरिभक्तिसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.8734)
- **Original**: तत्पश्चात्‌ सब देवताओंने तथा पृथ्वीने भी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.8735)
- **Original**: $ श्रोकृष्णजन्मखण्ड * 403 +004]/)।।।0
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.8736)
- **Original**: ।। 4, 4 /4404049 484 444
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.8737)
- **Original**: 0 4/40494049494/494943494439--4+ >> -#न्‍न्‍न्‍न्‍नन न ]]]0 00000 5] 6 6
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.8738)
- **Original**: $%क$ककं# ####क##%%$%%$%# 8 # 85 भक्तिभावसे चन्द्रशेखर शिवको प्रणाम किया और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.8739)
- **Original**: वे प्रकाशित हो रहे थे। उनके चार भुजाएँ थीं शिवने उन सबको आशीर्वाद दिया। प्रजापति
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.8740)
- **Original**: और मुखपर मन्द मुस्कानकी छटा छा रही थी। ब्रह्माने पार्वतीनाथ शिवसे सारा वृत्तान्त कहा। बह
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.8741)
- **Original**: सुनन्‍्द, नन्‍्द और कुमुद आदि पार्षद उनकी सब सुनकर भक्तवत्सल शंकरने तुरंत ही मुँह
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.8742)
- **Original**: सेवामें जुटे थे। उनका सम्पूर्ण अज्ज चन्दनसे नीचा कर लिया। भक्तोंपर कष्ट आया सुनकर [चर्चित था तथा उनका मस्तक रलज्लमय मुकुटसे पार्वती और परमेश्वर शिवको बड़ा दुःख हुआ।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.8743)
- **Original**: जगमगा रहा था। वे परमानन्द-स्वरूप भगवान्‌ तदनन्तर ब्रह्मा और शिवने देवसमूहों तथा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.8744)
- **Original**: भक्तोंपर अनुग्रह करनेके लिये व्याकुल दिखायी बसुधाको यत्रपूर्वक सान्त्वना देकर घरको लौटा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.8745)
- **Original**: देते थे। मुने! ब्रह्मा आदि देवेश्वरोंने भक्तिभावसे दिया। फिर वे दोनों देवेश्वर तुरंत धर्मके घर आये
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.8746)
- **Original**: उनके चरणोंमें प्रणाम किया और श्रद्धापूर्वक और उनके साथ विचार-विमर्श करके वे तीनों
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.8747)
- **Original**: मस्तक झुकाकर बड़ी भक्तिके साथ उनकी स्तुति श्रीहरिके धामको चल दिये। भगवान्‌के उस परम
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.8748)
- **Original**: की। उस समय वे परमानन्दके भारसे दबे हुए धामका नाम बैकुण्ठ है। वह जरा और मृत्युको
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.8749)
- **Original**: थे। उनके अब्जोंमें रोमात्ष हो आया था। दूर भगानेवाला है। ब्रह्माण्डसे ऊपर उसकी स्थिति
- **Translation**: 

---


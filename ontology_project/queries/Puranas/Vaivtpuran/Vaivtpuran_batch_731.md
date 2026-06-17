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

### Verse 1 (Vaivtpuran 543.12934)
- **Original**: यही सोचती थीं कि पुरुष अपनी स्ट्रियोंके रूप, मनोहर थी। विधाताकी सृष्टिमें गिरिराजनन्दिनीके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12935)
- **Original**: यौवन तथा वेशभूषाका ग्राहक है। शिव मेरा नाम लिये कहीं कोई उपमा नहीं थी। गुणोंकी तो
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12936)
- **Original**: सुनते ही बिना तपस्याके मुझे ग्रहण कर लेंगे। वे जननी ही हैं; अत: सभी और सब प्रकारके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12937)
- **Original**: मनमें यह विश्वास लेकर गिरिजा हिमवान्‌के घरमें सदुणोंको धारण करती हैं। समस्त देवपत्रियाँ रहती थीं और दिन-रात सखी-सहेलियोंके बीच उनकी सोलहवों कलाके बराबर भी नहीं हैं। खेल-कूदमें मतवाली रहा करती थीं। इसी समय जैसे शुक्लपक्षमें चन्द्रमाकी कला बढ़ती है, उसी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12938)
- **Original**: शीघ्रतापूर्वक दूतने गिरिराजके भवनमें आकर तरह हिमालयके घरमें वे देवी दिनोंदिन बढ़ने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12939)
- **Original**: दोनों हाथ जोड़ उनके सामने मधुर वाणीमें कहा। लगीं। जब उन्होंने युवावस्थामें प्रवेश किया, तब
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12940)
- **Original**: दूत बोला--शैलराज! उठिये, उठिये। उन जगदम्बाको सम्बोधित करके आकाशवाणीने
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12941)
- **Original**: अक्षयवटके पास जाइये। वहाँ वृषभवाहन महादेवजी कहा--'शिवे! तुम कठोर तपस्याद्वारा भगवान्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12942)
- **Original**: अपने गणोंके साथ पधारे हैं। महाराज! आप शिवको पति-रूपमें प्राप्त करो; क्योंकि तपस्याके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12943)
- **Original**: भक्तिभावसे मस्तक झुका उन्हें मधुपर्क आदि बिना ईश्वरकों पाना अथवा उनके अंशसे गर्भ
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12944)
- **Original**: देकर उन इन्द्रियातीत देवेश्वरका पूजन कौजिये।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12945)
- **Original**: 566 * संक्षिमत ब्रह्मवैवर्तपुराण « 55% 6$$# $# 4 $ 44 # 5 $ 5 # % ## ## 6 # 85884 646 66 6 8 4 8 # 8 कक 4 # 5 कक ऊ 4 5 55 51% # 4 $ 44 4 56 4 6 8 5 4 5 महादेवजी सिद्धिस्वरूप, सिद्धोंके स्वामी, योगीद्धोंके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12946)
- **Original**: और प्रत्येक मुखमें तीन-तीन नेत्र थे। उनके गुरुके भी गुरु, मृत्युझ्य, कालके भी काल तथा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12947)
- **Original**: श्रीअज्ञोंसे करोड़ों सूयोके समान प्रकाश फैल सनातन ब्रह्मज्योति हैं। वे प्रभु परमात्मस्वरूप, [रहा था। हिमवानने उनके चारों ओर एकादश सगुण तथा निर्गुण हैं। उन्होंने भक्तोंके ध्यानके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12948)
- **Original**: रुद्रोंको देखा, जो ब्रह्मतेजसे प्रकाशमान थे। लिये निर्मल महेश्वररूप धारण किया है।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12949)
- **Original**: शिवके वामभाग़में महाकाल और दाहिने भागमें दूतकी यह बात सुनकर हिमवान्‌ प्रसन्नता-
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12950)
- **Original**: नन्दिकेश्वर खड़े थे। भूत, प्रेत, पिशाच, कूष्माण्ड, पूर्वक उठे और मधुपर्क आदि साथ ले भगवान्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12951)
- **Original**: ब्रह्मराक्षस, बेताल, क्षेत्रपाल, भयानक पराक्रमी शंकरके समीप गये। दूतकी पूर्वोक्त बात सुनकर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12952)
- **Original**: भैरव, सनक, सननन्‍्दन, सनत्कुमार, सनातन, देवी शिवाके मुख और नेत्र प्रसन्नतासे खिल उठे।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12953)
- **Original**: जैगीषव्य, कात्यायन, दुर्वासा और अष्टावक्र आदि उन्होंने अपने मनमें यही माना कि महेश्वर
- **Translation**: 

---


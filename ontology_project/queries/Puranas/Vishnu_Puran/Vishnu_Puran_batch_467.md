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

### Verse 1 (Vishnu Puran 0.9321)
- **Original**: 14 आताप्रनयन: कोपाहविषज्वालाकुलैर्मुसैः । वृतो.. महाविषैश्वान्यैरुरगैरनिलाशनैः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9322)
- **Original**: 15 नागपत्यश्व शतशो हारिहारोपश्ोभिता: । प्रकप्पिततनुक्षेपचलत्कुण्डलकान्तय:;.
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9323)
- **Original**: 16 ततः ग्रवेष्टितस्सपैंस्स कृष्णो भोगबन्धनैः । दर्दशुस्तेषपि ते कृष्णं विषज्वालाकुलैमुखै:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9324)
- **Original**: 17 ते तत्र पतितं दृष्ठा सर्पभोगैर्निपीडितम्‌। गोपा ब्रजमुपागम्य चुक्तुशु: शोकलालसा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9325)
- **Original**: 18 गोपा ऊचु: एघ मोह गत: कृष्णो मगझ्नो वै काल्यडहुदे । भ्रक्ष्तते नागराजेन तमागच्छत पहयत
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9326)
- **Original**: 19 तच्छुत्वा तत्र ते गोपा वज्रपातोपरम बच: । गोप्यश्न त्वरिता जग्पुर्यशोदाप्रमुखा हृदम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9327)
- **Original**: 20 हा हा क्रासाविति जनो गोपीनामतिविद्ञलः । यझोदया सम भ्रान्तो द्वुतप्रस्खलितं ययौ
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9328)
- **Original**: 21 नन्‍्दगोपश्च गोपाश्च रामश्वाद्भधुतविक्रम: । त्वरित बमुनां जम्मुः कृष्णदर्शनलालसा:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9329)
- **Original**: 22 ददृशुआपि ते तत्र सर्पराजवशाड्तम्‌। निष्प्रबत्नीकृतं कृष्ण सर्पभोगविवेष्टितम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9330)
- **Original**: 23 ननन्‍्दगोपो5पि निश्वेष्टो न्यस्य पुत्रमुखे दृशाम्‌। यश्ोदा च महाभागा बभूव मुनिसत्तम
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9331)
- **Original**: 24ड गोप्यस्त्वन्या रुदन्त्यश्न ददुशु: शोककातरा: । प्रोचुश्न केशव प्रीत्या भयकातर्यगढ़रदम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9332)
- **Original**: 25 ग्रेष्पय ऊचुः सर्वा यजश्ञोदया सार्ड विशामो5त्र महाहुदम्‌ । सर्पराजस्यथ नो गन्तुमस्माभिर्युज्यते त्रजम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9333)
- **Original**: 26 दिवस: को बिना सूर्य बिना चन्द्रेण का निशा । बिना वृषेण का गाबो बिना कृष्णेन को ब्रज:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9334)
- **Original**: 27 उस सर्पके विषम विषकी ज्वाल्से तपे हि जल्से भीगनेके कारण जे वृक्ष तुरत ही जल उठे और उनकी ज्यालाओंसे सम्पूर्ण दिज्लाएँ व्याप्त हो गयीं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9335)
- **Original**: तब कृष्णचन्द्रने उस नागकुण्डमें अपनी भुजाओंकों ठॉका; उनका दाब्द सुनते ही बह नागयज तुरंत उनके सम्मुख आ गया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9336)
- **Original**: तसके नेत्र क्रोधसे कुछ ताप्रवर्ण हो रहे थे, मुखोंसे अग्रिकी छपटें निकऊ रही थीं और बह महाविषैले अन्य वायुभक्षी सपॉसे घिय हुआ था
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9337)
- **Original**: उसके साथयमें मनोहर हारोंसे भूषिता और झरीर-कम्पनसे हिलते हुए कुण्डललॉकी कान्तिसे सुशोभिता सैकड़ों नागपत्नियाँ थीं। 16
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9338)
- **Original**: तब सर्पोनि कुण्डल्थकार होकर कृष्णचद्धको अपने शरौरसे बाँध लिया और अपने विषाधरि-सन्तप्त मुशॉसे काटने लगे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9339)
- **Original**: तदनन्तर गोपगण कृष्णयन्द्रको नागकुण्डमें गिरा हुआ और सर्पेकि फणोंसे पीडित होता देख अ्जमें चले आये और शोकसे व्याकुछ होकर रोने छगें
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9340)
- **Original**: गोपगण बोछे--आओ, आओ, देखो ! यह कृष्ण कालीदहमें डूबकर मूच्छित हो गया है, देखो इसे नागराज खाये जाता है
- **Translation**: 

---


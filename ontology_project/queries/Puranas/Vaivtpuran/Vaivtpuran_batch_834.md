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

### Verse 1 (Vaivtpuran 543.14994)
- **Original**: वृक्षोंमें कल्पवृक्ष, कामधेनुओंमें सुरभि, नदियोंमें है। प्रकृति मेरा ही विकार है अर्थात्‌ वह प्रकृति
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14995)
- **Original**: पापनाशिनी गड्गा, पण्डितोंमें पाण्डित्यपूर्ण बाणी, भी मैं ही हूँ। जैसे दूधमें धवलता होती है। दूध
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14996)
- **Original**: मन्त्रोंमें प्रणव, विद्याओंमें उनका बीजरूप तथा और धवलतामें कभी भेद नहीं होता। जैसे जलमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14997)
- **Original**: खेतसे पैदा होनेवाली वस्तुओंमें धान्य हूँ।फलबान्‌ शीतलता, अग्निमें दाहिका शक्ति, आकाशमें शब्द,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14998)
- **Original**: वृक्षोंमें पीपल, गुरुओंमें मन्त्रदाता गुरु, प्रजापतियोंमें भूमिमें गन्ध, चन्द्रमामें शोभा, सूर्यमें प्रभा और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14999)
- **Original**: कश्यप, पक्षियोंमें गरुड़, नागोंमें अनन्त (शेषनाग), जीबमें आत्मा है; उसी प्रकार राधाके साथ मुझको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15000)
- **Original**: नरोंमें नरेश, ब्रह्मर्षियोंमें भृगु, देवर्षियोंमें नारद, अभिन्न समझो। तुम राधाको साधारण गोपी और
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15001)
- **Original**: राजर्षियोंमें जनक, महर्षियोंमें शुक, गन्धवॉमें मुझे अपना पुत्र न जानो। मैं सबका उत्पादक
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15002)
- **Original**: चित्ररथ, सिद्धोंमें कपिलमुनि, बुद्धिमानोंमें बृहस्पति, परमेश्वर हूँ और राधा ईश्वरी प्रकृति है*।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15003)
- **Original**: कबियोंमें शुक्राचार्य, ग्रहोंमें शनि, शिल्पियोंमें बाबा! मेरी सुखदायिनों विभूतिका वर्णन विश्वकर्मा, मृगोंमें मृगेन्द्र, वृषभोंमें शिववाहन सुनो, जिसे पहले मैंने अव्यक्तजन्मा ब्रह्माजीको
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15004)
- **Original**: नदी, गजराजोंमें ऐराबत, छन्‍्दोंमें गायत्री, सम्पूर्ण बताया था। मैं देवताओंमें श्रीकृष्ण हूँ। गोलोकमें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15005)
- **Original**: शास्त्रोंमें बेद, जलचरोंमें उनका राजा वरुण, स्वयं ही द्विभुजरूपसे निवास करता हूँ और अप्सराओमें उर्वशी, समुद्रोंमें जलनिधि, पर्वतोंमें वैकुण्ठमें चतुर्भुज विष्णुरूपसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15006)
- **Original**: शिवलोकमें मैं ही
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15007)
- **Original**: सुमेरु, रत्रवान्‌ शैलोंमें हिमालय, प्रकृतियोंमें देवी शिव हूँ। ब्रह्मलोकमें ब्रह्मा हूँ। तेजस्वियोंमें सूर्य
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15008)
- **Original**: पार्वती तथा देवियोंमें लक्ष्मी हूँ। हूँ। पवित्रोंमें अग्नि हूँ। द्रव-पदार्थोमें जल हूँ।। मैं नारियोंमें शतरूपा, अपनी प्रियतमाओंमें + यथा जीवस्तथात्मा च तथैव राधया स॒ह। त्यज त्वं गोपिकाबुद्धिं राधायां मयि पुत्रताम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15009)
- **Original**: अहं सर्वस्य प्रभव: सा च प्रकृतिरीश्वरी। (73। 506 ) [63] ] सं0 ब्ल0 जै0 पुराण 22
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15010)
- **Original**: 652 के संक्षिप्त श्रह्मैवर्तपुराण क्र
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15011)
- **Original**: #8#8 88 ## 8 # ##ऋ ## # %## # कड़क ऊऋऊऋऋऊऋकऋकऊऋ कक कुक ऊ्ुक $%%#%#%#%# # ####% 4; #%कश् राधिका तथा साध्वी स्त्रियोंमें निश्चय ही वेदमाता
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15012)
- **Original**: उद्धव, पशुजीबोंमें गौ, बनोंमें चन्दन, पतित्रोंमें सावित्री हूँ। दैत्योंमें प्रह्माद, बलिष्ठोंमें बलि,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15013)
- **Original**: तीर्थ और निःशंकोंमें वैष्णव हूँ; बैष्णवसे बढ़कर ज्ञानियोंमें भगवान्‌ नारायण ऋषि, वानरोंमें हनुमान्‌,
- **Translation**: 

---

